import time
import httpx
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

# Initialize colorama
init()

# Define log file
LOG_FILE = "scraping_log.txt"

# Define ASCII art with colors
ASCII_ART = f"""
{Fore.CYAN}{Style.BRIGHT}
 /$$$$$$$$ /$$$$$$  /$$$$$$$           /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$  /$$     /$$
|__  $$__//$$__  $$| $$__  $$         /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$__  $$|  $$   /$$/
   | $$  | $$  \\ $$| $$  \\ $$        | $$  \\__/| $$  \\__/| $$  \\ $$| $$  \\ $$| $$  \\ $$ \\  $$ /$$/ 
   | $$  | $$  | $$| $$$$$$$/ /$$$$$$|  $$$$$$ | $$      | $$$$$$$/| $$$$$$$$| $$$$$$$/  \\  $$$$/  
   | $$  | $$  | $$| $$__  $$|______/ \\____  $$| $$      | $$__  $$| $$__  $$| $$____/    \\  $$/   
   | $$  | $$  | $$| $$  \\ $$         /$$  \\ $$| $$    $$| $$  \\ $$| $$  | $$| $$          | $$    
   | $$  |  $$$$$$/| $$  | $$        |  $$$$$$/|  $$$$$$/| $$  | $$| $$  | $$| $$          | $$    
   |__/   \\______/ |__/  |__/         \\______/  \\______/ |__/  |__/|__/  |__/|__/          |__/    
                                                                                                   
                                                                                                   
{Style.RESET_ALL}
"""

def fetch_page(url, use_tor=False):
    proxies = {"socks5://": "socks5://127.0.0.1:9050"} if use_tor else None
    try:
        with httpx.Client(proxies=proxies, timeout=30) as client:
            response = client.get(url)
            response.raise_for_status()  # Ensure we notice bad responses
            return response.text
    except httpx.HTTPStatusError as e:
        log_message(f"Error response {e.response.status_code} while requesting {e.request.url}")
    except httpx.RequestError as e:
        log_message(f"Request error: {e}")
    except Exception as e:
        log_message(f"An unexpected error occurred: {e}")
    return None

def log_message(message):
    """ Append a message to the log file with timestamp. """
    with open(LOG_FILE, "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - {message}\n")

def scrape_data(url):
    html = fetch_page(url)
    if html is None:
        log_message("Error: Failed to fetch the page.")
        return

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    
    # Log the title
    log_message(f"Title of the page: {title}")

    # Log the entire HTML content (may be large)
    log_message("Page HTML content (truncated):")
    log_message(html[:1000])  # Truncate for readability

    # Example: Extract all links on the page
    links = [a['href'] for a in soup.find_all('a', href=True)]
    log_message("Found links:")
    for link in links:
        log_message(link)

def measure_execution_time(url, use_tor=False):
    proxies = {"socks5://": "socks5://127.0.0.1:9050"} if use_tor else None
    try:
        with httpx.Client(proxies=proxies, timeout=30) as client:
            start_time = time.time()
            response = client.get(url)
            response.raise_for_status()
            total_execution_time = time.time() - start_time
            proxy_type = "Tor proxy" if use_tor else "regular"
            log_message(f"Request with {proxy_type} execution time: {total_execution_time:.2f} seconds")
    except httpx.RequestError as e:
        log_message(f"Request error during timing measurement: {e}")
    except Exception as e:
        log_message(f"An unexpected error occurred during timing measurement: {e}")

def main():
    print(ASCII_ART)  # Print ASCII art at the start

    url_to_scrape = input("Enter the URL to scrape: ").strip()
    if not url_to_scrape.startswith("http"):
        print(Fore.RED + "Invalid URL. Please ensure the URL starts with 'http' or 'https'." + Style.RESET_ALL)
        return

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
