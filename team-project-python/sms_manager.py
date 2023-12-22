from twilio.rest import Client

# Move to environment variables
account_sid = "ACd04d5632398fd0dfab997a798e3070a6"
auth_token = "602431b4ae7c559d331918bc77c47d9f"
from_number = "+14082284738"

twilio_client = Client(account_sid, auth_token)

def send_message(phone_number, text):
    try:
        message = twilio_client.messages.create(
            body=text,
            from_=from_number,
            to=phone_number
        )
        print(f"Message sent to {phone_number}")

        if message.sid:
            print(f"Message '{text}' sent to phone number:'{phone_number}'")
        else:
            print(f"Failed to send message to: {phone_number}. Make sure phone number is correct.")
    #Exception code could be improved
    except Exception:
        print(f"Failed to send message to: {phone_number}. Make sure phone number is correct.")
