#Resume analysis 

This project is an AI-driven résumé analysis platform that automatically extracts content from PDF résumés, compares it with job descriptions, and generates actionable insights using Gemini AI.
It is built with FastAPI for high-performance backend services and includes Prometheus and Grafana to provide real-time monitoring, request analytics, and application performance dashboards.
The entire system runs in lightweight, isolated services using Docker, making it easy to deploy, scale, and monitor.

🚀 Features

🔍 AI-Powered Résumé Analysis
Uses Gemini AI to compare résumé content with job descriptions and generate actionable insights.

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

🧩 Extensible & Clean Codebase
Ideal for learning, showcasing, and expanding.

🛠️ Technologies Used
First Header | Second Header 
------------ | ------------- 
FastAPI	Backend | framework
Gemini API	AI model | for résumé analysis
PyMuPDF (Fitz)	| PDF text extraction
Prometheus |	Metrics collection
Grafana 	|Metrics visualization
Docker & Docker Compose |	Containerized deployment
Python | Core programming language

📂 Project Structure
project/
│── main.py
│── analyse_pdf.py
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── prometheus.yml
│── templates/
│     └── index.html
│── uploads/ (ignored by Git)
│── .gitignore
└── README.md

