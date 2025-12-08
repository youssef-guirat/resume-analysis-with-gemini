# Resume analysis 

This project is an AI-driven résumé analysis platform that automatically extracts content from PDF résumés, compares it with job descriptions, and generates actionable insights using Gemini AI.
It is built with FastAPI for high-performance backend services and includes Prometheus and Grafana to provide real-time monitoring, request analytics, and application performance dashboards.
The entire system runs in lightweight, isolated services using Docker, making it easy to deploy, scale, and monitor.

🚀 Features

🔍 AI-Powered Résumé Analysis
Analyse résumé content using Gemini 2.0 Flash

Compare résumé text vs job description

Extract strengths, weaknesses, and an overall matching score

Generate clear, actionable recommendations

📄 PDF Text Extraction
Uses PyMuPDF (Fitz) for fast and accurate text extraction.

⚡ FastAPI Backend
High-performance REST API for fast résumé processing.

📊 Real-Time Monitoring
Track résumé uploads, request count, latency, processing time, and API performance.

📈 Grafana Dashboards
Clean and real-time visualization of Prometheus metrics.

🐳 Dockerized Architecture
Easy deployment using Docker + Docker Compose.


🛠️ Technologies Used
Technologie | Purpose
------------ | ------------- 
FastAPI	Backend | framework
Gemini API	AI model | for résumé analysis
PyMuPDF (Fitz)	| PDF text extraction
Prometheus |	Metrics collection
Grafana 	|Metrics visualization
Docker & Docker Compose |	Containerized deployment
Python | Core programming language


### Structure
📂 Project Structure
```
project/
│── main.py
│── analyse_pdf.py
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── prometheus.yml
│── templates/
│     └── index.html
│── .gitignore
└── README.md
```
## 🐳 Run the Project
🔥 Option 1 — Run with Docker 
1️⃣ Start all services
```
docker-compose up -d
```
2️⃣ Access Services
Service	| URL
------------ | ------------- 
FastAPI App | http://localhost:8000
Prometheus | http://localhost:9090
Grafana | http://localhost:3000


Grafana Login

Username: admin

Password: admin

## 🖥️ Option 2 — Run Locally
1️⃣ Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```
2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

3️⃣ Start FastAPI
```
uvicorn main:app --reload
```

➡️ Open browser → http://localhost:8000

🔑 API Key Setup (Required)

Gemini API is needed for AI résumé analysis.

✅ Step 1 — Get Your API Key

➡️ Visit:

👉 https://aistudio.google.com/apikey

Create an API key and copy it.

✅ Step 2 — Create a .env File

In the project root (same level as main.py) create:
```
.env
```

Add your key:
```
GEMINI_API_KEY=your_api_key_here
```
✅ Step 3 — Done

The project automatically loads the key using python-dotenv

.env is already in .gitignore → it will NOT be committed

