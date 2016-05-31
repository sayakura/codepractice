var express = require("express");
var app = express();
var path = require("path");

app.use(express.static('client'));

app.get('/',function(req, res){
	res.sendFile(path.join(__dirname+"/index.html"));
});

app.post('/',function(req, res){
	res.send("HEllo world");
});

app.get('ajax', function (req, res) {
  res.send('ajax.txt');
});


app.listen(3000, function(){
	console.log("Server listen at port 3000...");
});