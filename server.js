const express = require("express");
const app = express();
const portNumber = 4379;

const bodyParser = require("body-parser");
const fs = require("fs");
const { spawnSync } = require("child_process");
const { response } = require("express");

app.listen(portNumber);
app.use(bodyParser.urlencoded({ extended: true }));

/*
-------Main-------
*/

app.get("/", function (request, response) {
  response.sendFile(__dirname + "/team503weatherapp.html");
});

app.post("/", function (req, res) {
  const userState = req.body.userState;
  const dataType = req.body.dataType;
  let response = populateData(userState, dataType);
  res.send(response);
});

console.log("Listening on port " + portNumber);

/*
-------Functions-------
*/

function populateData(userState, dataType) {
  bearAttackService = "bearAttackService/attack_service.py";
  bearAttackResponse = "bearAttackService/attack_response.csv";
  weatherService = "weatherService/weatherService.py";
  weatherResponse = "weatherService/weather_response.csv";
  userState = "State , " + userState;
  let result = null;
  if (dataType === "bearData") {
    writeDoc("bearAttackService/attack_request.csv", userState);
    callScript(bearAttackService);
    result = readResponse(bearAttackResponse);
    removeFile(bearAttackResponse);
  } else {
    writeDoc("weatherService/weather_request.csv", userState);
    callScript(weatherService);
    result = readResponse(weatherResponse);
    removeFile(weatherResponse);
  }
  return result;
}

function writeDoc(path, data) {
  fs.writeFileSync(path, data, "utf8");
}

function readResponse(responseAddress) {
  let result = fs.readFileSync(responseAddress, "utf8");
  return result;
}

function removeFile(fileAddress) {
  fs.rmSync(fileAddress);
}

function callScript(script) {
  const pythonScript = spawnSync("python3", [script]);
}
