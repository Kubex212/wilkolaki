from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from random import randint
from flask import session
from classes.player import Player  # Import the Player class

app = Flask(__name__)
socketio = SocketIO(app, manage_session=True)
app.secret_key = 'your_secret_key'

# In-memory storage for lobbies and players
lobbies = {}
players = {}
games = {}

def generate_unique_client_id():
    return randint(0, 1000)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    client_id = session.get('client_id')
    if client_id:
        # This is a reconnection, handle accordingly
        pass
    else:
        session['client_id'] = generate_unique_client_id() 
        pass

@socketio.on('create_lobby')
def create_lobby(data):
    lobby_name = data['lobby_name']
    if lobby_name not in lobbies:
        lobbies[lobby_name] = []
        emit('lobby_created', {'lobby_name': lobby_name})
    else:
        emit('lobby_exists', {'lobby_name': lobby_name})

@socketio.on('list_players')
def list_players(data):
    lobby_name = data['lobby_name']
    if lobby_name in lobbies:
        players_in_lobby = [player for player in players.values() if players[player] == lobby_name]
        emit('players_listed', {'players': players_in_lobby}, room=lobby_name)
    else:
        emit('lobby_not_found', {'lobby_name': lobby_name})

@socketio.on('join_lobby')
def join_lobby(data):
    lobby_name = data['lobby_name']
    player_name = data['player_name']
    if lobby_name in lobbies:
        if player_name not in players:  # Check if the player is not already in a lobby
            players[player_name] = lobby_name  # Add the player to the players dictionary
            join_room(lobby_name)
            emit('player_joined', {'player_name': player_name}, room=lobby_name)
            emit('redirect_to_lobby', {'lobby_name': lobby_name}, room=lobby_name)
            emit('update_player_list', {'lobby_name': lobby_name}, broadcast=True)
        else:
            emit('player_already_in_lobby', {'player_name': player_name})
    else:
        emit('lobby_not_found', {'lobby_name': lobby_name})


@socketio.on('leave_lobby')
def leave_lobby(data):
    player_name = data['player_name']
    lobby_name = data['lobby_name']
    if player_name in players.values() and players[player_name] == lobby_name:
        players.pop(player_name)
        leave_room(lobby_name)
        emit('player_left', {'player_name': player_name}, room=lobby_name)
        return redirect(url_for('home'))
    else:
        emit('player_not_in_lobby', {'player_name': player_name})


@app.route('/lobby/<lobby_name>')
def lobby_page(lobby_name):
    players_in_lobby = [player for player, lobby in players.items() if lobby == lobby_name]
    return render_template('lobby.html', players=players_in_lobby, lobby=lobby_name)

@app.route('/get_players_in_lobby/<lobby_name>')
def get_players_in_lobby(lobby_name):
    players_in_lobby = [player for player, lobby in players.items() if lobby == lobby_name]
    return jsonify(players=players_in_lobby)

if __name__ == "__main__":
    socketio.run(app)

@app.route('/game/<lobby_name>')
def start_game():
    werewolves = int(request.args.get('werewolves', 1))
    guardians = int(request.args.get('guardians', 1))
    villagers = int(request.args.get('villagers', 1))
    
    # Use the parameters to set up your game
    # For example, you might store these settings in a session or a database
    
    return render_template('start_game.html', werewolves=werewolves, guardians=guardians, villagers=villagers)

@app.route('/game')
def game():
    # Example array of Player objects
    players = [
        Player(client_id="1", nickname="Alice", role="Werewolf"),
        Player(client_id="2", nickname="Bob", role="Guardian"),
        Player(client_id="3", nickname="Charlie", role="Villager")
    ]
    
    return render_template('game.html', players=players)