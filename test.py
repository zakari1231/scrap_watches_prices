# url = 'https://api.watchanalytics.io/v1/products/rolex-daytona-116500ln/'

def url_to_slug(url):
    new_str = url.split('/')
    return new_str[-2]

urls = ['https://api.watchanalytics.io/v1/products/audemars-piguet-royal-oak-offshore-25940sk-oo-d002ca-02-a/', 'https://api.watchanalytics.io/v1/products/audemars-piguet-royal-oak-offshore-navy-26170st-oo-d305cr-01/', 'https://api.watchanalytics.io/v1/products/rolex-daytona-16520/', 'https://api.watchanalytics.io/v1/products/audemars-piguet-royal-oak-offshore-panda-26170st-oo-d101cr-02/', 'https://api.watchanalytics.io/v1/products/audemars-piguet-royal-oak-offshore-safari-26020st-oo-d091cr-01/', 'https://api.watchanalytics.io/v1/products/rolex-daytona-116520/', 'https://api.watchanalytics.io/v1/products/audemars-piguet-royal-oak-offshore-26170st-oo-1000st-01/', 'https://api.watchanalytics.io/v1/products/rolex-yacht-master-ii-116680/', 'https://api.watchanalytics.io/v1/products/audemars-piguet-royal-oak-offshore-diver-15710st-oo-a010ca-01/']

for url in urls:
    print(url_to_slug(url))
