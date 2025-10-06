## 🧠 AWS LLM Chatbot (Generative AI Text System)

A serverless Generative AI chatbot powered by Amazon Bedrock and deployed on AWS using Lambda, API Gateway, RDS and S3.
This project demonstrates scalable, low-latency LLM-powered text generation with a simple browser-based frontend.


## 🚀 Overview

The chatbot allows users to enter prompts via a web UI hosted on Amazon S3, which are sent to a Lambda backend through API Gateway.
The Lambda function invokes Amazon Bedrock’s Titan Text model to generate responses, which are stored in Amazon RDS for persistence.


## 🧩 Architecture Components

- Amazon Bedrock – Provides LLM inference (Titan Text Lite model)
- AWS Lambda – Handles inference requests and data persistence
- API Gateway (HTTP API) – Exposes a REST endpoint for the frontend
- Amazon RDS (MySQL) – Stores prompts and AI-generated responses
- Amazon S3 – Hosts the static frontend web interface
- IAM – Secures permissions between all services


## ⚙️ Architecture Diagram
[S3 Frontend UI] → [API Gateway] → [Lambda Function] → [Bedrock (Titan Model)]
                                                    ↳ [RDS MySQL Database]

## 💬 Chat Deployment & Frontend

Backend: AWS Lambda function integrated with Amazon Bedrock via API Gateway for real-time text generation and RDS storage.
Frontend: Static web interface hosted on Amazon S3, allowing users to interact with the chatbot in real time through a clean browser UI.

🔗 [Live Chat Demo](http://genai-webui.com.s3-website.eu-north-1.amazonaws.com/)


## 🧑‍💻 Features

- LLM-Powered Chatbot – Uses Amazon Titan Text G1 Lite for natural language generation
- Fully Serverless – Built entirely with AWS managed services
- Persistent Conversations – Stores user prompts and model responses in RDS
- IAM-Secured Architecture – Follows AWS security best practices
- Low-Latency Inference – Optimized Bedrock model integration


## 🧰 Tech Stack

### Layer	Service / (Tool)
- Frontend	HTML, CSS, JavaScript (Static website on S3)
- Backend	AWS Lambda (Python 3.x)
- API	AWS API Gateway (HTTP API)
- Database	Amazon RDS (MySQL)
- AI Model	Amazon Bedrock – Titan Text G1 Lite
- Auth / Security	IAM Roles and Policies

## 🧾 Lambda Function (Core Logic)
```bash
response = bedrock.invoke_model(
    modelId="amazon.titan-text-lite-v1",
    body=json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 512,
            "temperature": 0.7,
            "topP": 0.9
        }
    })
)
model_response = json.loads(response['body'].read())
ai_response = model_response['results'][0]['outputText']
```


## 🌐 Frontend

- A lightweight HTML + JS interface hosted on Amazon S3 (Static Website Hosting)
- Uses the API Gateway Invoke URL to send user prompts to Lambda
- Displays model-generated responses dynamically


## 🔧 Setup Instructions

### Deploy Lambda Function
- Create a Lambda function in AWS
- Attach IAM policies for Bedrock, RDS, and CloudWatch
- Upload your function code and dependencies

### Set Up Amazon RDS
- Create a MySQL instance
- Create a table:

```bash
CREATE TABLE responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prompt TEXT,
    response TEXT
);
```

### Create API Gateway
- Create an HTTP API
- Add route: POST /genai
- Integrate with Lambda function
- Enable CORS for your S3 frontend domain

### Host Frontend on S3
- Upload index.html, style.css, and script.js
- Enable Static Website Hosting
- Allow public read access

### Test the Chatbot
- Visit your S3 website URL
- Type a prompt and submit
- The AI-generated response will appear instantly and be logged to RDS


## 📈 Example Output

- Prompt:
List the best spas in the UK.

- Response:
The Spa at The Grove
The Gainsborough Bath Spa
The Spa at The Lanesborough
The Spa at The Corinthia London
The Spa at The Waldorf Hilton


## 🧩 Future Improvements

- Add support for multi-turn chat sessions
- Integrate with Claude 3.7 Sonnet or Amazon Nova for richer responses
- Add user authentication (Cognito + SAML)
- Implement a React-based frontend with enhanced UX


# 📜 License
This project is released under the MIT License.
