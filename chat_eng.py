from tts import print_speak

def chat(query: str):
    if 'how are you' in query or "how's life" in query:
        print_speak("I am good, doing great things.")

    elif 'what are you doing' in query:
        print_speak("I am your assistant and listening to your orders")

    elif 'what am i doing' in query:
        print_speak("My guess is you are giving orders to me")

    elif 'where do you live' in query or 'where do you stay' in query or 'where is your home' in query \
            or 'what is your address' in query:
        print_speak(
            'I live in your workplace or maybe in your work things like your laptop or computer.')

    elif 'whom am I talking to' in query:
        print_speak("You are talking to your assistant")

    elif 'who created you' in query or 'who made you' in query or 'who is your creator' in query:
        print_speak('I was created by Sandhya for her science project.')

    elif 'what is your name' in query or 'what should I call you' in query or \
            "what's your name" in query:
        print_speak("You can call me Jarvis.")

#You can continue from here.
