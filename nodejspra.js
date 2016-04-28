var path = require("path");

var hello = "Hello World";

console.log(`Dont even say ${hello} !!!`);

console.log(`Dirname: ${__dirname}`);

console.log(`Filename: ${__filename}`);

console.log(`Rock on world from ${path.basename(__filename)}`);

console.log("__________________________________________\n\n");

function grab(flag){
	var index = process.argv.indexOf(flag);
	return (index === -1) ? null : process.argv[index+1]; 
}

var greeting = grab('--greeting');
var user = grab('--user');


if(!user || !greeting){
	console.log("U screwed it all : )");
}else{
	console.log(`Welcome ${user}, ${greeting}`);
}

var questions = [
	"question1",
	"question2",
	"question3"
];

var answer = [];
function ask(i){
	process.stdout.write(`\n${questions[i]}`);
	process.stdout.write(" > ");
}

process.stdin.on("data", function(data){
	answer.push(data.toString().trim());
	if(answer.length === 6){
		process.exit();
	}
	for(var a = 0 ; a < answer.length; a ++){
		process.stdout.write(answer[a]);
	}
});

process.on('exit', function(){
	process.stdout.write("That's bullllllshit!");
})



ask(0);

var timeout = 15000;
var waitInterval = 100;
var currentTime = 0;

process.stdout.write(`Can you please wait ${timeout/1000} second?\n`);

function printPercentage(time){
	process.stdout.clearLine();
	process.stdout.cursorTo(0);
	process.stdout.write(`waiting.... ${time} %`);
}

var interval = setInterval(function(){
	currentTime+= waitInterval;
	printPercentage(Math.floor((currentTime/timeout) * 100));

},waitInterval);

setTimeout(function() {
	console.log("\nGameOVER");
	clearInterval(interval);
}, timeout);

