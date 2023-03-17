import requests

def get_api_data(url):
    try:
        response = requests.get(url)
        api_data = response.json()
        return api_data
    except requests.RequestException:
        print(requests.RequestException)


