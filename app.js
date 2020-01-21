var express = require("express");
var app = express();

app.get("/power", runPy);

var server = app.listen(3000, () => {
	var host = server.address().address;
	var port = server.address().port;
	console.log('Server running on:' + host + ':' + port)
});

function runPy(req, res){
	console.log("###############################################");
	console.log(new Date());
	console.log("###############################################");
	console.log("Processing request...");
	var PathToScript = 'check_units.py';
	var {PythonShell} = require('python-shell');
	var pyshell = new PythonShell(PathToScript);
	pyshell.on('message', function (message) {
    	console.log(message);
	console.log("Finished.");	
	console.log("###############################################");
	res.json([message]);
 	});

	pyshell.end(function (err) {
		if (err){
			throw err;
		};
 	});
}
