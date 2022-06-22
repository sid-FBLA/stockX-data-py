from tokenize import String
from matplotlib.pyplot import title
import requests
import json
import numpy as np

shoes_array = [ 
]

#this is a function in python
def searchInput(query): 
    url = f'https://stockx.com/api/browse?_search={query}&page=1&resultsPerPage=10000&dataType=product&facetsToRetrieve[]=browseVerticals&propsToRetrieve[][]=brand&propsToRetrieve[][]=colorway&propsToRetrieve[][]=media.thumbUrl&propsToRetrieve[][]=title&propsToRetrieve[][]=productCategory&propsToRetrieve[][]=shortDescription&propsToRetrieve[][]=urlKey'

    #headers to bypass security
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-US,en;q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://stockx.com/en-US',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    html = requests.get(url=url, headers=headers)
    output = json.loads(html.text)
    print(output)
    return output


class Shoe():
    #self operates the same way as "this" it's not an actual 
    #each of these are methods which must be called on the respective Shoe class
    def __init__(self, objectID, title, productCategory, gender):
        self.objectID = objectID
        self.title = title
        self.productCategory = productCategory
        self.gender = gender
    
    def createObjectID(query, index):
        output = searchInput(query);
        print(output)
        #objectID refers to ID when searching for exact shoe
        return output['Products'][index]['objectID'] 

    def getObjectID(self):
        return self.objectID

    def createTitle(query, index):
        output = searchInput(query);
        #objectID refers to ID when searching for exact shoe
        return output['Products'][index]['title'] 

    def getTitle(self):
        return self.title

    def createProductCategory(query, index):
        output = searchInput(query);
        #objectID refers to ID when searching for exact shoe
        return output['Products'][index]['productCategory'] 

    def getProductCategory(self):
        return self.productCategory

    def createGender(query, index):
        output = searchInput(query);
        #objectID refers to ID when searching for exact shoe
        name = output['Products'][index]['title'] 
        print(name)
        if 'W' in name: 
            return 'W'
        elif 'GS' in name:
            return 'Y'
        else:
            return 'M'

    def getGender(self):
        return self.gender
        
    # Sizes: size, skuUID, priceHistory[[]]
    #[ [size, skuUID, priceHistory[[]]], [size, skuUID, priceHistory[[]]], [size, skuUID, priceHistory[[]]] ]

    def searchShoe(self): 
        url = f'https://stockx.com/api/products/{self.objectID}/activity?limit=1000&page=1&sort=createdAt&order=DESC&state=480&currency=USD&country=US'

        headers = {
            'accept': 'application/json',
            'accept-encoding': 'utf-8',
            'accept-language': 'en-US,en;q=0.9',
            'app-platform': 'Iron',
            'referer': 'https://stockx.com/en-US',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        html = requests.get(url=url, headers=headers)
        output = json.loads(html.text)
        return output

shoe1 = Shoe(Shoe.createObjectID('Epic React', 0), Shoe.createTitle('Epic React', 0), Shoe.createProductCategory('Epic React', 0), Shoe.createGender('Epic React', 0))