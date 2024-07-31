import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

# Function to create a new Tor circuit
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()  # Authenticate with Tor (default setup)
        controller.signal(Signal.NEWNYM)

# Function to fetch a webpage using Tor
def fetch_page(url):
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050',
    }
    response = session.get(url)
    return response.text

# Main function to scrape data
def scrape_data(url):
    html = fetch_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract data here. For example:
    title = soup.title.string
    print(f'Title of the page: {title}')

# Get URL from user input
if __name__ == '__main__':
    url = input('Enter the URL of the website to scrape: ')
    scrape_data(url)
