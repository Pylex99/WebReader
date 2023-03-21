import requests  # Used to make HTTP requests
from bs4 import BeautifulSoup  # Used to parse HTML content
from gtts import gTTS  # Used to convert text to audio


# Takes input URL from the user, accesses the URL, parses the HTML content and converts text to audio
def main():
    url = input("Enter URL of the webpage: ")
    corrected_url = user_url(url)
    html_content = access_url(corrected_url)
    text = parse_html(html_content)
    text_to_audio(text)
    
    
# Corrects the URL entered by the user if it doesn't start with http or https
def user_url(url):
    if not url.startswith('http|https'):
        #print('http://' + url)
        return 'http://' + url


# Accesses the URL and gets the HTML content
def access_url(url):
    try:
        response = requests.get(url)
    except:
        print("Invalid URL")
        user_url(url)
    if response.status_code == 200:
        return response
    else:
        print("Invalid URL")


# Parses the HTML content and gets the text
def parse_html(html_content):
    soup = BeautifulSoup(html_content.content, 'html.parser')
    text = soup.get_text()
    #print(text)
    return text


# Converts text to audio and saves the audio as a file
def text_to_audio(text):
    tts = gTTS(text, lang="en")
    tts.save("text_to_audio.mp3")


if __name__ == "__main__":
    main()
