import requests
from bs4 import BeautifulSoup


def get_markdown_from_url(url: str) -> str:
    """
    The function `get_markdown_from_url` takes a URL as input, downloads the webpage content, parses the
    HTML to extract the text body, and returns the extracted text as a string.
    
    @param url The `url` parameter is a string that represents the URL of a webpage.
    
    @return The function `get_markdown_from_url` returns a string.
    """
    try:
        # Download the webpage
        response = requests.get(url)
        html = response.content

        # Parse the HTML to extract the text body
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()

        return text

    except Exception:
        return ""
