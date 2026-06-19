# sentinel_agent.py
import boto3
import json

client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def analyze_logs(log_data):
    prompt = f"Analyze these validator logs for threats: {log_data}. Return status and action."
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "messages": [{"role": "user", "content": prompt}]
    })
    response = client.invoke_model(body=body, modelId="anthropic.claude-3-haiku-20240307-v1:0")
    return json.loads(response.get('body').read())['content'][0]['text']

logs = "Error: High latency detected. CPU 98%. Peer count dropping."
print(analyze_logs(logs))