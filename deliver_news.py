#pylint: disable=E1101

from __future__ import print_function
import fetch_google_creds
import base64
from email.mime.text import MIMEText
import mimetypes


def main():
    creds = fetch_google_creds.fetch_creds()
    service = fetch_google_creds.build_service(creds)
    file = open('output.txt', mode='r')
    msg = file.read()
    message = create_message(
        "daily.news.updates.from.peter@gmail.com", "david.rolfe@pobox.com", "Hello", msg)
    send_message(service, "me", message)
    print('done')


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
    message = MIMEText(message_text)
    message['to'] = destination
    message['from'] = origin
    message['subject'] = subject
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

    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    return message


main()
