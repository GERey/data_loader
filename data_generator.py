import argparse
import requests
import json
from datetime import datetime, timezone
import random
import uuid
import time

def send_post_request(api_url, api_token, customer_id, data_warehouse):
    for _ in range(10):
        # Generate RFC 3339 timestamp
        timestamp = datetime.now(timezone.utc).isoformat()

        # Generate random billable time between 1 and 100
        billable_time = str(random.randint(1, 100))

        # Generate UUID for transaction_id
        transaction_id = str(uuid.uuid4())

        # Payload data
        payload = [
            {
                "customer_id": customer_id,
                "event_type": "compute_time",
                "timestamp": timestamp,
                "transaction_id": transaction_id,
                "properties": {
                }
            }
        ]

        # Convert payload to JSON format
        json_payload = json.dumps(payload)

        # Set headers with API token
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_token}'
        }

        # Make the POST request
        response = requests.post(api_url, data=json_payload, headers=headers)

        # Print the response
        print("Request", _ + 1, "- Response Code:", response.status_code)
        print("Response Content:", response.text)

        # Wait for one second before sending the next request
        time.sleep(1)

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Send POST requests to an API')
    parser.add_argument('--api_url', required=True, help='API endpoint URL')
    parser.add_argument('--api_token', required=True, help='API token')
    parser.add_argument('--customer_id', required=True, help='Customer ID')
    parser.add_argument('--data_warehouse', required=True, help='Data Warehouse')
    args = parser.parse_args()

    # Call the function with command line arguments
    send_post_request(args.api_url, args.api_token, args.customer_id, args.data_warehouse)
