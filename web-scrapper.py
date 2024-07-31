import time
import httpx
from bs4 import BeautifulSoup

def fetch_page(url, use_tor=False):
    if use_tor:
        # SOCKS proxy configuration
        client = httpx.Client(proxies={"socks5://": "socks5://127.0.0.1:9050"}, timeout=30)
    else:
        client = httpx.Client()
    
    try:
        response = client.get(url)
        response.raise_for_status()  # Ensure we notice bad responses
        return response.text
    except httpx.HTTPStatusError as e:
        print(f"Error response {e.response.status_code} while requesting {e.request.url}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def scrape_data(url):
    html = fetch_page(url)
    if html is None:
        print("Error: Failed to fetch the page.")
        return

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    print(f"Title of the page: {title}")

def measure_execution_time(url, use_tor=False):
    if use_tor:
        client = httpx.Client(proxies={"socks5://": "socks5://127.0.0.1:9050"}, timeout=30)
    else:
        client = httpx.Client()

    start_time = time.time()
    response = client.get(url)
    print(f"Fetched page with status code: {response.status_code}")

    total_execution_time = time.time() - start_time
    proxy_type = "Tor proxy" if use_tor else "regular"
    print(f"Request with {proxy_type} execution time: {total_execution_time:.2f} seconds")

def main():
    url_to_scrape = input("Enter the URL to scrape: ")

    # Scrape the provided URL
    print("Scraping the provided URL...")
    scrape_data(url_to_scrape)

    # Measure execution time using Tor proxy
    print("Measuring execution time with Tor proxy...")
    measure_execution_time(url_to_scrape, use_tor=True)

    # Measure execution time using regular connection
    print("Measuring execution time with regular connection...")
    measure_execution_time(url_to_scrape, use_tor=False)

if __name__ == '__main__':
    main()
