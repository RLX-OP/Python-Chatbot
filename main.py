import requests, time


def chatBot():
        name = "Enter Your name here"
        msg = input(name + ":-  ")

# API url for chat response
        url = "http://api.brainshop.ai/get?bid=169766&key=m6HzHyHVG3qvz7LO&uid="+name+"&msg="+msg+""

# Connecting to API and converting the data to JSON format.
        req = requests.get(url = url)
        data = req.json()

# Name Of JSON key that will give out a value
        response = data['cnt']

# Data responded by API if status is 200, if not then throws an error in console
        if req.status_code == 200:
                time.sleep(2)
                print("ChatBot:-  " + response)
                print("\n")
        else:
                print("An Error Occurred In API Please Restart And Try Again")
                exit()

while True:
        chatBot()
