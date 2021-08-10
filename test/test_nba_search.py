from app.nba_search import fetch_roster

def test_home():
    results = fetch_roster("Bulls")
    assert isinstance(results , list)
    player = results[0]
    assert isinstance(player, dict)
    