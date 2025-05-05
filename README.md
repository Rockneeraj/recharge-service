# Recharge Service

## Overview
This microservice handles recharge operations by linking users to selected recharge plans. It is built using Flask and SQLite to maintain a lightweight and simple design.

## Features
- Create a recharge entry for a user with a selected plan
- View all recharge transactions

## API Endpoints

### 1. Create a Recharge
- **URL**: `/recharges`
- **Method**: `POST`
- **Request Body**:
```json
{
  "user_id": 1,
  "plan_id": 2
}
```

### 2. Get All Recharges
- **URL**: `/recharges`
- **Method**: `GET`

## Technology Stack
- Python 3.9
- Flask
- Flask-SQLAlchemy
- SQLite

## How to Run with Docker
```bash
docker build -t recharge-service:latest .
docker run -p 5002:5002 recharge-service:latest
```

## How to Deploy to Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

## Example Usage
A recharge is created by providing:
- A valid `user_id` from the user-service
- A valid `plan_id` from the plan-service

