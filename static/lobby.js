var socket = io.connect('http://' + document.domain + ':' + location.port);
var _data = {};

socket.on('update_player_list', function(data) {
    // Assuming you have a function to fetch and display the player list
    fetchAndDisplayPlayerList(data.lobby_name);
    _data.lobby_name = lobby_name;
});


function fetchAndDisplayPlayerList(lobbyName) {
    // Example AJAX request to fetch player list
    $.ajax({
        url: '/get_players_in_lobby/' + lobbyName,
        success: function(data) {
            // Update the UI with the new player list
            updateUIWithPlayers(data);
        }
    });
}

function updateUIWithPlayers(data) {
    var playersList = $('#player-list'); // Assuming '#players-list' is the ID of your list element
    playersList.empty(); // Clear the existing list
    data.players.forEach((player) => playersList.append('<li>' + player + '</li>'));
    _data.players = players;
}


function leaveLobby(lobbyName) {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.emit('leave_lobby', {'lobby_name': lobbyName, 'player_name': '{{ player_name }}'});
}


document.getElementById('gameSettingsForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the default form submission
    
    var werewolves = document.getElementById('werewolves').value;
    var guardians = document.getElementById('guardians').value;
    var villagers = document.getElementById('villagers').value;
    
    // Construct the URL with query parameters
    var url = '/start_game?werewolves=' + werewolves + '&guardians=' + guardians + '&villagers=' + villagers;
    
    // Navigate to the new page
    window.location.href = url;
});
