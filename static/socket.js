// socket.js
import io from 'socket.io-client';

const socket = io.connect('http://' + document.domain + ':' + location.port);

export default socket;