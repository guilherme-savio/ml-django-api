import json
import requests

class SpotifyAuth:
    client_id = None
    client_secret = None
    token = None
    
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
    
    
    def authenticate(self):
        try:
            auth = requests.post(
                url="https://accounts.spotify.com/api/token",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                data=f"grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_secret}",
                timeout=0.5
            )
            auth.raise_for_status()
        except requests.Timeout as e:
            return {"status": "error", "message": str(e)}
        except requests.RequestException as e:
            return {"status": "error", "message": str(e)}
        else:
            self.token = auth.json().get("access_token")