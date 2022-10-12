import requests, os, time, sys

# Typing Effect in Console
def typing(words):
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.10)

# Settings
name = "Enter your name here"
msg = input(name + ":-  ")

# API url for chat response
url = "http://api.brainshop.ai/get?bid=169766&key=m6HzHyHVG3qvz7LO&uid="+name+"&msg="+msg+""

# Connecting to API and converting the data to JSON format.
req = requests.get(url = url)
data = req.json()

# Name Of JSON key that will give out a value
response = data['cnt']

# Data responded by API
if req.status_code == 200:
        time.sleep(1)
        typing("ChatBot:-  " + response)
        print("\n")
        os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        
                
else:
       typing("An Error Occurred In API Please Restart And Try Again")
