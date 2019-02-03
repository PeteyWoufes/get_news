#pylint: disable=E1101

from __future__ import print_function
import fetch_google_creds
import base64
import json
from email.mime.text import MIMEText
import mimetypes
from datetime import date


def main():
    ''' Credential Acquisition. '''
    creds = fetch_google_creds.get_authorizaton()
    date = fetch_date()
    origin = fetch_origin()
    destination = fetch_destination()
    ''' Builds service to access Gmail API. '''
    service = fetch_google_creds.build_service(creds)
    ''' Reads from pre-formatted output file. '''
    file = open('output.txt', mode='r')
    msg = file.read()
    ''' Creates message to be sent using args origin, destiantion, subject matter and body text. '''
    message = create_message(
        origin, destination, "News for " + date, msg)
    '''
    Sends message using args service (the service that accesses the Gmail API), user_id (the email to send it from)
    and message (the message created earlier.)
    '''
    send_message(service, "me", message)


def create_message(origin, destination, subject, message_text):
    """
    Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    ''' Formatting text into a format usable for email. '''
    message = MIMEText(message_text)
    ''' Matching args with the ones provided. '''
    message['to'] = destination
    message['from'] = origin
    message['subject'] = subject
    ''' Encoding the email in a format acceptable for Gmail; this step is absolutely essential. '''
    raw = base64.urlsafe_b64encode(message.as_bytes(message))
    raw = raw.decode()
    return {'raw': raw}


def send_message(service, user_id, message):
    """
    Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    """

    ''' Sends message using Gmail API. '''
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    return message

def fetch_date():
    ''' Gets the current date and returns it. '''
    today = str(date.today())
    return today


def fetch_origin():
    ''' Reads origin from config file and returns it. '''
    with open("config.json", "r") as a:
        data = json.load(a)
    origin = data["origin"]
    return origin

def fetch_destination():
    ''' Reads destination from config file and returns it. '''
    with open("config.json", "r") as a:
        data = json.load(a)
    destination = data["destination"]
    return destination

main()
