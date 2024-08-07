# Web Scraping Using Tor

Welcome to the **Web Scraping Using Tor** project! This repository demonstrates how to perform web scraping with enhanced anonymity by utilizing the Tor network.

## Key Features

- **Enhanced Anonymity:** Utilizes the Tor network to keep your browsing and scraping activities private and avoid detection.
- **Flexible Configuration:** Easily switch between using Tor for anonymity or a regular connection based on your needs.
- **Detailed Logging:** Automatically logs page titles, HTML content, and performance metrics for comprehensive insights.
- **Execution Time Measurement:** Measures and logs the time taken to fetch pages, both with Tor and regular connections, for performance comparison.
- **Customizable Scraping Logic:** Modify the Python script to extract different types of data from web pages according to your requirements.

## Overview

This project allows you to scrape websites while maintaining privacy and avoiding detection by routing your requests through the Tor network. It is designed for developers and researchers who need to perform web scraping tasks anonymously.

## What It Scrapes

The tool is designed to extract the following types of information from web pages:

- **Page Title:** Logs the title of the web page for easy identification.
- **HTML Content:** Logs the entire HTML content of the page for comprehensive analysis.
- **Links:** Extracts and logs all hyperlinks (`<a>` tags with `href` attributes) found on the page.
- **Execution Time:** Measures and logs the time taken to fetch the page using both Tor and regular connections to compare performance.

## Prerequisites

Before you start, make sure you have the following installed:

- Python 3.x
- Tor (Tor Browser or Tor Service)
- Required Python libraries (specified in `requirements.txt`)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/m13hack/web-scrapping-using-tor.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd web-scrapping-using-tor
   ```

3. **Run the installation script:**

   The `install.sh` script will install all necessary system packages and Python dependencies, and configure Tor:

   ```bash
   chmod +x install.sh
   ./install.sh
   ```

4. **Start the Tor service manually (if not done by the script):**

   ```bash
   sudo systemctl start tor
   ```

5. **Enable Tor to start on boot (if not done by the script):**

   ```bash
   sudo systemctl enable tor
   ```

## Usage

1. **Configure Tor:**
   - Make sure Tor is running and accessible. You may need to adjust the Tor proxy settings in the `config.py` file.

2. **Run the scraper:**

   ```bash
   python3 web_scrapper.py
   ```

3. **Modify the scraping logic:**
   - Edit `web_scrapper.py` to customize the scraping logic according to your requirements.

## Best Practices and Regulations

To ensure ethical and responsible use of this web scraping tool, please adhere to the following best practices and regulations:

### **Best Practices**

1. **Respect Robots.txt:**
   - Always check the `robots.txt` file of a website before scraping. This file specifies the rules for web crawlers and scrapers. Ensure your scraping activities comply with these rules.

2. **Limit Request Frequency:**
   - Avoid sending too many requests in a short period. Implement rate limiting in your scraping logic to minimize the load on the server and avoid being blocked.

3. **Use Tor Responsibly:**
   - Use Tor to protect your anonymity, but avoid abusing the network. Excessive scraping can affect the performance and availability of Tor nodes.

4. **Handle Data Responsibly:**
   - Ensure that any data collected is used ethically and in compliance with data protection regulations. Avoid scraping sensitive or personal information without proper authorization.

5. **Respect Copyright and Terms of Service:**
   - Verify and adhere to the website’s terms of service and copyright policies. Do not scrape content if it is prohibited by the website’s terms.

6. **Monitor and Log Activity:**
   - Keep detailed logs of your scraping activities. This helps in diagnosing issues and provides a record of your scraping operations.

7. **Test on a Smaller Scale:**
   - Test your scraping code on a smaller scale before running it on larger datasets to ensure it behaves as expected and does not cause unintended issues.

### **Regulations**

1. **Compliance with Legal Requirements:**
   - Ensure that your web scraping activities comply with local and international laws, including data protection regulations such as GDPR, CCPA, or similar laws applicable in your region.

2. **Ethical Considerations:**
   - Act ethically by avoiding actions that could be considered malicious or harmful, such as scraping private or confidential information or causing undue disruption to the target website.

3. **Use of Proxies:**
   - If using proxies or anonymization tools like Tor, ensure that their use complies with relevant laws and regulations. Do not engage in activities that might be considered illegal or unethical.

4. **Intellectual Property Rights:**
   - Respect intellectual property rights when scraping and using data from websites. Avoid infringing on copyrights or other intellectual property protections.

5. **Avoiding Overuse:**
   - Do not overload the target website with excessive requests. Ensure that your scraping activities do not negatively impact the performance or availability of the website.

By following these best practices and regulations, you can ensure that your web scraping activities are conducted in an ethical, legal, and responsible manner.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug reports, please submit a pull request or open an issue.

## License

This project is licensed under the [Apache License 2.0](https://opensource.org/licenses/Apache-2.0). See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or inquiries, feel free to reach out to me directly on github.
