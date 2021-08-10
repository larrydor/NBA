import os
import csv

import ast
import http.client
import pandas as pd
from dotenv.main import load_dotenv
from pprint import pprint
load_dotenv()

API = os.getenv("api_key")

if __name__ == "__main__":

    print("Welcome to the GM Assist: NBA Free Agent Tracker Tool!")
    print("-------------------------")
    print("NBA Teams: Lakers, Warriors, Celtics, Knicks, Suns, Bucks, Nets, Raptors, 76ers, Mavericks, Clippers, Spurs, Jazz, Heat, Wizards, Trail Blazers, Hawks, Kings, Rockets, Hornets, Nuggets, Cavaliers, Pelicans, Pacers, Timberwolves, Grizzlies, Magic, Pistons, Bulls")
    print("-------------------------")
    desired_team = input("Which team do you want to be the GM for? ")
    print(f"Great, you are the GM of the {desired_team}. Here's your current roster:")
    if (desired_team == "Lakers"):
        team_id = '583ecae2-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Warriors"):
        team_id = '583ec825-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Celtics"):
        team_id = '583eccfa-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Knicks"):
        team_id = '583ec70e-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Suns"):
        team_id = '583ecfa8-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Bucks"):
        team_id = '583ecefd-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Nets"):
        team_id = '583ec9d6-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Raptors"):
        team_id = '583ecda6-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "76ers"):
        team_id = '583ec87d-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Mavericks"):
        team_id = '583ecf50-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Clippers"):
        team_id = '583ecdfb-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Spurs"):
        team_id = '583ecd4f-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Jazz"):
        team_id = '583ece50-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Heat"):
        team_id = '583ecea6-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Wizards"):
        team_id = '583ec8d4-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Trail Blazers"):
        team_id = '583ed056-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Hawks"):
        team_id = '583ecb8f-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Kings"):
        team_id = '583ed0ac-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Rockets"):
        team_id = '583ecb3a-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Hornets"):
        team_id = '583ec97e-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Nuggets"):
        team_id = '583ed102-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Cavaliers"):
        team_id = '583ec773-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Thunder"):
        team_id = '583ecfff-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Pelicans"):
        team_id = '583ecc9a-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Pacers"):
        team_id = '583ec7cd-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Timberwolves"):
        team_id = '583eca2f-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Grizzlies"):
        team_id = '583eca88-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Magic"):
        team_id = '583ed157-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Pistons"):
        team_id = '583ec928-fb46-11e1-82cb-f4ce4684ea4c'
    if (desired_team == "Bulls"):
        team_id = '583ec5fd-fb46-11e1-82cb-f4ce4684ea4c'
    else:
        print("Team not found...")

    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", f"/nba/trial/v7/en/teams/{team_id}/profile.json?api_key={API}")
    res_nba_teams = conn.getresponse()
    nba_teams_data = res_nba_teams.read()
    nba_teams_dict_str = nba_teams_data.decode("UTF-8")
    nba_teams_datas = ast.literal_eval(nba_teams_dict_str)
    team_players = nba_teams_datas["players"]

    clean_team_players = []
    for item in team_players:
        clean_team_player = {}

        try:
            clean_team_player["name"] = item["full_name"]
        except KeyError:
            clean_team_player["name"] = "N/A"
        try:
            clean_team_player["general_position"] = item["position"]
        except KeyError:
            clean_team_player["general_position"] = "N/A"
        try:
            clean_team_player["position"] = item["primary_position"]
        except KeyError:
            clean_team_player["position"] = "N/A"
        try:
            clean_team_player["experience"] = item["experience"]
        except KeyError:
            clean_team_player["experience"] = 0
        try:
            clean_team_player["college"] = item["college"]
        except KeyError:
            clean_team_player["college"] = "N/A"
        try:
            clean_team_player["height"] = float(item["height"])
        except KeyError:
            clean_team_player["height"] = "N/A"
        try:
            clean_team_player["weight"] = float(item["weight"])
        except KeyError:
            clean_team_player["height"] = "N/A"
        try:
            clean_team_player["birthdate"] = item["birthdate"]
        except KeyError:
            clean_team_player["birthdate"] = "N/A"
        try:
            clean_team_player["birthplace"] = item["birth_place"]
        except KeyError:
            clean_team_player["birthplace"] = "N/A"
        clean_team_players.append(clean_team_player)
    #source: Professor Rossetti in class 10 explained how to convert our orginal data to a clean list

    for item in clean_team_players:
        try:
            print(f'Player Name: {item["name"]}, Position: ({item["general_position"]}), Primary Position: ({item["position"]}), Years of Experience: ({item["experience"]}), College: {item["college"]}, Height (inches): ({item["height"]}), Weight (lbs): ({item["weight"]}), Birthdate: ({item["birthdate"]}), Place of Birth: {item["birthplace"]}')
        except KeyError as e:
            pass

    print("-------------------------")
    x = input("Do you want to find the best free agent for your team? (Type Yes or No): ")
    if x.upper() == "YES":
        print("Great, let's do this. Here's the entire list of available players...")
    else:
        print("Alright, well good luck building a championship team without us! Have a good day :-)")
        exit()

    conn = http.client.HTTPSConnection("api.sportradar.us")
    conn.request("GET", f"/nba/trial/v7/en/league/free_agents.json?api_key={API}")
    res = conn.getresponse()
    data = res.read()
    dict_str = data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    free_agents = mydata["free_agents"]

    clean_players = []
    for player in free_agents:
        clean_player = {}

        try:
            clean_player["name"] = player["full_name"]
        except KeyError:
            clean_player["name"] = "N/A"
        try:
            clean_player["general_position"] = player["position"]
        except KeyError:
            clean_player["general_position"] = "N/A"
        try:
            clean_player["position"] = player["primary_position"]
        except KeyError:
            clean_player["position"] = "N/A"
        try:
            clean_player["experience"] = player["experience"]
        except KeyError:
            clean_player["experience"] = 0
        try:
            clean_player["college"] = player["college"]
        except KeyError:
            clean_player["college"] = "N/A"
        try:
            clean_player["height"] = float(player["height"])
        except KeyError:
            clean_player["height"] = "N/A"
        try:
            clean_player["weight"] = float(player["weight"])
        except KeyError:
            clean_player["height"] = "N/A"
        try:
            clean_player["birthdate"] = player["birthdate"]
        except KeyError:
            clean_player["birthdate"] = "N/A"
        try:
            clean_player["birthplace"] = player["birth_place"]
        except KeyError:
            clean_player["birthplace"] = "N/A"
        clean_players.append(clean_player)
    #source: Professor Rossetti in class 10 explained how to convert our orginal data to a clean list

    for player in clean_players:
        try:
            print(f'Player Name: {player["name"]}, Position: ({player["general_position"]}), Primary Position: ({player["position"]}), Years of Experience: ({player["experience"]}), College: {player["college"]}, Height (inches): ({player["height"]}), Weight (lbs): ({player["weight"]}), Birthdate: ({player["birthdate"]}), Place of Birth: {player["birthplace"]}')
        except KeyError as e:
            pass

    y = input("Now, what position are you looking for? (Input PG, SG, SF, PF, or C): ")
    z = input("How many years of professional experience are you looking for?: ")

    if (y == "PG"):
        print(f"Here's a list of available Point Guards: with {z} years of experience:")
    if (y == "SG"):
        print(f"Here's a list of available Shooting Guards: with {z} years of experience:")
    if (y == "SF"):
        print(f"Here's a list of available Small Forwards: with {z} years of experience:")
    if (y == "SG"):
        print(f"Here's a list of available Power Forwards: with {z} years of experience:")
    if (y == "C"):
        print(f"Here's a list of available Centers: with {z} years of experience:")
    if y != "PG" or "SG" or "SF" or "SG" or "C":
        print("Sorry you have entered an invalid position. (Input PG, SG, SF, PF, or C): ")
    else:
        print(f"Sorry there are currently no {y} with {z} years of experience are available.")

    query_list = []
    for player in clean_players:
        if player["position"] == y and player["experience"] == z:
            print(f'Player Name: {player["name"]}, Position: ({player["general_position"]}), Primary Position: ({player["position"]}), Years of Experience: ({player["experience"]}), College: {player["college"]}, Height (inches): ({player["height"]}), Weight (lbs): ({player["weight"]}), Birthdate: ({player["birthdate"]}), Place of Birth: {player["birthplace"]}')
            query_list.append(player)
        if KeyError:    
            pass        
    #source: https://realpython.com/python-keyerror/
    #source: https://stackoverflow.com/questions/15653966/ignore-keyerror-and-continue-program
    #source: https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make

    to_csv = input("Would you like a copy of this information in CSV? (Type Yes or No): ")
    if to_csv.upper() == "YES":
        #csv_file_path = "data/free_agents.csv" # source: https://www.youtube.com/watch?v=UXAVOP1oCog&t=847s
        csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "free_agents.csv") # source: https://www.youtube.com/watch?v=UXAVOP1oCog&t=847s
        print(f"Writing data to: {csv_file_path}")
        csv_headers = ["name", "general_position", "position", "experience", "college", "height", "weight", "birthdate", "birthplace"]
        with open(csv_file_path, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()
            for player in query_list:
                writer.writerow({
                        "name": player["name"],
                        "general_position": player["general_position"],
                        "position": player["position"],
                        "experience": player["experience"],
                        "college": player["college"],
                        "height": player["height"],
                        "weight": player["weight"],
                        "birthdate": player["birthdate"],
                        "birthplace": player["birthplace"],
                            })
    #source: csv related: https://github.com/Fleshner/robo-advisor/blob/main/app/robo_advisor.py
    #source: https://github.com/s2t2/robo-advisor-screencast/blob/v3-testing/app/robo_advisor.py
    else:
        print("Thank you for using our application!")
        print("Have a great day!")
        exit()