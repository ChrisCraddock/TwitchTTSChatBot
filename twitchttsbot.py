# Config portion
import socket
import time
import re
import pyttsx3
#import soundfx  <-- for use with soundfx module, uncomment if used

'''Change lines 115,117,121 with your name or bot name, 148-152 to your bots name 
   (leave the ':' where they are, just put in YOUR bots name)'''
'''Edit 83-105 if you want to use sound effects and download the soundfx module'''
'''Check line 151, take out if not interested'''

HOST = "irc.chat.twitch.tv"  # the twitch irc server
PORT = 6667  # always use port 6667
NICK = ""  # twitch bot username, lowercase
PASS = ""  # your twitch OAuth token
CHAN = ""  # the channel you want to join 

# Message Rate
RATE = (20 / 30)  # messages per second

#BANN HAMMER
PATT = [
    r"swear",
    # ...
    r"some_pattern"
    ]

# bot.py portion
# Network functions go here

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))





def chat(sock, msg):
    '''
    Send a chat message to the server.
    sock -- the socket over which to send the message
    msg -- the message to be sent
    '''
    sock.send("PRIVMSG #{} :{}\r\n".format(CHAN, msg).encode("utf-8"))


def ban(sock, user):
    '''
    Ban a user from the current channel.
    sock -- the socket over which to send the ban command
    user -- the user to be banned
    '''
    chat(sock, ".ban {}".format(user))


def timeout(sock, user, secs=10):
    '''
    Time out a user for a set period of time
    sock -- the socket over which to send the timeout command
    user -- the user to be timed out
    secs -- the length of the timeout in seconds (default 600)
    '''
    chat(sock, ".timeout {}".format(user, secs))

# Make sure you prefix the quotes with an 'r'
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
chat(s,"Change ma value you bum, line 71") #Enter chat message for when connecting

while True:
    response = s.recv(1024).decode("utf-8")
    print(response)
    if response == "PING :tmi.twitch.tv\r\n":
       s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
       print("Pong")
    else:
        username = re.search(r"\w+", response).group(0)  # return the entire match
        message = CHAT_MSG.sub("", response)
        print(username + ": " + message)
        #Start TTS Bot

        ##################### MP3 Effects ###################################
    '''
        # checks for '!--' and playes associated effect in soundfx module
        if '!wasted' in message:
            soundfx.sounds0(message)
        elif '!wrong' in message:
            soundfx.sounds1(message)
        elif '!toot' in message:
            soundfx.sounds2(message)
        elif '!pcfail' in message:
            soundfx.sounds3(message)
        elif '!surprise' in message:
            soundfx.sounds4(message)
        elif '!chewy' in message:
            soundfx.sounds5(message)
        elif '!lao' in message:
            soundfx.sounds6(message)
        elif '!scared' in message:
            soundfx.sounds7(message)
        elif '!focus' in message:
            soundfx.sounds8(message)
        elif '!gameover' in message:
            soundfx.sounds9(message)
    '''
        #####################################################################
        
        if '!' in message: #ignore reading song request
            pass
        elif 'http' in message: #ignore reading http links (which really is solved by streamelements below)
            pass
        elif ':tmi' in message: #ignore initial loading text (trust me, remove it and see how annoying it is)
            pass
        elif ':fuzzybottgaming' in message: #same as above
            pass
        elif 'fuzzybottgaming' in username: #ignores your bot if it posts anything
            pass
        elif 'streamelements' in username: #ignores your bot if it posts anything
            pass
        elif ':fuzzybuttgaming' in username: #ignores your username for testing
            pass

        #####################StreamElements Alerts###########################
        elif 'Meow Meow Mother Fluffer' in message:  # Part of Follower Alert from StreamElements
            engine = pyttsx3.init()
            sound = engine.getProperty('voices')
            engine.setProperty('voice', sound[1].id)  # 0= male 1=female
            engine.say(username + " joined you in the litter box")
            # engine.setProperty('rate', 120)  # 120 words per minute
            engine.setProperty('volume', 0.9)
            engine.runAndWait()
        elif 'just hosted the stream for' in message:  # Alert to Hosts
            engine = pyttsx3.init()
            sound = engine.getProperty('voices')
            engine.setProperty('voice', sound[1].id)  # 0= male 1=female
            engine.say(message)
            engine.setProperty('rate', 120)  # 120 words per minute
            engine.setProperty('volume', 0.9)
            engine.runAndWait()
        elif 'just raided the channel with' in message:  # Alert to Raids
            engine = pyttsx3.init()
            sound = engine.getProperty('voices')
            engine.setProperty('voice', sound[1].id)  # 0= male 1=female
            engine.say(message)
            engine.setProperty('rate', 120)  # 120 words per minute
            engine.setProperty('volume', 0.9)
            engine.runAndWait()
         ###################################################################
        elif '@FuzzyButtGaming' in message:  # Alert to mentions only
            engine = pyttsx3.init()
            sound = engine.getProperty('voices')
            engine.setProperty('voice', sound[1].id)  # 0= male 1=female
            message = message.replace('@FuzzyButtGaming', 'fuzzy', 2)
            engine.say(username + " says " + message)
            engine.setProperty('rate', 120)  # 120 words per minute
            engine.setProperty('volume', 0.9)
            engine.runAndWait()
        elif '@' in message:        #Reads anything with @
            engine = pyttsx3.init()
            sound = engine.getProperty('voices')
            engine.setProperty('voice', sound[1].id) #0= male 1=female
            engine.say(username + " says " + message)
            engine.setProperty('rate', 120)  # 120 words per minute
            engine.setProperty('volume', 0.9)
            engine.runAndWait()
        #End TTS Bot
        for pattern in PATT:
            if re.match(pattern,message):
                ban(s, username)
                break
    time.sleep(1 / RATE)






