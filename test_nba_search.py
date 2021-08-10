import requests
import os
from dotenv.main import load_dotenv
import http.client
load_dotenv()
API = os.getenv("api_key")

def test_home():
    "GET request to url returns a 200"
    url = "api.sportradar.us"
    resp = requests.get(url)
    assert resp.status_code == 200

#def test_http_to_https_redirect():
#    "HTTP requests should be redirected to HTTPS"
#    conn = http.client.HTTPSConnection("api.sportradar.us")
#    resp = conn.request("GET", f"/nba/trial/v7/en/teams/583ecae2-fb46-11e1-82cb-f4ce4684ea4c/profile.json?api_key={API}")
#    #assert resp.url == 'api.sportradar.us'
#    assert resp.history[0].status_code == 301

#source: https://gist.github.com/smajda/005f34e88ffa998e02dd