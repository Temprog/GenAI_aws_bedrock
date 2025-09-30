import os
import json
import pymysql
import boto3

# Environment variables from Lambda configuration
RDS_HOST = os.environ['RDS_HOST']
RDS_USER = os.environ['RDS_USER']
RDS_PASSWORD = os.environ['RDS_PASSWORD']
RDS_DB = os.environ['RDS_DB']

# Database connection
connection = pymysql.connect(
    host=RDS_HOST,
    user=RDS_USER,
    password=RDS_PASSWORD,
    database=RDS_DB
)

# Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")  # replace with your region

def lambda_handler(event, context):
    body = json.loads(event['body'])
    prompt = body.get('prompt', '')

    if not prompt:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Prompt is required'})
        }

    # Titan Text Lite / Nova Lite invocation
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
    ai_response = model_response['results'][0]['outputText']  # Titan returns outputText

    # Save to RDS
    with connection.cursor() as cursor:
        sql = "INSERT INTO responses (prompt, response) VALUES (%s, %s)"
        cursor.execute(sql, (prompt, ai_response))
        connection.commit()

    return {
        'statusCode': 200,
        'body': json.dumps({'prompt': prompt, 'response': ai_response}),
        'headers': {'Content-Type': 'application/json'}
    }
