from fastapi import FastAPI, File, Form, UploadFile, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates
import fitz, os, time
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from analyse_pdf import analyse_resume_gemini

app = FastAPI()
templates = Jinja2Templates(directory="templates")
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Prometheus metrics ---
REQUEST_COUNT = Counter("request_count", "Total number of requests")
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency in seconds")

@app.middleware("http")
async def add_metrics(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(time.time() - start_time)
    return response

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/", response_class=HTMLResponse)
async def upload_resume(
    request: Request,
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    pdf_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    with open(pdf_path, "wb") as f:
        f.write(await resume.read())

    doc = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in doc)
    result = analyse_resume_gemini(text, job_description)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
