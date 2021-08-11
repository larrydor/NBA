from app.nba_search import fetch_roster

def test_home():
    results = fetch_roster("Bulls")
    assert isinstance(results , list)
    player = results[0]
    assert isinstance(player, dict)
    assert list(player.keys()) == ["name", "general_position", "position", "experience", "college", "height", "weight", "birthdate", "birthplace"]
# source: Professor Rossetti Class 11 and https://github.com/s2t2/daily-briefings-py/blob/main/test/weather_test.py
