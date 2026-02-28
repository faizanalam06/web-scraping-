
import pandas as pd
import requests

from bs4 import BeautifulSoup

web = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets")

# first we will check the response of web
print(web)

# now we will make the soup for extracting the information from the web
soup = BeautifulSoup(web.content, "html.parser")

# using prettify look like structure way
#print(soup.prettify())


# now we will go to the website and open the inspect then shows everything informations in this part we 
# we will collect the Tablet name, features, price rating and review

# using find and fnd_all

mobiles = []
product_container = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
#print(product_container)

for container in product_container:
    
    # Extract title
    title_element = container.find("a", class_="title")
    title = title_element['title'] if title_element else "N/A"
    
    # Extract features/description
    features_element = container.find("p", class_="description card-text")
    features = features_element.text if features_element else "N/A"
    
    # Extract price
    price_element = container.find("span", itemprop="price")
    price = price_element.text if price_element else "N/A"
    
    # Extract rating star
    rating_m = container.find_all("span", class_="ws-icon ws-icon-star")
    rating = len(rating_m) if rating_m else "0"
    
    # Extract review of peoples
    review_element = container.find("span", itemprop="reviewCount")
    review = review_element.text if review_element else "0"



    mobiles.append({"Mobile":title,
                   "Features":features,
                   "price":price,
                   "Rating":rating,
                   "Review":review
                   })

#print(mobiles)  # for checking purpose

# convert data into DataFrame
df = pd.DataFrame(mobiles)



# now we will save the file as the csv
filename = "mobile.csv"
file = df.to_csv(filename, index= False)
print(file)
print("the file is download sucessfully")