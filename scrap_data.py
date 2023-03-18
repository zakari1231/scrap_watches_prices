import requests
import time

def get_api_data(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'}

    try:
        response = requests.get(url, headers=headers,)
        time.sleep(25)
        if response.status_code == 200:
            api_data = response.json()
            return api_data
        else:
            print("Error from server: " + str(response.content))
            return None
    except requests.RequestException as e:
        print("Error: " + str(e))
        return None


url = 'https://api.watchanalytics.io/v1/products/rolex-daytona-116500ln/'

for i in range(1):  # Make 10 requests
    response = get_api_data(url)
    if response is not None:
        time.sleep(5)
        raw_data = response
        print(raw_data)
        # content = raw_data.content.decode()
        # print(content)
    time.sleep(1) 

# response = get_api_data(url)
# product_name = response['title']

# print (product_name)