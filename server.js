const express = require("express")
const app = express()
const portNumber = 4379

const bodyParser = require("body-parser")
const fs = require("fs")
const {spawn} = require("child_process")

app.listen(portNumber)
app.use(bodyParser.urlencoded({extended: true}))

function callScript(state) {
  const pythonScript = spawn('python3', ["bearAttackService/attack_service.py"])
  pythonScript.stdout.on('data', (data) => {
    console.log("Sucess! ")
    console.log(`stdout: ${data}`)
  })
  pythonScript.stderr.on('data', (data) => {
    console.log("There was a problem... ")
    console.error(`stderr: ${data}`)
  })
  pythonScript.on('close', (code) => {
    function readResponse () {
      fs.readFile('bearAttackService/attack_response.csv', 'utf8', function(err, data) {
        if (err) {
          console.log(err)
        } else {
          console.log(data)
        }
      })
    }
    console.log(`script exited with code ${code}`)
    readResponse()
  })
}

app.get("/", function(request, response){
  response.sendFile(__dirname + "/team503weatherapp.html")
})
app.post("/", function(req, res){
  const userState = req.body.userState
  res.send(userState)

  //create attack_request.csv file
  const attack_request_raw = "State , " + userState
  fs.writeFile('bearAttackService/attack_request.csv', attack_request_raw, 'utf8', function(err){
    if (err) return console.log(err)
  })

  //run attack_service.py
  callScript(userState)
  //send response
})
console.log("Listening on port " + portNumber)
