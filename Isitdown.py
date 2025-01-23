import requests
import time

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
        website_url = "http://beta.bliptext.com"
        if check_website(website_url):
            print(f"{website_url} is up and running.")
            break
        else:
            print(f"{website_url} is not accessible.")
        time.sleep(60)
