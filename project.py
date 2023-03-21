import requests
from bs4 import BeautifulSoup
from gtts import gTTS


def main():
    url = input("Enter URL of the webpage: ")
    corrected_url = user_url(url)
    html_content = access_url(corrected_url)
    text = parse_html(html_content)
    text_to_audio(text)
    #play_audio(text_to_audio)


def user_url(url):
    if not url.startswith('http|https'):
        #print('http://' + url)
        return 'http://' + url


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


def parse_html(html_content):
    soup = BeautifulSoup(html_content.content, 'html.parser')
    text = soup.get_text()
    #print(text)
    return text


def text_to_audio(text):
    tts = gTTS(text, lang="en")
    tts.save("text_to_audio.mp3")


if __name__ == "__main__":
    main()
