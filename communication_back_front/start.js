// initialize variables
var spawn = require('child_process').spawn,
py    = spawn('python3', ['filename.py']),
data_list = [1,2,3,4,5,6,7,8,9],
data_from_py = '';
var array

commandDict = {'type':'timeLatLon'}

/*We have to stringify the data first otherwise our python process wont recognize it*/
py.stdin.write(JSON.stringify(commandDict));

// recive data from python as variable data
py.stdout.on('data', function(data){
  data_from_py = JSON.parse(data);
});

/*Once the stream is done (on 'end') we want to simply log the received data to the console.*/
py.stdout.on('end', function(){
  for (i = 0; i < data_from_py.length ; i++) {
    console.log(data_from_py[i])
}

});

py.stdin.end();
