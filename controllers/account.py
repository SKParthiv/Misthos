from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class Account:
    def __init__(self, google_user_info=None):
        self.google_user_info = google_user_info
        if google_user_info:
            self.username = google_user_info['name']
            self.email = google_user_info['email']
            self.avatar_url = google_user_info['picture']
        else:
            self.username = None
            self.email = None
            self.avatar_url = None

    def link_google_account(self):
        """Link Google account to the application."""
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', 
            scopes=['https://www.googleapis.com/auth/userinfo.profile']
        )
        credentials = flow.run_local_server(port=0)
        service = build('oauth2', 'v2', credentials=credentials)
        self.google_user_info = service.userinfo().get().execute()
        self.username = self.google_user_info['name']
        self.email = self.google_user_info['email']
        self.avatar_url = self.google_user_info['picture']
