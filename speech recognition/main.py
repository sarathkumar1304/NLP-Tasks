#import necessary libraries

import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

#Assinging a variable for text to speech

engine=pyttsx3.init()

#defing a function to speak

def talk(text):
    engine.say(text)
    engine.runAndWait()

#defining a function to call

def start():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listennig.... ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            r1=str(text.lower())
            return r1
        except:
            print("Sorry could not recognize what you said")
            start()

#defing to get details of the customers
def details():

    print("Kindly say your details")
    talk("Kindly say your details")

    print("please say your sweet name")
    talk("please say your sweet name")

    name1=start()
    print("Say your phone number")
    talk("say your phone number")

    ph_no=start()
    print("say your  current location")
    talk("say your current location ")

    address=start()
    print('Say your id type')
    talk("say your id type")

    id_type=start()
    print("say your id number")
    talk("say your id number")

    id_no=start()
    print("what type of room do you want book like single bedroom or double bedroom ")
    talk("what type of room do you want book like single bedroom or double bedroom ")

    room_type=start()
    print("say your arrival date like 13 april 2022")
    talk("say your arrival date like 13 april 2022")

    arr_date=start()
    print("Say your depature date like 15 april 2022" )
    talk("Say your depature date like 15 april 2022")

    dep_date=start()
    talk("thank you for room booking welcome back")
    print("Thank you for room booking Welcome back.. !!")

    with open ("info.txt",'a+') as f:
        f.write(f"---------------- Details of {name} -------------------------\n")
        f.write(f"name          : {name1}\n")
        f.write(f"age           : {age}\n")
        f.write(f"ph_no         : {ph_no}\n")
        f.write(f"address       : {address}\n")
        f.write(f"id_type       : {id_type}\n")
        f.write(f"id_no         : {id_no}\n")
        f.write(f"room_type     : {room_type}\n")
        f.write(f"arrival_date  : {arr_date}\n")
        f.write(f"depature_date : {dep_date}\n")
        f.write("--------------------------------------------------------------")
#To check the eligibility to book  room

print("Hi Grandridge 5 star hotel heartly welcome's you ")
talk("Hi Grandridge 5 star hotel heartly welcome's you")

print("please Enter your Name")
talk("please Enter your name")

name=input("Enter Name :")
talk(f"Hi,{name} Welcome,please enter age to check eligibility")
print(f"Hi,{name} Welcome,please enter age to check eligibility")

age=int(input("Enter Age :"))

if age >=18:
    talk(f"congratulations {name} you are eligible for room booking")
    print(f"congratulation {name} you are eligible for room booking")
    details()
else:
    talk(f"Sorry {name} you are not eligible for room booking")
    print(f"Sorry {name} you are not eligible for room booking")
