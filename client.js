const b = require("buffer");
const io = require("socket.io-client");

var net = require('net');

const HEADER = 64;
const PORT = 5050;
const FORMAT = 'utf-8';
const SERVER = "172.16.226.95";

var client = new net.Socket();



socket = io.connect(`${SERVER}:${PORT}`);

const byteSize = str => new b.Blob([str]).size;

let msg = "nerdJUICESFEF";
msg = Buffer.from(msg, 'utf-8').toString();
console.log(msg);

let myHeader = byteSize(msg);

console.log(myHeader);

while(true){
  if(byteSize(myHeader) == HEADER){
    break;
  }
  if(myHeader > HEADER){
    console.log("Error");
    break;
  }
  myHeader += " ";
}

// socket.send(myHeader);
// socket.send(msg);

client.connect(PORT, SERVER, function() {
  console.log('Connected');
  console.log(`this is mh "${myHeader}"`);
  client.write(myHeader);
  console.log(`this is m ${msg}`);
  client.write(msg);
});

client.on('data', function(data) {
  console.log('Received: ' + data);
  client.destroy(); // kill client after server's response
});

socket.disconnect()