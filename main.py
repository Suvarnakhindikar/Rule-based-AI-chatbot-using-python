# Rule Based AI ChatBot using Python

import datetime
import time 

# Greeting Message
name = input("Enter your name:")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour < 11:
   print("Good Morning", name)
elif 11 <= presentHour < 17:
   print("Good Afternoon", name)   
elif 17 <= presentHour < 20:
   print("Good Evening", name)


print("Namaste! Welcome to your Personal ChatBot")
print("You can ask me basic quetions,type 'bye' to exit from the bot ")

# ChatBot Memory Creation [ Dictionary of Responses ]
responses = {
  "hello":"Hi,welcome.How can i help you ??",
  "how are you":"I am very fine. Thank you",
  "who are you":"I am your Smart AI chatbot",
  "motivate me": " Keep going.Every Bug of your project makes you a better developer",
  "happy":"Great to hear that",
  "What is the Function":"Functions are the "
}

# Methods /Function to get response of Chatbot

def getResponsofBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
       if eachkey in userQuestion:
        return responses[eachkey]
      
    return "I am not able to tell that yet. I'll learn soon"


# Take user input 

while True:
    userInput = input("please ask your question:")
    reply= getResponsofBot(userInput)
    print(" Bot Response :" , reply)

    if "bye" in userInput.lower():
      break
print("Thank you for using the ChatBot. Have a nice day!")