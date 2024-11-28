import requests
from bs4 import BeautifulSoup


def get_html(url):
    """Extracts the text content of a webpage, removing scripts, styles, and other unnecessary elements."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove scripts, styles, and other unnecessary elements
    for element in soup(['script', 'style', 'meta', 'link']):
        element.decompose()
        
    # Get text while preserving some structure
    text = soup.get_text(separator='\n', strip=True)
    return text
