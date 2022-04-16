from secrets import choice
import twilio
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import time
ssid = int(input('Enter Twilio SSID: '))
authcode = int(input('Enter Auth Code from Twilio: '))
number = int(input('Enter Twilio number: '))


client = Client(ssid, authcode)

def send_msg():
    to = input('Number to send: ')
    message = input('Message: ')

    client.messages.create(to=to, 
                       from_=number, 
                       body=message)

def check_msg():
    msg = request.values.get('Body', None)

    print(msg)


def logo():
    print('Github: https://github.com/thedenzellight')
    print('')
    print('Author of the script is not responsible for things you do.')
    print('')
    print(" ..^PPPPPPPPP^..                           .7JJJJJJJJJJJJ~    G@&5!.        ~Y#@G    ~?7777777777?! ")
    print(" 5&&@&&&&&&&@&#5                           7@@@@@@@@@@@@@J    G@@@@#5~.  ~YB@@@@G   :&@@@@@@@@@@@@G ")
    print("~B@@@? ....^&@@B!:                         7@@@#GGGGGGGGG7    G@@@@@@@#PB@@@@@@@G   ^@@@&BBBBBBBBBY ")
    print("@@@@P:      G@@@@!      :777777777777~     7@@@Y              G@@@@@@@@@@@@@@@@@G   ^@@@B        ")
    print("@@@@Y~!!!!!~P@@@@?      ~@&&&&&&&&&&@5     7@@@Y              G@@@BPPPPPPPPPB@@@G   ^@@@B           ")
    print("@@@@@&&&&&&&@@@@@G       .............     7@@@G777777777^    G@@@!         !@@@G   ^@@@#!!!!!!!!!~ ")
    print("@@@@7.......?@@@@G                         ~B&&&@@@@@@@@@B.   G@@@!         !@@@G   :G@@@@@@@@@@@@&^")
    print("@@@#.       :@@@@B                          .::::::::.:#@@^   G@@@!         !@@@G     ^:::::::::P@@?")
    print("###G.       :GBBB5                          :.........:#@@^   G@@@!         !@@@G    .......... 5@@?")
    print("###G.       :GBBB5                         ~@@@@@@@@@@@@@&:   B@@@!         !@@@B   .B&&&&&&&&&&@@@7")
    print(" ")
    print(' ')
    print("")
    print("1: Send SMS")
    print("|__ 2: Read SMS")
    global choice
    choice = input("Options: ")

logo()

if choice == "1":
    send_msg()
    time.sleep(2)
    logo()
elif choice == "1":
    check_msg()
    time.sleep(2)
    logo()
