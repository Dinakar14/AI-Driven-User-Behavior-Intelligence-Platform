# AI-Driven-User-Behavior-Intelligence-Platform
The AI-Driven User Behavior Intelligence Platform is a production-ready machine learning system designed to analyze user behavior and predict customer churn. The project demonstrates how real-world AI systems are built, deployed, and scaled using modern industry tools.

This is not just a model, but a complete AI system deployed as microservices using Docker and Kubernetes.

🎯 Problem Statement

Customer churn is one of the biggest challenges faced by digital platforms such as:

SaaS products

E-commerce websites

Mobile applications

FinTech platforms

Traditional churn analysis is:

Manual

Slow

Not scalable

👉 This project solves the problem by providing an automated AI-based churn prediction system with a business-friendly dashboard.

🧠 Solution Highlights

Predicts whether a user is likely to churn

Provides real-time predictions via API

Interactive dashboard for non-technical users

Fully containerized using Docker

Deployed and orchestrated using Kubernetes

Microservices-based architecture (industry standard)

🏗️ System Architecture
User → Streamlit Dashboard
        ↓
FastAPI Backend (Churn Prediction API)
        ↓
ML Logic / Scoring

Architecture Characteristics

Streamlit = Frontend service

FastAPI = Backend inference service

Kubernetes = Service discovery & orchestration

Docker = Consistent deployment

🛠️ Tech Stack
Layer	Technology
Programming	Python
Backend API	FastAPI
Frontend	Streamlit
Containerization	Docker
Orchestration	Kubernetes
Data Handling	Pandas
Deployment	Docker Desktop (Local Kubernetes)
📁 Project Structure
ai-user-intelligence/
│
├── api/                    # FastAPI backend
│   └── app.py
│
├── dashboard/              # Streamlit dashboard
│   └── app.py
│
├── data/                   # Dataset
│   └── user_events.csv
│
├── docker/                 # Dockerfiles
│   ├── Dockerfile.api
│   └── Dockerfile.dashboard
│
├── k8s/                    # Kubernetes manifests
│   ├── api-deployment.yaml
│   ├── api-service.yaml
│   ├── dashboard-deployment.yaml
│   └── dashboard-service.yaml
│
├── requirements.txt
└── docker-compose.yml

⚙️ How the System Works

User opens the Streamlit dashboard

Inputs user behavior data

Dashboard sends request to FastAPI service

FastAPI evaluates churn risk

Prediction is returned and displayed

All communication happens inside Kubernetes using service DNS.

🐳 Docker Setup
Build Images
docker build -t ai-user-api:latest -f docker/Dockerfile.api .
docker build -t ai-user-dashboard:latest -f docker/Dockerfile.dashboard .

☸️ Kubernetes Deployment
Deploy Services
kubectl apply -f k8s/

Verify Pods
kubectl get pods


Expected:

ai-api-xxxxx         1/1   Running
ai-dashboard-xxxxx   1/1   Running

🌐 Access the Dashboard

Check NodePort:

kubectl get svc ai-dashboard-service


Open in browser:

http://localhost:<NODE_PORT>


Example:

http://localhost:31622

🔗 Service-to-Service Communication

Inside Kubernetes:

Dashboard communicates with API using:

http://ai-api-service:8000


✔️ No localhost
✔️ Production-style microservice networking

📊 Churn Prediction Logic (Current)

The system calculates a risk score based on:

Session count

Time spent

Purchase history

Inactivity duration

High risk → Likely to churn
Low risk → Active user


Architecture supports future integration of real ML models such as XGBoost, Random Forest, or Neural Networks.

🎓 Why This Project Is Different
Typical Student Project	This Project
Single Python file	Microservices
Local execution	Kubernetes
No deployment	Dockerized
No UI	Business dashboard
Academic only	Industry-ready
💼 Skills Demonstrated

AI & ML fundamentals

Backend API development

Frontend analytics dashboard

Docker containerization

Kubernetes orchestration

Microservice architecture

Production-grade deployment

📈 Business Impact

Early identification of at-risk users

Improved customer retention

Data-driven business decisions

Scalable architecture for growth

🔮 Future Enhancements

Integration of trained ML models (XGBoost / DL)

MLflow model registry

Prediction history & analytics

Cloud deployment (AWS / GCP / Azure)

👤 Author

Dinakar Subramanian
AI & Machine Learning Engineer (Fresher)
📍 India
CI/CD pipelines

Authentication & security
