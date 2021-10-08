from flask import Flask, request
from flask_cors import CORS
import json, random, time, sys, subprocess, os, shutil
from datetime import datetime

app = Flask(__name__)
CORS(app)

with open('validAuthTokens.txt', 'r') as f:
  validAuthTokens = json.load(f)

def generateAuthToken():
  letters_lst = ['a', 'e', 'w', 't', 'a', 'u', 'o', 'p', '2', '5', '6', '3', '8', '4']
  authTokenString = ''
  while len(authTokenString) < 10:
    authTokenString += random.choice(letters_lst)
  return authTokenString


@app.route('/')
def homepage():
  with open('homepage.html', 'r') as f:
    f_content = f.read()
    return f_content

@app.route('/passwordCheck', methods=['POST'])
def passwordAuth():
  if request.headers['DataBankAccessCode'] == 'ert56' and request.headers['Content-Type'] == 'application/json':
    if request.json['data'] == 'dataBank@Prakh0706!':
      newToken = generateAuthToken()
      validAuthTokens[datetime.now().strftime('%H:%M:%S')] = newToken
      json.dump(validAuthTokens, open('validAuthTokens.txt', 'w'))
      # print(validAuthTokens)
      return 'Authorisation successful! Temp auth token: {}'.format(newToken)
    else:
      return 'Authorisation failed!'
  else:
    return 'Authorisation failed! Incorrect data bank access code or content-type.'

@app.route('/data/<authToken>')
def showData(authToken):
  isValid = False
  print(validAuthTokens)
  for timeKey in validAuthTokens:
    if validAuthTokens[timeKey] == authToken:
      isValid = True
  if not isValid:
    return "<h1>Invalid auth token. Please obtain a new auth token by making a password check request.</h1>"
  with open('data.html', 'r') as f:
    f_content = f.read()
    return f_content

@app.route('/clearTokens/<password>')
def clearTokens(password):
  if password != "0706!":
    return "Invalid password. Clear tokens failed."
  global validAuthTokens
  validAuthTokens = {}
  print(validAuthTokens)
  with open('validAuthTokens.txt', 'w') as f:
    json.dump(validAuthTokens, f)
  return "Tokens cleared!"

@app.route('/home')
def homeJS():
  with open('home.js', 'r') as f:
    f_content = f.read()
    return f_content

@app.route('/dataJS')
def dataJS():
  with open("data.js", 'r') as f:
    f_content = f.read()
    return f_content

@app.route('/data/filenames/<authToken>')
def fileNamesAccess(authToken):
  isValid = False
  for timeKey in validAuthTokens:
    if validAuthTokens[timeKey] == authToken:
      isValid = True
  if not isValid:
    return "<h1>Invalid auth token. Please obtain a new auth token by making a password check request.</h1>"
  fileNames = []
  for _, _, files in os.walk(os.path.join(os.getcwd(), 'dataBankFiles')):
    for filename in files:
      try:
        if filename not in ['main.py', 'data.html', 'home.js', 'homepage.html', 'validAuthTokens.txt']:
          fileNames.append(filename)
        else:
          continue
      except:
        return "Error in getting filenames. Please check server status."
  return ', '.join(fileNames)

@app.route('/data/<filename>/<authToken>')
def getFileData(filename, authToken):
  isValid = False
  for timeKey in validAuthTokens:
    if validAuthTokens[timeKey] == authToken:
      isValid = True
  if not isValid:
    return "<h1>Invalid auth token. Please obtain a new auth token by making a password check request.</h1>"
  filename = filename.replace("%20", " ")
  fileData = ''
  for _, _, files in os.walk(os.path.join(os.getcwd(), 'dataBankFiles')):
    for tempFileName in files:
      try:
        if tempFileName == filename:
          with open(os.path.join(os.getcwd(), 'dataBankFiles', filename), 'r') as f:
            fileDataLinesArray = f.readlines()
            firstParaOpeningTag = "<p style=\"white-space: pre-line\">"
            fileData = firstParaOpeningTag + ''.join(fileDataLinesArray) + "</p>"
            return fileData
      except:
        return 'Error in getting file data. Please check server status'
  if fileData == '':
    return "No such filename. Please try again."
      

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, threaded=True)