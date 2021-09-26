const scanner = require('sonarqube-scanner');
scanner(
  {
  serverUrl: "http://54.167.89.227/",
  //login:"admin",
  //password:"4WNxM2ReQN8r",
  options: {
    "sonar.sources": "./givekudo, ./kudos, ./users"
  },
},
() => process.exit()
);