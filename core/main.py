from twilio.rest import Client
from core.config import settings

# Your Account SID and Auth Token from console.twilio.com
ACCOUNT_SID = "ACa96434d632e5d56f486a6504878898a9"
AUTH_TOKEN  = settings.AUTH_TOKEN

client = Client(ACCOUNT_SID, AUTH_TOKEN)


if __name__ == "__main__":
    message = client.messages.create(
        to=f"whatsapp:{settings.NUMBER_TO}",
        from_=f"whatsapp:{settings.NUMBER_FROM}",
        body="Hello from Python!")

    print(message.sid)
