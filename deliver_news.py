#pylint: disable=E1101

from __future__ import print_function
import fetch_google_creds
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


def main():
    creds = fetch_creds()
    service = build_service(creds)

def fetch_creds():
    creds = fetch_google_creds.get_authorizaton()
    return creds

def build_service(creds):
    service = fetch_google_creds.build_service(creds)
    return service

if __name__ == '__main__':
    main()
