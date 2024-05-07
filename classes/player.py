class Player:
    def __init__(self, client_id, nickname, role):
        """
        Initializes a new Player instance.

        :param client_id: Unique identifier for the client.
        :param nickname: The nickname of the player.
        :param role: The role of the player in the game.
        """
        self.client_id = client_id
        self.nickname = nickname
        self.role = role

    def __str__(self):
        """
        Returns a string representation of the Player object.
        """
        return f"Client ID: {self.client_id}, Nickname: {self.nickname}, Role: {self.role}"
