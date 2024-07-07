from tts import print_speak
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen
import requests
from selenium.webdriver.common.by import By
import time

def news():
    print_speak('In which form you would like to get the daily news')
    print("1) for headlines in English\n2) for listening in English\n3) to quit")
    pref = input("Please enter your preference: ")
    
    if '1' in pref:
        news_url = 'https://news.google.com/news/rss'
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close()
        soup_page = Soup(xml_page, "html.parser")
        news_list = soup_page.findAll('item')
        for news in news_list:
            print(news.title.text)
            print(news.link.text)
            print(news.pubDate)
            print("_" * 60)
            
    elif '2' in pref:
        toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
        toi_soup = BeautifulSoup(toi_r.content, 'html5lib')
        toi_headings = toi_soup.find_all('h2')
        toi_headings = toi_headings[0:-13]  
        toi_news = []
        for th in toi_headings:
            toi_news.append(th.text)
        for news in toi_news:
            print_speak(news)
            
    else:
        pass

def login_facebook(driver, username, password):
    driver.get("https://www.facebook.com/")
    time.sleep(2)
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()

def login_instagram(driver, username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()

def login_linkedin(driver, username, password):
    driver.get("https://www.linkedin.com/")
    time.sleep(2)
    driver.find_element(By.ID, "session_key").send_keys(username)
    driver.find_element(By.ID, "session_password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button").click()

def login_twitter(driver, username, password):
    driver.get("https://www.twitter.com/login")
    time.sleep(2)
    driver.find_element(By.NAME, "session[username_or_email]").send_keys(username)
    driver.find_element(By.NAME, "session[password]").send_keys(password)
    driver.find_element(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]').click()

def current_location():
    import geocoder
    from geopy.geocoders import Nominatim
    g = geocoder.ip('me')
    latitude, longitude = g.latlng
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse((latitude, longitude), language='en')
    print(location.address)
    if location:
        address = location.raw['address']
        street = address.get('road', '')
        city = address.get('city', '')
        state = address.get('state', '')
        postcode = address.get('postcode', '')
        
        print(f"Street: {street}")
        print(f"City: {city}")
        print(f"State: {state}")
        print(f"Zip Code: {postcode}")
    else:
        print("Location not found")