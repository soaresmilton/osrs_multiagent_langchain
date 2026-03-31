import requests

from app.utils.convert_date import date_to_epoch

BASE_URL = "https://templeosrs.com/api"

class TempleOsrsClient:
    def get_player_stats(self, username: str) -> dict:
        url = f"{BASE_URL}/player_stats.php"
        
        date = date_to_epoch()
        
        response = requests.get(url, params={"player":username,"date": date  ,"bosses":1})

        response.raise_for_status()

        return response.json()

    def get_player_info(self, username: str) -> dict:
        url = f"{BASE_URL}/player_info.php"
        response  = requests.get(url, params={"player":username})

        response.raise_for_status()

        return response.json()