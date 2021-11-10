function displayWeather() {
  ///create/target elements - variable initialization
  let targetDiv = document.getElementsByClassName("weatherDataBox")[0]
  let newContent = document.createTextNode("This is the weather report!")
  let newButton = document.createElement("input")
  let lineBreak = document.createElement("br")

  ///newButton properties
  newButton.type = "Submit"
  newButton.value = "Would you like to continue and get your Bear Risk Assessment Report?"
  newButton.size = "50"
  newButton.addEventListener("click", function (event) {
    event.preventDefault()
    displayBearRisk()
  }
  )

  ///appendElements
  targetDiv.appendChild(newContent)
  targetDiv.appendChild(lineBreak)
  targetDiv.appendChild(newButton)
}

function displayBearRisk() {
  let targetDiv = document.getElementsByClassName("bearAttackBox")[0]
  let userState = document.getElementById("userState").value
  let newContent = document.createTextNode("" + userState)
  //create XML request to go to server.js with bear_attack_request
  //receive response from server.js
  targetDiv.appendChild(newContent)
}

document.getElementById("weatherSubmitButton").addEventListener("click", function (event) {
  event.preventDefault()
  displayWeather()
}
)
document.getElementById("bearAttackSubmitButton1").addEventListener("click", function(event) {
  event.preventDefault()
  displayBearRisk()
}
)
