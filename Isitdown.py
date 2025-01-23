import requests
import time
from datetime import datetime

def check_website(url):
    try:
        response = requests.get(url, timeout=10)  # 10 másodperc timeout
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False

if __name__ == "__main__":
    while True:
        now = datetime.now()
        website_url = "http://beta.bliptext.com"
        if check_website(website_url):
            print(f"{website_url} is up and running at {now.strftime('%H:%M')}.")
            break
        else:
            print(f"{website_url} is not accessible at {now.strftime('%H:%M')}.")
        time.sleep(60)
