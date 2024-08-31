from urllib.parse import urljoin, urlparse, urlunparse
from bs4 import BeautifulSoup
import requests
from collections import deque
import time

def normalize_url(url):
    """Normalize URLs by removing fragments and converting to lowercase."""
    parsed_url = urlparse(url)
    normalized = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))
    return normalized.lower()

def is_valid_url(url):
    """Check if the URL is valid by making a HEAD request."""
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def spider_urls(start_url, keyword=None, max_depth=2, delay=1):
    """Crawl the web using BFS with URL normalization, optional keyword search, depth limit, and rate limiting."""
    queue = deque([(start_url, 0)])
    visited_urls = set()
    
    while queue:
        url, depth = queue.popleft()
        if depth > max_depth:
            continue
        
        normalized_url = normalize_url(url)
        if normalized_url in visited_urls:
            continue
        
        if not is_valid_url(url):
            continue
        
        visited_urls.add(normalized_url)
        
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            
            for a_tag in soup.find_all("a"):
                href = a_tag.get("href")
                if href:
                    absolute_url = urljoin(url, href)
                    normalized_absolute_url = normalize_url(absolute_url)
                    
                    if keyword:
                        if keyword in href:
                            print(normalized_absolute_url)
                    else:
                        print(normalized_absolute_url)
                    
                    if normalized_absolute_url not in visited_urls:
                        queue.append((normalized_absolute_url, depth + 1))
        
        except requests.exceptions.RequestException as e:
            print(f'Error fetching {url}: {e}')
        
        time.sleep(delay)  # Delay between requests to avoid overloading servers

if __name__ == "__main__":
    url = input("Enter the URL to start crawling: ")
    
    print("\n--- Web Crawler Settings ---")
    print("Recommended Maximum Depth:")
    print("  - Shallow (1-2): Ideal for quick and small crawls.")
    print("  - Moderate (3-4): Balanced for more extensive crawling.")
    print("  - Deep (5+): For thorough crawls; use with caution.")
    
    max_depth = int(input("Enter the maximum depth to crawl (e.g., 2): "))
    
    print("\nRecommended Delay Between Requests:")
    print("  - Short (0.5-1 second): Faster but may risk being blocked.")
    print("  - Moderate (1-2 seconds): Balanced speed and server respect.")
    print("  - Long (3+ seconds): Very respectful to server load.")
    
    delay = float(input("Enter the delay between requests (in seconds, e.g., 1): "))
    
    keyword_option = input("Do you want to use a specific keyword? (yes/no): ").strip().lower()
    
    if keyword_option == 'yes':
        keyword = input("Enter the keyword to search for in URLs: ")
    else:
        keyword = None
    
    spider_urls(url, keyword, max_depth, delay)
