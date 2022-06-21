// Node.js socket client script
const net = require('net');

import { io } from "socket.io-client";


const socket = io("172.91.45.85", {

});
socket.on("connect", () =>{
  socket.on("recieve_msg", () =>{})

  socket.emit("send_msg", { a: "b", c: [] });
});