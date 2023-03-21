import project
import requests
from bs4 import BeautifulSoup
from gtts import gTTS


def test_access_url():

    url = 'http://www.example.com'
    expected_output = requests.Response
    assert isinstance(project.access_url(url), expected_output)
    assert project.access_url(url).status_code == 200


def test_parse_html():
    # test that the parse_html function returns the text from the HTML content
    html_content = requests.get('http://www.example.com')
    expected_output = BeautifulSoup(html_content.content, 'html.parser').get_text()
    assert project.parse_html(html_content) == expected_output


def test_user_url():
    url = 'www.example.com'
    expected_output = 'http://www.example.com'
    assert project.user_url(url) == expected_output

