#.venv\Scripts\activate -> to activate virtual environment.
import recognition
from tts import speak, speech, print_speak
from os import system
import commands
from random import choice
import sys_info
import social
import pm
import time
from datetime import datetime

if __name__ == '__main__':
    clear = lambda: system('cls')
    clear()
    input_func = recognition.define_input()
    pm1 = pm.PasswordManager()
    
    while True:
        try:
            cmd = input_func().lower()
                
            if any(element in cmd.split() for element in commands.greetEng):
                from commands import greet_responseEng
                print_speak(choice(greet_responseEng))
            if any(element in cmd.split() for element in commands.greetHin):
                from commands import greet_responseHin
                speech(choice(greet_responseHin))
                
            elif any(element in cmd for element in commands.chat):
                import chat_eng
                try:
                    chat_eng.chat(cmd)
                except ModuleNotFoundError:
                    print_speak('The chitchat module is not installed')
                    continue
                except Exception:
                    pass
            elif any(element in cmd for element in commands.chatHin):
                import chat_hin
                try:
                    chat_hin.chat_hin(cmd)
                except ModuleNotFoundError:
                    print_speak('The chitchat module is not installed')
                    continue
                except Exception:
                    pass
            
            elif any(element in cmd for element in commands.voice_chatEng):
                from recognition import chat_command
                input_func = chat_command
            elif any(element in cmd for element in commands.voice_chatHin):
                from recognition import chat_command
                input_func = chat_command

            elif any(element in cmd for element in commands.chat_voice_toEng):
                from recognition import speech_command
                input_func = speech_command
            elif any(element in cmd for element in commands.chat_voiceHin_toEng):
                from recognition import speech_command
                input_func = speech_command

            elif any(element in cmd for element in commands.chat_voice_toHin):
                from recognition import hin_command
                input_func = hin_command
            
            elif 'location' in cmd.lower():
                social.current_location()
                    
            elif any(element in cmd.split() for element in commands.news):
                social.news()
            
            elif any(element in cmd.split() for element in commands.system_o):
                sys_info.System_Information()
                
            elif any(element in cmd.split() for element in commands.insta):
                minutes = int(input("For, how many minutes do you wish to spend time on your socials: "))
                choice = input("Would you like to (a)dd new credentials or (l)ogin using saved credentials? ").strip().lower()

                if choice == 'a':
                    username = input("Enter your username/email: ").strip()
                    password = input("Enter your password: ").strip()
                    pm1.add_password('instagram', username, password)
                    print_speak("Credentials saved successfully. Reprompt again for login")
                elif choice == 'l':
                    username, password = pm1.get_password('instagram')
                    if username and password:
                        try:
                            driver = social.webdriver.Chrome()
                            social.login_instagram(driver, username, password)
                            print_speak("Press ctrl + c to terminate the browser.")
                            time.sleep(minutes*60)
                            driver.quit()
                        except KeyboardInterrupt:
                            driver.quit()
                else:
                    print("Invalid choice.")
                    
            # Add here more socials-facebook, linkedin, twitter
                    
            elif any(element in cmd.split() for element in commands.add):
                platform = input("Enter the platform: ").strip().lower()
                username = input("Enter your username/email: ").strip()
                password = input("Enter your password: ").strip()
                pm1.add_password(platform, username, password)
                print("Credentials saved successfully.")
                
            elif any(element in cmd.split() for element in commands.battery):
                sys_info.battery()
            
            elif any(element in cmd.split() for element in commands.yt):
                import pywhatkit as kit
                try:
                    query = cmd.replace("play" or "प्ले", "")
                    kit.playonyt(query)
                except ImportError:
                    print_speak('Please install pywhatkit')
                except ConnectionError:
                    print_speak('There was a connection error')
                except Exception:
                    pass
            
            elif 'wikipedia' in cmd.lower() or 'विकिपीडिया' in cmd:
                import wikipedia
                try:
                    query = cmd.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=5)
                    print_speak('Searching Wikipedia...')
                    print_speak("According to Wikipedia")
                    print_speak(results)
                except ImportError:
                    print_speak('Please install wikipedia')
                except ConnectionError:
                    print_speak('There was a connection error')
                except Exception:
                    print_speak('There was a error')
                
            elif any(element in cmd.split() for element in commands.search):
                import pywhatkit as kit
                try:
                    kit.search(cmd)
                except ImportError:
                    print_speak('Please install pywhatkit')
                except ConnectionError:
                   print_speak('There was a connection error')
                except Exception:
                    pass
                
            elif 'dictionary' in cmd:
                from PyDictionary import PyDictionary
                try:
                    dictionary = PyDictionary()
                    word = input_func("What is the word: ")
                    print(dictionary.meaning(word),'\n')
                    print(dictionary.synonym(word),'\n')
                    print(dictionary.antonym(word),'\n')
                    speech(dictionary.translate(word, 'hi'),'\n')
                except ImportError:
                    print_speak('Please install PyDictionary')
                except ConnectionError:
                    print_speak('There was a connection error')
                except Exception:
                    print_speak('There was an error')
                
            elif any(element in cmd.split() for element in commands.photo):
                import cv2
                try:
                    videoCaptureObject = cv2.VideoCapture(0)
                    result = True
                    while (result):
                        ret, frame = videoCaptureObject.read()
                        cv2.imwrite("New_Picture.jpg", frame)
                        result = False
                    videoCaptureObject.release()
                    cv2.destroyAllWindows()
                except ImportError:
                    print_speak('Please install PyDictionary')
                except Exception:
                    print_speak('There was an error')
            
            elif any(element in cmd.split() for element in commands.write):
                speech("मुझे क्या लिखना है")
                print("What should I write: ")
                note = input_func()
                file = open('jarvis.txt', 'w')
                speech("दिन और समय भी दालु")
                print("Should i include date and time")
                snfm = input_func()
                if 'yes' in snfm or 'sure' in snfm or 'हाँ' in snfm:
                    strfTime = datetime.now().strftime('%H:%M:%S:%p')
                    file.write(strfTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif any(element in cmd.split() for element in commands.show):
                speech("Showing Notes")
                file = open("jarvis.txt", "r")
                print_speak(file.read())
                
            elif any(element in cmd.split() for element in commands.weather): 
                from Py_Weather import get_weather
                try:
                    city = 'Mumbai'
                    weather_data = get_weather(city)
                except Exception as e:
                    pass
                
            elif 'open drive' in cmd or 'ओपन ड्राइव' in cmd:
                import os
                speech("C or D: ")
                query = input(':')
                if "C" in query or "c" in query:
                    os.startfile("C:")
                elif "D" in query or "d" in query:
                    os.startfile("D:")
                else:
                    print('no such directory/ऐसा कुछ भी नहीं है')
                
            elif 'date' in cmd.lower() or 'दिनांक' in cmd or 'तारीख' in cmd:
                today = datetime.today()
                print_speak(f"{today:%B %d, %Y}")

            elif 'time' in cmd.lower() or 'समय' in cmd or 'वक़्त' in cmd:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                print_speak(current_time)
            
            elif any(element in cmd.split() for element in commands.lock):
                import ctypes
                ctypes.windll.user32.LockWorkStation()
                exit()
                
            elif any(element in cmd.split() for element in commands.shutdown):
                import subprocess, time
                speech("Make sure all the application are closed before sign-out\nसुनिश्चित करें कि साइन-आउट से पहले सभी "
                    "एप्लिकेशन बंद हैं")
                time.sleep(10)
                subprocess.call(["shutdown", "/r"])

            elif 'jarvis' in cmd:
                speak("Jarvis 1 point 0 in your service ")
            elif 'जार्विस' in cmd:
                speech("जार्विस १ पॉइंट ० आपकी सेवा में")

            elif any(element in cmd.split() for element in commands.sleep):
                speech("For how much time, should I relax human")
                a = int(input(':'))
                time.sleep(a*60)
                print(a)

            elif any(element in cmd.split() for element in commands.restart):
                subprocess.call(["shutdown", "/r"])

            elif any(element in cmd.split() for element in commands.exit):
                import sys
                sys.exit(0)
                
                
        except Exception as e:
            pass
