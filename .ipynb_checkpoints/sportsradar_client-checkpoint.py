import requests

API_KEY      = "API_KEY_HERE"  # Replace with your actual API ke
ACCESS_LEVEL = "trial"
LANGUAGE     = "en"
FORMAT       = "json"
SEASON_YEAR  = "2023"
SEASON_TYPE  = "REG"

SEASON_SCHEDULE_URL = (
    "https://api.sportradar.com/ncaafb/{access_level}/v7/{language}/games/"
    "{season_year}/{season_type}/schedule.{format}"
)
GAME_STATS_URL = (
    "https://api.sportradar.com/ncaafb/{access_level}/v7/{language}/games/"
    "{game_id}/statistics.{format}"
)

def get_season_game_ids(api_key, access_level, language, season_year, season_type, fmt):
    """
    Returns a flat list of every game GUID in the given season.
    """
    url = SEASON_SCHEDULE_URL.format(
        access_level=access_level,
        language=language,
        season_year=season_year,
        season_type=season_type,
        format=fmt,
    )
    resp = requests.get(url, params={"api_key": api_key})
    resp.raise_for_status()
    data = resp.json()
    game_ids = []
    for week in data.get("weeks", []):
        for game in week.get("games", []):
            game_ids.append(game["id"])
    return game_ids

def get_game_statistics(api_key, access_level, language, game_id, fmt):
    """
    Fetch statistics for one game. Raises HTTPError on non-200.
    """
    url = GAME_STATS_URL.format(
        access_level=access_level,
        language=language,
        game_id=game_id,
        format=fmt,
    )
    resp = requests.get(url, params={"api_key": api_key})
    resp.raise_for_status()
    return resp.json()