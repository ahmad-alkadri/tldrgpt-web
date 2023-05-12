import requests
from bs4 import BeautifulSoup


def get_text_from_url(url):
    """
    The function takes a URL as input, downloads the webpage, extracts the text body using
    BeautifulSoup, removes paragraph breaks and other whitespace, and returns the cleaned text.

    @param url The URL of the webpage that you want to extract text from.

    @return the text content of a webpage after downloading and parsing the HTML. The text is cleaned by
    removing paragraph breaks and other whitespace before being returned.
    """
    # Download the webpage
    response = requests.get(url)
    html = response.content

    # Parse the HTML to extract the text body
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()

    # Remove paragraph breaks and other whitespace
    text = text.replace("\n", " ")
    text = " ".join(text.split())

    return text
