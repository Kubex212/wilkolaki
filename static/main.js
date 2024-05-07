var socket = io.connect('http://' + document.domain + ':' + location.port);

$('.host-join-form').on('submit', function(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Determine which button was clicked
    var submitter = event.submitter;

    // Perform different actions based on the clicked button
    if (submitter.id === 'submit1') {
        // Action for the first button
        console.log('Button 1 clicked');
        // Perform your action here
    } else if (submitter.id === 'submit2') {
        // Action for the second button
        console.log('Button 2 clicked');
        // Perform your action here
    }
});


socket.on('lobby_created', function(data) {
    alert('Lobby created: ' + data.lobby_name);
});

socket.on('lobby_exists', function(data) {
    alert('Lobby already exists: ' + data.lobby_name);
});

socket.on('player_joined', function(data) {
    alert('Player joined: ' + data.player_name);
});

socket.on('players_listed', function(data) {
    console.log('Players in lobby:', data.players);
});

socket.on('lobby_not_found', function(data) {
    alert('Lobby not found: ' + data.lobby_name);
});

socket.on('redirect_to_lobby', function(data) {
    // Perform the redirection using JavaScript
    console.log('lobby join');
    window.location.href = '/lobby/' + data.lobby_name;
});
