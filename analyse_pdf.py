import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# --- 1. Load environment variables ---
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --- 2. Configure the Gemini model ---
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config={
        "temperature": 0.4,           # Balanced creativity for consistency
        "top_p": 0.9,
        "top_k": 40,
        "max_output_tokens": 2048,
        "response_mime_type": "text/plain"
    }
)

# --- 3. Define the resume analysis function ---
def analyse_resume_gemini(resume_content, job_description):
    """
    Compare a resume with a job description using Google's Gemini model.
    Returns a structured Python dict containing ATS-style evaluation results
    plus personalized career recommendations.
    """

    # --- a. Structured JSON prompt ---
    prompt = f"""
You are an expert ATS evaluator and career advisor.

Compare the following resume with the provided job description and return results
**strictly in valid JSON format only** — no explanations or text outside JSON.

Expected JSON structure:
{{
  "match_score": int,
  "matched_keywords": [list],
  "missing_keywords": [list],
  "experience_fit": str,
  "formatting_issues": [list],
  "suggestions": [list],
  "summary": str,
  "career_recommendations": {{
      "skills_to_learn": [list],
      "recommended_courses": [list],
      "projects_to_build": [list],
      "networking_tips": [list]
  }}
}}

Resume:
{resume_content}

Job Description:
{job_description}

Rules:
- Output ONLY valid JSON (no markdown, code fences, or commentary).
- Be realistic and professional.
- For each course, include a short title and platform if possible.
- Ensure all lists are properly formatted arrays.
"""

    # --- b. Call Gemini API ---
    response = model.generate_content(prompt)
    text = getattr(response, "text", None) or getattr(response, "output_text", "")

    # --- c. Cleanup ---
    text = text.strip()
    if text.startswith("```json"):
        text = text.replace("```json", "")
    if text.endswith("```"):
        text = text.replace("```", "")
    text = text.strip()

    # --- d. Try parsing JSON safely ---
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        print("⚠️ Invalid JSON returned by Gemini. Raw output:\n", text)
        data = {
            "error": "Invalid JSON format",
            "raw_output": text,
            "match_score": 0,
            "matched_keywords": [],
            "missing_keywords": [],
            "experience_fit": "Unknown",
            "formatting_issues": [],
            "suggestions": ["Could not analyze due to output formatting issues."],
            "summary": "Error in AI output.",
            "career_recommendations": {
                "skills_to_learn": [],
                "recommended_courses": [],
                "projects_to_build": [],
                "networking_tips": []
            }
        }

    # --- e. Add a human-readable fit label ---
    score = data.get("match_score", 0)
    if isinstance(score, (int, float)):
        if score >= 80:
            data["fit_level"] = "Excellent Match ✅"
        elif score >= 60:
            data["fit_level"] = "Good Match ⚙️"
        else:
            data["fit_level"] = "Needs Improvement ⚠️"

    return data
