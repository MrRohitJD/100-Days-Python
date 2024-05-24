import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")

h = ["rohit" , "aditya" ,"Neeta" ,"rohini"]

for i in h:
    speaker.Speak(f"Shout out to {i}")

# speaker.Speak("fuck you")


