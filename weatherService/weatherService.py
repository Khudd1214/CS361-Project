import os

homeDirectoryPath = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
weatherDict = {
    "oregon" : """Sun! Yes! To the water - oh wait, nvmd. Just started raining again. 
                        HOW? There aren't even clouds in the sky. Where is the rain coming from?""",
    "california" : """The sounds of plants and animals dying as we go 6 
                        months without rain... Ooh! Another earthquake.""",
    "washington" : "Cloudy with a chance of bear attacks",
    "new york" : "Cloudy with a chance of meatballs",
    "nevada" : "REALLY dry",
    "hawaii" : "fun in the sun. Sunshine all week long!",
    "alabama" : "REALLY dry",
    "alaska" : "The polar bears would say its warm, but...",
    "arkansas" : "The lizards are crying - it's too darn hot!",
    "arizona" : "I think I saw lucifer dancing in the grand canyon...",
    "colorado" : """Nice and chill. If I lived in arizona, 
                    I would be running for the colorado hills.""",
    "connecticut" : "If you like lightning and thunderstorms... what is wrong with you?",
    "delaware" : "Dull and Dry - just like the state.",
    "florida" : """Weather is the least of your problems - the thousands 
                    of drunk teenagers are a much bigger concern...""",
    "georgia" : "At least it has water... Just be ready to dodge the sharks.",
    "idaho" : "Get ready for ice.",
    "illinois" : """A pleasant afternoon with sunshine and a gentle breeze... 
                    oh, nevermind. Now there's another thunderstorm""",
    "indiana" : "Cold and snowy. Not much else to be said.",
    "iowa" : "Snow in the winter - and the sounds of people weeping in a humid summers.",
    "kansas" : "I would tell you... but let's be honest, its gonna change again in 5 minutes.",
    "kentucky" : "Eh. Summer hot, winter cold. Nothing exciting here.",
    "louisiana" : "REALLY dry",
    "maine" : "REALLY dry",
    "maryland" : "REALLY dry",
    "massachusetts" : "REALLY dry",
    "michigan" : "REALLY dry",
    "minnesota" : "REALLY dry",
    "mississippi" : "REALLY dry",
    "missouri" : "REALLY dry",
    "montana" : "REALLY dry",
    "nebraska" : "REALLY dry",
    "new hampshire" : "REALLY dry",
    "new jersey" : "REALLY dry",
    "new mexico" : "REALLY dry",
    "north carolina" : "REALLY dry",
    "north dakota" : "REALLY dry",
    "ohio" : "REALLY dry",
    "oklahoma" : "REALLY dry",
    "pennsylvania" : "REALLY dry",
    "rhode island" : "REALLY dry",
    "south carolina" : "REALLY dry",
    "south dakota" : "REALLY dry",
    "tennessee" : "REALLY dry",
    "texas" : "REALLY dry",
    "utah" : "REALLY dry",
    "vermont" : "REALLY dry",
    "virginia" : "REALLY dry",
    "west virginia" : "REALLY dry",
    "wisoncsin" : "REALLY dry",
    "wyoming" : "REALLY dry",
}
def formatContent():
    rawFile = open(os.path.join(homeDirectoryPath, 'weather_request.csv'))
    contents = ""
    for line in rawFile:
        for characters in line:
            if characters in [' ', '\n']:
                continue
            contents += characters.lower()
    rawFile.close()
    return contents

def readSourceFile():
    deletePreviousResponseFile()
    if os.path.exists(homeDirectoryPath + "/weather_request.csv"):
        contents = formatContent()

        input_state = contents.split(",")

        if len(input_state) != 2 or input_state[1] == "":
            err = "Invalid input parameters!"
            writeError(err)
            return err

        targetState = input_state[1]
        return targetState
    else:
        err = "Could not find request file"
        writeError(err)
        return None
        
def writeError(errorString):
    with open(os.path.join(homeDirectoryPath, 'error.csv'), 'w') as output:
        output.write(errorString)
    return
def writeData(state):
    text = weatherDict[state]
    with open(os.path.join(homeDirectoryPath, 'weather_response.csv'), 'w') as output:
        output.write(state[0].upper() + state[1::].lower() + " , " + text)
    return
def deleteSourceFile():
    if os.path.exists(homeDirectoryPath + "/weather_request.csv"):
        os.remove(homeDirectoryPath + "/weather_request.csv")
    return
def deletePreviousResponseFile():
    if os.path.exists(homeDirectoryPath + "/weather_response.csv"):
        os.remove(homeDirectoryPath + "/weather_response.csv")
    return

state = readSourceFile()
writeData(state)
deleteSourceFile()