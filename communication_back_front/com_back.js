// node start.js

// initialize variables
function new_request(command){
  var spawn = require('child_process').spawn,

  // start python process
  py    = spawn('python3', ['com_front.py']),
  data_from_py = [];

  //write to python
  command_msg = {'type':command}
  py.stdin.write(JSON.stringify(command_msg));

  // recive data from python as variable data_from_py
  py.stdout.on('data', function(data){
    data_from_py = JSON.parse(data);
  });

  /*Once the stream is done (on 'end') we want to simply log the received data to the console.*/
  py.stdout.on('end', function(){
    for (var i = 0; i < data_from_py['country'].length ; i++) {
      console.log(data_from_py['country'][i],data_from_py['lat'][i],data_from_py['lon'][i] )
    }
  });

  py.stdin.end();
}

new_request('CountryLatLon');
