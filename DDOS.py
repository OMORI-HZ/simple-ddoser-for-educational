import requests
import threading

# Target URL (Use a local or approved server for testing)
target_url = "http://example.com"

# Function to send a request
def send_request():
    try:
        response = requests.get(target_url)
        print(f"Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Number of threads (simulate multiple clients)
num_threads = 100

# Create and start threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
