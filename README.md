# 🧠 AWS LLM Chatbot (Generative AI Text System)

A serverless Generative AI chatbot powered by Amazon Bedrock and deployed on AWS using Lambda, API Gateway, RDS and S3.
This project demonstrates scalable, low-latency LLM-powered text generation with a simple browser-based frontend.


# 🚀 Overview

The chatbot allows users to enter prompts via a web UI hosted on Amazon S3, which are sent to a Lambda backend through API Gateway.
The Lambda function invokes Amazon Bedrock’s Titan Text model to generate responses, which are stored in Amazon RDS for persistence.


# 🧩 Architecture Components

- Amazon Bedrock – Provides LLM inference (Titan Text Lite model)
- AWS Lambda – Handles inference requests and data persistence
- API Gateway (HTTP API) – Exposes a REST endpoint for the frontend
- Amazon RDS (MySQL) – Stores prompts and AI-generated responses
- Amazon S3 – Hosts the static frontend web interface
- IAM – Secures permissions between all services


# ⚙️ Architecture Diagram
[S3 Frontend UI] → [API Gateway] → [Lambda Function] → [Bedrock (Titan Model)]
                                                    ↳ [RDS MySQL Database]


# 🧑‍💻 Features

- LLM-Powered Chatbot – Uses Amazon Titan Text G1 Lite for natural language generation
- Fully Serverless – Built entirely with AWS managed services
- Persistent Conversations – Stores user prompts and model responses in RDS
- IAM-Secured Architecture – Follows AWS security best practices
- Low-Latency Inference – Optimized Bedrock model integration


# 🧰 Tech Stack

- Layer	Service / Tool
- Frontend	HTML, CSS, JavaScript (Static website on S3)
- Backend	AWS Lambda (Python 3.x)
- API	AWS API Gateway (HTTP API)
- Database	Amazon RDS (MySQL)
- AI Model	Amazon Bedrock – Titan Text G1 Lite
- Auth / Security	IAM Roles and Policies
