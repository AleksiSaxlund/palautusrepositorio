import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        self.players = self.get_players(response)

    def get_players(self, response):
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        
        return players