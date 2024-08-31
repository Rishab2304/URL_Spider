# URL_Spider

This Python script is a web crawler designed to systematically explore a website, extract and print valid URLs. The crawler supports optional keyword filtering, depth limiting, and rate limiting to ensure responsible and efficient crawling.

Features
URL Normalization: Converts URLs to a consistent format by removing fragments and converting them to lowercase.
URL Validation: Uses HTTP HEAD requests to verify if URLs are valid before processing.
Depth Limiting: Controls how deep the crawler explores within the site (max_depth).
Rate Limiting: Adds a configurable delay between requests to avoid overwhelming the server (delay).
Keyword Filtering: Optionally prints only URLs that contain a specific keyword.

Usage
1)Input Parameters:
Starting URL: The initial URL from which the crawler begins.
Maximum Depth: Number of levels to explore. For example, 2 means the crawler will follow links up to 2 levels deep.
Delay: Time (in seconds) to wait between requests to avoid server overload.
Keyword: Optional. If provided, the crawler will only print URLs containing this keyword.

2)Execution:
The crawler reads from the provided starting URL, normalizes and validates URLs, and explores links up to the specified depth.
Only valid URLs are processed, and the results are printed to the console.

Example
Enter the URL to start crawling: https://example.com
Enter the maximum depth to crawl (e.g., 2): 3
Enter the delay between requests (in seconds, e.g., 1): 1
Do you want to use a specific keyword? (yes/no): no

Dependencies
requests
beautifulsoup4
