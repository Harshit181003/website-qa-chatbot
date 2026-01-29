import requests
from bs4 import BeautifulSoup

def extract_website_text(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    
    for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
        tag.decompose()

    text = soup.get_text(separator=" ")

    
    lines = [line.strip() for line in text.splitlines()]
    cleaned_text = " ".join([line for line in lines if line])

    title = soup.title.string if soup.title else "No Title"

    return cleaned_text, title