var app = require('express')();
var http = require('http').Server(app);

app.get('/', function(req, res){
   res.sendFile('C:\Users\levip\GlenProjects\JS-Python-Server\index.html');
});

http.listen(3000, function(){
   console.log('listening on *:3000');
});