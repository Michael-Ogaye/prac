import requests

# Set up the PayPal API endpoint and headers
url = "https://api.paypal.com/v1/payments/payment"
headers = {
    "Authorization": "Bearer <your access token here>",
    "Content-Type": "application/json"
}

# Set up the payment data
payment_data = {
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"
    },
    "transactions": [
        {
            "amount": {
                "total": "10.00",
                "currency": "USD"
            }
        }
    ],
    "redirect_urls": {
        "return_url": "http://example.com/success",
        "cancel_url": "http://example.com/cancel"
    }
}

# Send the payment request to PayPal
response = requests.post(url, headers=headers, json=payment_data)

# Process the PayPal response
if response.status_code == 201:
    # Payment created successfully, extract the payment ID
    payment_id = response.json()["id"]
    print(f"Payment created successfully with ID: {payment_id}")
    # Redirect the user to PayPal to complete the payment
    approval_url = next(link["href"] for link in response.json()["links"] if link["rel"] == "approval_url")
    print(f"Please approve the payment at: {approval_url}")
else:
    # Payment creation failed, display the error message
    error_message = response.json()["message"]
    print(f"Payment creation failed: {error_message}")
