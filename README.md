# TwitchTTSChatBot
Working with PYTTSX3 to create a tts bot for the chat
I am new to this whole thing so feel free to tweek whatever
you want.  I am still learning how to do the pull requests

# Feel free to make the TTS part more simple than the if/elif ductape version I have
## TwitchTTSChatBot updates:
- 10/11/18 Uploaded
  - must pip install pyttsx3
- 10/12/18 -fixed bot to:
  - only speak when '@' symbol is used
  - use voice to mention follow/host/raid alerts
  - ignore reading inital start-up responces
- 10/13/18 -added ability to call soundfx.py for sound effects
  - must first install pip install soundplay
- 10/16/18 -FIXED to now send messages to chat
  - line 17: took out the '#' in CHAN
  - line 18: had to add in a 2nd CHAN so the bot will show messages, same with line 39 and 52
  - line 50: added '\r\n' and '.encode("utf-8")'
  - line 75: added message to be sent into chat when bot connects
## Soundfx updates:
- 10/13/18 -soundfx.py added to store mp3 files for chat to call upon
