import time
import httpx
from scrapfly import ScrapeConfig, ScrapflyClient

def scrapfly_scrape(url, api_key):
    scrapfly = ScrapflyClient(key=api_key)
    response = scrapfly.scrape(ScrapeConfig(
        url=url,
        asp=True,  # enable the anti scraping protection to bypass blocking
        proxy_pool="public_residential_pool",  # select the residential proxy pool
        country="US",  # set the proxy location to a specific country
        render_js=True  # enable rendering JavaScript (like headless browsers) to scrape dynamic content if needed
    ))

    # use the built in Parsel selector
    selector = response.selector
    # access the HTML content
    html = response.scrape_result['content']
    print(f"Scraped content length: {len(html)}")
    return html

def measure_execution_time(url_pattern, use_tor=False):
    if use_tor:
        client = httpx.Client(proxies={"http://": "http://127.0.0.1:9050", "https://": "http://127.0.0.1:9050"}, timeout=5000)
    else:
        client = httpx.Client()

    start_time = time.time()
    for page_number in range(1, 6):
        response = client.get(url_pattern.format(page_number))
        print(f"Fetched page {page_number} with status code: {response.status_code}")

    total_execution_time = time.time() - start_time
    proxy_type = "Tor proxy" if use_tor else "regular"
    print(f"Requests with {proxy_type} execution time: {total_execution_time:.2f} seconds")

def main():
    scrapfly_api_key = input("Enter your ScrapFly API key: ")
    url_to_scrape = input("Enter the URL to scrape: ")
    paginated_url_pattern = input("Enter the paginated URL pattern (use {} for page number): ")

    # Scrape using Scrapfly
    print("Scraping using Scrapfly...")
    scrapfly_scrape(url_to_scrape, scrapfly_api_key)

    # Measure execution time using Tor proxy
    print("Measuring execution time with Tor proxy...")
    measure_execution_time(paginated_url_pattern, use_tor=True)

    # Measure execution time using regular connection
    print("Measuring execution time with regular connection...")
    measure_execution_time(paginated_url_pattern, use_tor=False)

if __name__ == '__main__':
    main()
