import datetime

class PlayerStats:
    def __init__(self, reader):
        self._reader = reader


    def _check_finnish(self, player):
        if player.nationality == "FIN":
            return True
        return False
    
    def get_top_fin_scorers(self):
        players = self._reader.get_players()

        finplayers = list(filter(self._check_finnish, players))

        time = datetime.datetime.now()

        print(f"Players from FIN {time}")

        for player in finplayers:
            print(player)

