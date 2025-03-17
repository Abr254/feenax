import base64
import requests
from datetime import datetime

def mpesa_withdrawal(amount, phone_number):
    # Safaricom API credentials (replace with your own)
    shortcode = "your_shortcode"
    lipa_na_mpesa_shortcode = "your_lipa_na_mpesa_shortcode"
    lipa_na_mpesa_shortcut_passkey = "your_lipa_na_mpesa_shortcut_passkey"
    lipa_na_mpesa_shortcode_key = "your_shortcode_key"
    
    # Define your authentication endpoint
    auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{api_key}:{api_secret}".encode()).decode('utf-8')
    }
    
    # Send an authentication request to Safaricom
    auth_response = requests.get(auth_url, headers=headers)
    if auth_response.status_code == 200:
        access_token = auth_response.json()['access_token']
        
        # Create the request body for withdrawal
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        withdrawal_url = "https://sandbox.safaricom.co.ke/mpesa/express/v1/submit"
        
        # Define the withdrawal details
        payload = {
            "Amount": amount,
            "PhoneNumber": phone_number,
            "Shortcode": lipa_na_mpesa_shortcode,
            "AccountReference": f"Account withdrawal {datetime.now().isoformat()}",
            "TransactionType": "Payment",
            "LipaNaMpesaShortcode": lipa_na_mpesa_shortcode
        }
        
        # Send the withdrawal request to M-Pesa
        response = requests.post(withdrawal_url, headers=headers, json=payload)
        if response.status_code == 200:
            return True
        else:
            print("Error with M-Pesa API", response.text)
            return False
    else:
        print("Error with authentication", auth_response.text)
        return False