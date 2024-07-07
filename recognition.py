from tts import speak, print_speak, speech
import speech_recognition as sr

command = sr.Recognizer()

def speech_command():
    try:
        with sr.Microphone() as source:
            speak('listening..')
            audio = command.listen(source = source, timeout = 5, phrase_time_limit = 5)
            query = command.recognize_google(audio, language = 'en-IN')
            print(f'User said: {query}')
            return query
    except OSError:
        print_speak("Microphone is not connected.")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    except sr.WaitTimeoutError:
        pass
    except Exception as e:
        print(e)
        speak("Unable to recognize your voice.")
        return None

def chat_command():
    text = input("Command: ")
    return text

def hin_command():
    try:
        with sr.Microphone() as source:
            speech('बोलिये..')
            audio = command.listen(source = source, timeout = 5, phrase_time_limit = 5)
            query = command.recognize_google(audio, language = 'hi')
            print(f'User said: {query}')
            return query
    except OSError:
        speech("माइक्रोफ़ोन कनेक्ट नहीं है.")
    except sr.RequestError:
        speech("मुझे एक समस्या का सामना करना पड़ रहा है कृपया बाद में पुनः प्रयास करें")
    except sr.WaitTimeoutError:
        pass
    except Exception as e:
        print(e)
        speech("आपकी आवाज पहचानने में असमर्थ")
        return None
        
def define_input():
    input_option = str(input("Would you like to talk in english or hindi, or simply chat with me?\n: ").lower())
    while input_option != "chat" and input_option != "talk in hindi" and input_option != "talk in english":
        input_option = str(input("Invalid input. Would you like to talk in english or hindi, or chat with me?\n: ".lower()))
    if input_option == "chat":
        return chat_command
    elif input_option == "talk in hindi":
        return hin_command
    else:
        return speech_command
