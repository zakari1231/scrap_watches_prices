# import cloudscraper 
 
# scraper = cloudscraper.create_scraper(delay=10, browser="chrome") 
# content = scraper.get("https://api.watchanalytics.io/v1/products/rolex-daytona-116500ln/").text 
 
# print(content)
################################################
# import cfscrape 
 
# scraper = cfscrape.create_scraper() 
# scraped_data = scraper.get('https://api.watchanalytics.io/v1/products/rolex-daytona-116500ln/') 
# print(scraped_data.text)
##################################################

# import undetected_chromedriver as uc
import undetected_chromedriver as uc 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import time
import json

def url_to_slug(url):
    new_str = url.split('/')
    return new_str[-2]

def scrape_data(url, driver = None, depth = 0):
    if not driver:
        # code to initialize the driver and load the page
        options = Options()
        driver = uc.Chrome(options=options) 
        driver.get(url)
    else:
        driver.get(url)

    # wait for the data to load
    time.sleep(10)

    # get the element with the pre tag
    pre_element = driver.find_element(By.TAG_NAME, "pre")

    # extract the text inside the pre tag
    data_text = pre_element.text

    # convert the text into a JSON object
    data_json = json.loads(data_text)

    # extract the data you need from the JSON object
    product_name = data_json['name']
    product_ref = data_json['ref']
    product_price_history = data_json['prices']
    product_related = data_json['related']

    slug_url = url_to_slug(url)

    # convert the product_price dictionary to a list of dictionaries
    product_price_list = [{'date': k, 'price': v} for k, v in product_price_history.items()]

    # create a new dictionary to store the updated keys
    product_price = {}

    # loop through the original dictionary and update the keys
    for k, v in product_price_history.items():
        date_obj = datetime.strptime(k, '%b %Y')
        new_key = date_obj.strftime('%Y-%m')
        product_price[new_key] = v

     # create a list of dictionaries to store the product information
    related_dict_list = []

    # loop through the products and add their information to the list of dictionaries
    for i, product in enumerate(product_related):
        slug = product['slug']
        name = product['name']
        price = product['price']
        related_dict_list.append({'id': i+1, 'slug': slug, 'name': name, 'price': price})

    # save the result into csv file 
    df = pd.DataFrame(product_price_list)
    df.to_csv(f'{slug_url}_prices_history.csv', index=False)
    df2 = pd.DataFrame(related_dict_list)
    df2.to_csv(f'{slug_url}_related_watches.csv', index=False)

    if depth > 0:
        scrape_related_watches(related_dict_list, driver, depth-1)
    
    return product_name, product_price_list, related_dict_list, driver


def from_slug_to_url(related_list):
    url_list = []
    for item in related_list:
        slug = item['slug']
        new_item = f'https://api.watchanalytics.io/v1/products/{slug}/'
        url_list.append(new_item)
    return url_list



def scrape_related_watches(related_list, driver, depth):
    urls = from_slug_to_url(related_list)
    for url in urls:
        scrape_data(url, driver, depth)


url = 'https://api.watchanalytics.io/v1/products/rolex-daytona-116500ln/'
# call the scrape_data() function and get the data and the driver
name, product_price_list, related_dict, driver = scrape_data(url)

depth = 2  # set the maximum depth to scrape related watches
name, product_price_list, related_dict, driver = scrape_data(url, depth=depth)

# list_urls = from_slug_to_url(related_dict)
# # loop to save data from url and related urls
# for i in list_urls:
#     scrape_data(i, driver)

#TODO fix the exit pb in chrome driver

# manually close the driver
input("Press any key to exit")
driver.quit()

# print the data
# print(name)
# print(product_price_list)
# print(related_dict)
# print(from_slug_to_url(related_dict))

# save the result into csv file 
# df = pd.DataFrame(product_price_list)
# df.to_csv(f'{name}_prices_history.csv', index=False)
# df2 = pd.DataFrame(related_dict)
# df2.to_csv(f'{name}_related_watches.csv', index=False)
