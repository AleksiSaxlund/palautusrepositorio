
class PlayerStats:
    def __init__(self, players):
        self.players = players.players

    def top_scorers_by_nationality(self, nationality):
        players_of_nationality = []

        for player in self.players:
            if player.nationality == nationality:
                players_of_nationality.append(player)

        players_of_nationality.sort(key=lambda player: player.goals + player.assists, reverse=True)

        return players_of_nationality