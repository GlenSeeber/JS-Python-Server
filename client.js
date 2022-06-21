// Node.js socket client script
const net = require('net');

// Connect to a server @ port 9898
const client = net.createConnection(5050, "fe80::4407:f169:6f4f:2e43%11", () => {
  console.log('CLIENT: I connected to the server.');
  client.write('CLIENT: Hello this is client!');
});

client.on('data', (data) => {
  console.log(data.toString());
  client.end();
});

client.on('end', () => {
  console.log('CLIENT: I disconnected from the server.');
});