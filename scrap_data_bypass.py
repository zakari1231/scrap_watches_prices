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
from datetime import datetime
import time
import json
# driver = uc.Chrome() 
# driver.get('https://api.watchanalytics.io/v1/products/rolex-daytona-116500ln/')

# input("Press any key to exit")

# def scrape_data():
#     # code to initialize the driver and load the page
#     driver = uc.Chrome() 
#     driver.get('https://api.watchanalytics.io/v1/products/rolex-daytona-116500ln/')

#     # wait for the data to load
#     time.sleep(10)

#     # get the element with the pre tag
#     pre_element = driver.find_element(By.TAG_NAME, "pre")

#     # extract the text inside the pre tag
#     data_text = pre_element.text

#     # close the driver
#     driver.quit()

#     return data_text

# print (scrape_data())


def scrape_data():
    # code to initialize the driver and load the page
    options = Options()
    driver = uc.Chrome(options=options) 
    driver.get('https://api.watchanalytics.io/v1/products/rolex-daytona-116500ln/')

    # wait for the data to load
    time.sleep(10)

    # get the element with the pre tag
    pre_element = driver.find_element(By.TAG_NAME, "pre")

    # extract the text inside the pre tag
    data_text = pre_element.text

    # return the data and the driver
    # return data_text, driver
    # convert the text into a JSON object
    data_json = json.loads(data_text)

    # extract the data you need from the JSON object
    product_name = data_json['name']
    product_price_history = data_json['prices']
    product_related = data_json['related']
    # description = data_json['data']['product']['description']

    # create an empty dictionary to store the product information
    related_dict = {}

    # loop through the products and add their information to the dictionary
    for i, product in enumerate(product_related):
        slug = product['slug']
        name = product['name']
        price = product['price']
        related_dict[i+1] = [slug, name, price]
    return product_name, product_price_history, related_dict, driver

# call the scrape_data() function and get the data and the driver
data, product_price_history, related_dict, driver = scrape_data()

# # update the keys in the dictionary in place
# for key in product_price_history.keys():
#     date_obj = datetime.strptime(str(key), '%b %Y')
#     # new_key = date_obj.strftime('%m-%Y')
#     product_price_history[date_obj] = product_price_history.pop(key)

# create a new dictionary to store the updated keys
new_data = {}

# loop through the original dictionary and update the keys
for k, v in product_price_history.items():
    date_obj = datetime.strptime(k, '%b %Y')
    new_key = date_obj.strftime('%Y-%m')
    new_data[new_key] = v

#TODO fix the exit pb in chrome driver

# manually close the driver
input("Press any key to exit")
driver.quit()

# print the data
print(data)
print(new_data)
print(related_dict)
# for key in product_price_history.keys():
#     print(key, type(key))