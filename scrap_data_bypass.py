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

import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
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
    driver = uc.Chrome() 
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
    # description = data_json['data']['product']['description']
    return product_name, driver

# call the scrape_data() function and get the data and the driver
data, driver = scrape_data()


# manually close the driver
input("Press any key to exit")
driver.quit()

# print the data
print(data)