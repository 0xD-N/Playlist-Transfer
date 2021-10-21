import os
import os
import json
from google.auth.transport import Response

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

class client:
    
    scopes = []
    def __init__(self):
        
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        self.scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    
    #returns dictionary
    def getPlaylists(self):
        
        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, self.scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        
        request = youtube.playlists().list(
            part="snippet,contentDetails",
            maxResults=50,
            mine=True
        )
        response: dict = request.execute()
        
        return response
    
    #returns dictionary
    def getPlaylist(self, name) -> dict:
        
        
            r = json.dumps(self.getPlaylists())
            
            data = json.loads(r)
            
            user_playlist: dict = None
            for playlist in data["items"]:
                if(playlist["snippet"]["title"].lower() == name.lower()):
                    user_playlist = playlist
            
            if(user_playlist):
                r = json.dumps(user_playlist)
                return json.loads(r)
            
            else:
                print("I couldn't find the playlist")

    