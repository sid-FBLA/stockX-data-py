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
    return output

def searchShoe(objectID): 
    url = f'https://stockx.com/api/products/{objectID}/activity?limit=1000&page=1&sort=createdAt&order=DESC&state=480&currency=USD&country=US'

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


class shoe():
    #self operates the same way as "this" it's not an actual 
    #each of these are methods which must be called on the respective shoe class
    def __init__(self, objectID, title, productCategory, skUuid_array):
        self.objectID = objectID
        self.title = title
        self.productCategory = productCategory
        self.skUuid_array = skUuid_array
    
    def createObjectID(query, index):
        output = searchInput(query);
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
    # Sizes: size, skuUID, priceHistory[[]]
    #[ [size, skuUID, priceHistory[[]]], [size, skuUID, priceHistory[[]]], [size, skuUID, priceHistory[[]]] ]
    class Sizes:
        def __init__(self, size, skuUID):
            self.size = size
            self.skuUID = skuUID

            


    def createSkUuid_array(self, value):
        skUuid_array = []
        shoeData = searchShoe(self.getObjectID())
        for i in shoeData.length():           
            skuUuid = shoeData[i]['skuUid']
            for item in skUuid_array.length():
                if (skUuid != )
        return value
'''
def createSkUuid_array(query, index):
    skUuid_array = []
    #find the objectID
    output = searchInput(query);
    #objectID refers to ID when searching for exact shoe
    objectIDInstance = output['Products'][index]['objectID'] 

    skUuID_array = []
    output = searchInput(query);
    #objectID refers to ID when searching for exact shoe
    skUuid = output['Products'][index]['productCategory'] '''
    
#shoes_array.append(shoe(search('Epic React')))

print(shoe.createObjectID('Epic React', 0), shoe.createTitle('Epic React', 0), shoe.createProductCategory('Epic React', 0), createSkUuid_array(9));
shoe1 = shoe(shoe.createObjectID('Epic React', 0), shoe.createTitle('Epic React', 0), shoe.createProductCategory('Epic React', 0), createSkUuid_array(9))
shoes_array.append(shoe1)
print(shoes_array)
print(shoe1.getObjectID())
print(searchShoe('db1928e3-2b2e-4c69-8024-83cd87bdce09'))
'''tasks: 
1. Create a for loop that appends all SkUuid's to the shoe (refer to google doc on what to append)
2. Create another loop that stores the priceHistory array (Date, Price) in the skUuid object
3. Create a for loop to append all the shoes to the shoe_array
4. Now you can do the fun stuff'''