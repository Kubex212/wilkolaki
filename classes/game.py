class Player:
    def __init__(self, lobby_name, players):
        self.lobby_name = lobby_name
        self.players = players

    def __str__(self):
        """
        Returns a string representation of the Player object.
        """
        return f"Client ID: {self.client_id}, Nickname: {self.nickname}, Role: {self.role}"
