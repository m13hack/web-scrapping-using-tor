import time
import httpx
from bs4 import BeautifulSoup

# Define log file
LOG_FILE = "scraping_log.txt"

def fetch_page(url, use_tor=False):
    if use_tor:
        client = httpx.Client(proxies={"socks5://": "socks5://127.0.0.1:9050"}, timeout=30)
    else:
        client = httpx.Client()
    
    try:
        response = client.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        return response.text
    except httpx.HTTPStatusError as e:
        log_message(f"Error response {e.response.status_code} while requesting {e.request.url}")
        return None
    except Exception as e:
        log_message(f"An error occurred: {e}")
        return None

def log_message(message):
    """ Append a message to the log file. """
    with open(LOG_FILE, "a") as log_file:
        log_file.write(message + "\n")

def scrape_data(url):
    html = fetch_page(url)
    if html is None:
        log_message("Error: Failed to fetch the page.")
        return

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    
    # Log the title
    log_message(f"Title of the page: {title}")

    # Log the entire HTML content
    log_message("Page HTML content:")
    log_message(html)

    # Example: Extract all links on the page
    links = [a['href'] for a in soup.find_all('a', href=True)]
    log_message("Found links:")
    for link in links:
        log_message(link)

def measure_execution_time(url, use_tor=False):
    if use_tor:
        client = httpx.Client(proxies={"socks5://": "socks5://127.0.0.1:9050"}, timeout=30)
    else:
        client = httpx.Client()

    start_time = time.time()
    response = client.get(url)
    log_message(f"Fetched page with status code: {response.status_code}")

    total_execution_time = time.time() - start_time
    proxy_type = "Tor proxy" if use_tor else "regular"
    log_message(f"Request with {proxy_type} execution time: {total_execution_time:.2f} seconds")

def main():
    url_to_scrape = input("Enter the URL to scrape: ")

    # Clear the log file at the start
    open(LOG_FILE, "w").close()

    # Scrape the provided URL
    log_message("Scraping the provided URL...")
    scrape_data(url_to_scrape)

    # Measure execution time using Tor proxy
    log_message("Measuring execution time with Tor proxy...")
    measure_execution_time(url_to_scrape, use_tor=True)

    # Measure execution time using regular connection
    log_message("Measuring execution time with regular connection...")
    measure_execution_time(url_to_scrape, use_tor=False)

    print(f"Log file updated: {LOG_FILE}")

if __name__ == '__main__':
    main()
