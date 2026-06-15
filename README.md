# TechShop API 🛒

A Flask-based e-commerce REST API with a full DevOps pipeline.

## 🚀 Tech Stack

- **App:** Python / Flask
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Registry:** Docker Hub
- **Orchestration:** Kubernetes (Minikube)
- **Monitoring:** Prometheus + Grafana

## �endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/products` | List all products |
| GET | `/health` | Health check |

## ⚙️ CI/CD Pipeline

Every push to `main` branch:
1. Builds Docker image
2. Pushes to Docker Hub (`fulyag/techshop`)

## ☸️ Kubernetes

```bash
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
```

## 📊 Monitoring

Prometheus + Grafana deployed via Helm on Kubernetes.
