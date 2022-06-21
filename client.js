const b = require("buffer");
const io = require("socket.io-client");

const HEADER = 64;
const PORT = 5050;
const FORMAT = 'utf-8';
const SERVER = "172.16.225.152";

socket = io.connect(`${SERVER}:${PORT}`);

const byteSize = str => new b.Blob([str]).size;

let msg = "nerdjuice";
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

socket.send(myHeader);
socket.send(msg);


socket.disconnect()