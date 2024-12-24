import requests
import boto3
import stripe
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Validate Google API Key
def validate_google_api_key(key):
    try:
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/json?address=New+York&key={key}"
        response = requests.get(endpoint)
        return response.status_code == 200
    except Exception:
        return False

# Validate Heroku API Key
def validate_heroku_api_key(key):
    try:
        endpoint = "https://api.heroku.com/account"
        headers = {"Authorization": f"Bearer {key}"}
        response = requests.get(endpoint, headers=headers)
        return response.status_code == 200
    except Exception:
        return False

# Validate AWS API Key
def validate_aws_access_key(access_key, secret_key):
    try:
        client = boto3.client(
            'sts',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        response = client.get_caller_identity()
        return True
    except (NoCredentialsError, PartialCredentialsError):
        return False

# Validate Twilio API Key
def validate_twilio_api_key(key):
    try:
        endpoint = "https://api.twilio.com/2010-04-01/Accounts.json"
        auth = (key, '')  # Basic Auth with API key as username
        response = requests.get(endpoint, auth=auth)
        return response.status_code == 200
    except Exception:
        return False

# Validate Stripe API Key
def validate_stripe_api_key(api_key):
    try:
        stripe.api_key = api_key
        balance = stripe.Balance.retrieve()
        return True
    except stripe.error.AuthenticationError:
        return False

# Validate Facebook Access Token
def validate_facebook_access_token(token):
    try:
        endpoint = f"https://graph.facebook.com/me?access_token={token}"
        response = requests.get(endpoint)
        return response.status_code == 200
    except Exception:
        return False

# Validate Mailgun API Key
def validate_mailgun_api_key(key):
    try:
        endpoint = "https://api.mailgun.net/v3/domains"
        auth = ('api', key)
        response = requests.get(endpoint, auth=auth)
        return response.status_code == 200
    except Exception:
        return False

# Map regex patterns to validation functions
validation_map = {
    'google_api': validate_google_api_key,
    'Heroku API KEY': validate_heroku_api_key,
    'amazon_aws_access_key_id': validate_aws_access_key,
    'twilio_api_key': validate_twilio_api_key,
    'stripe_standard_api': validate_stripe_api_key,
    'facebook_access_token': validate_facebook_access_token,
    'mailgun_api_key': validate_mailgun_api_key,
    # Add additional mappings for other keys
}

def validate_key(key_type: str, key_value: str, secret_key: str = None) -> bool:
    """Return whether a key is valid based on its type and the appropriate validation function."""
    validate_func = validation_map.get(key_type)
    if validate_func:
        if key_type == 'amazon_aws_access_key_id':
            return validate_func(key_value, secret_key)
        return validate_func(key_value)
    return False


