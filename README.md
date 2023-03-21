PROJECT NAME: WEB SPEAKER
Video Demo: https://youtu.be/gAuFw8QSxyU
Description:

This program might be useful in real life for individuals who prefer to listen to content rather than read it. For example, someone who is visually impaired or someone who is driving and wants to consume content hands-free might find this program useful.

Additionally, this program could be useful for individuals who want to convert long pieces of text, such as articles or research papers, into audio for easier consumption. This could be especially useful for students or professionals who need to review or study large amounts of text but prefer to do so while multitasking or on the go.

Overall, this program offers a convenient way to convert text to audio, which can be useful in a variety of scenarios.

WEB SPEAKER is a Python script that converts the text content of a webpage to audio. It does this by using several libraries: requests, bs4, and gtts.

The script has a main function that prompts the user to enter the URL of the webpage that they want to convert to audio. It then calls several helper functions to accomplish this task.

The user_url function is used to check if the URL entered by the user starts with http or https. If it does not, the function adds http:// to the beginning of the URL and returns the corrected URL.

The access_url function uses the requests library to send a GET request to the specified URL. If the request is successful, it returns the response object. Otherwise, it prints an error message and prompts the user to enter a new URL.

The parse_html function uses the BeautifulSoup library to parse the HTML content of the webpage and extract the text. It then returns this text.

The text_to_audio function uses the gtts library to convert the extracted text to audio and save it as an .mp3 file.

Finally, the script checks if it is being run as the main program and, if it is, calls the main function.

The choice of the requests, bs4, and gtts libraries for this program is likely based on their functionality and ease of use.

The requests library is a popular choice for making HTTP requests in Python because it is easy to use and offers a lot of flexibility. It allows the program to send HTTP requests and receive responses from a server, which is necessary for accessing the content of a webpage.

The bs4 library, also known as Beautiful Soup, is a popular choice for parsing HTML and XML content in Python. It offers a convenient way to navigate and search through the structure of a document, making it easy to extract specific elements or text.

The gtts library, or Google Text-to-Speech, is a convenient way to convert text to audio in Python. It uses the Google Text-to-Speech API to generate high-quality audio from text, and it offers a wide range of options for customization and language support.

These libraries are likely chosen over other alternatives because they are well-established and offer a good balance of functionality and ease of use. However, there may be other libraries or approaches that could also be suitable for this task, depending on the specific requirements of the program.

The tests provided are designed to test the functionality of the access_url, parse_html, and user_url functions in the project module.

The test_access_url function tests the access_url function by sending a GET request to the URL 'http://www.example.com' and verifying that the function returns a response object and that the response has a status code of 200 (indicating a successful request).

The test_parse_html function tests the parse_html function by sending a GET request to 'http://www.example.com', parsing the HTML content of the response using the BeautifulSoup library, and verifying that the parse_html function returns the same text as the parsed HTML content.

The test_user_url function tests the user_url function by providing a URL that does not start with http or https and verifying that the function returns the correct corrected URL with http:// added to the beginning.

Thank you!