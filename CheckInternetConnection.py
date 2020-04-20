import requests
from datetime import date

def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("İnternet Disconnect")
    return False

result = check_internet()
print(result)

today = date.today()
print("Today's date:", today)

input("EnyPress to exit")
