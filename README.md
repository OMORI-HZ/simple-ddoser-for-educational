# simple-ddoser-for-educational
its just for educational practice and I do not guarantee that it will not be used for negative and illegal activities, and all responsibility for using this tool rests with the user

btw how to use:

To run the enhanced HTTP Request Flooder with the interactive menu in Python, follow these steps:

### Step-by-Step Instructions

1. **Install Required Libraries**:

   Before running the script, ensure you have the `requests` library installed. If you haven't installed it yet, you can do so using pip:

   ```bash
   pip install requests
   ```

2. **Save the Script**:

   Copy the entire Python script provided in the previous response into a file, e.g., `http_flooder.py`.

3. **Run the Script**:

   Open a terminal or command prompt, navigate to the directory where `http_flooder.py` is saved, and then run the script using Python:

   ```bash
   python http_flooder.py
   ```

4. **Follow the Interactive Menu**:

   - The script will prompt you to enter various parameters interactively:
     - Enter the target URL (e.g., `http://example.com`).
     - Choose the HTTP method (`GET` or `POST`).
     - Enter the number of threads (concurrent connections) you want to use.
     - Specify the number of requests each thread will make.
     - Optionally, provide POST data if you chose `POST` as the method.
     - Enter any custom headers in the format `key=value`, separated by commas.

5. **Execution**:

   - Once you've entered all the parameters, the script will start flooding the target URL with HTTP requests.
   - You'll see output indicating the progress of each request as it sends requests concurrently using multiple threads.

6. **Completion**:

   - After all threads have completed their requests, the script will print `Completed sending requests.`

### Example Usage

Here’s an example of how you might interact with the script:

```
$ python http_flooder.py
HTTP Request Flooder Configuration Menu
--------------------------------------
Enter the target URL: http://example.com
Enter the HTTP method (GET/POST): GET
Enter the number of threads: 10
Enter the number of requests per thread: 100
Enter the data to send with POST requests (leave blank for GET):
Enter custom headers (key=value, comma-separated):
```

After entering the required parameters and hitting Enter, the script will start flooding the specified URL with GET requests from 10 threads, each thread making 100 requests.

### Notes

- **Proxies**: The script uses a predefined list of proxies for request distribution. Ensure these proxies are correctly configured and available if you choose to use them.
- **Logging**: All request activities are logged to `request_flood.log` in the current working directory.
- **Responsibility**: Use this script responsibly and only on systems where you have explicit permission to test. Flooding a server with requests without permission may violate terms of service or even legal regulations.

By following these steps, you can effectively use the HTTP Request Flooder script with an interactive menu to test and understand its functionality. Adjust parameters as necessary to suit your testing requirements.


also do not forget to star this project and follow ;) 🥤

🤍🩶💛🤎💜🩵💙💚🧡🩷❤️🖤
