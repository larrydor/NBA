import json
import re
import statistics
import requests

print("-------------------------")
x = input("Do you want to find the best player for your team? (Type Yes or No):")
if (x == "Yes"):
    print("Great, let's do this. Here's the entire list of available players...")
else:
    print("Alright, well good luck building a championship team without us! Have a good day :-)")
    exit()
import json
import requests
import os
from dotenv import dotenv_values
from dotenv.main import load_dotenv
load_dotenv()

api = os.getenv("api")
#url = 'https://api.sportradar.us/nba/{access_level}/{version}/{language_code}/league/free_agents.{format}?api_key={your_api_key}'
#final_url = f'{url}'


#url = "https://api.sportradar.us/nba/trial/v7/en/league/free_agents.json?"
#final_url = f'{url}api_key={api}'

import http.client

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", f"/nba/trial/v7/en/league/free_agents.json?api_key={api}")

res = conn.getresponse()
data = res.read()

print(data)

y = input("Now, what position are you looking for? (Input PG, SG, SF, PF, or C):")
if (y == "PG"):
    print("Here's a list of available Point Guards:")
if (y == "SG"):
    print("Here's a list of available Shooting Guards:")
if (y == "SF"):
    print("Here's a list of available Small Forwards:")
if (y == "SG"):
    print("Here's a list of available Power Forwards:")
if (y == "C"):
    print("Here's a list of available Centers:")
