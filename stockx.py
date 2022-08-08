from tokenize import String
from matplotlib.pyplot import title
import requests
import json
import numpy as np
# from bs4 import BeautifulSoup as bs -- not sure why bs4 is not working

shoes_array = [ 
]

#try changing proxies to bypass 403 error

#this is a function in python
def searchInput(query): 
    url = f'https://stockx.com/api/browse?_search={query}&page=1&resultsPerPage=10000&dataType=product&facetsToRetrieve[]=browseVerticals&propsToRetrieve[][]=brand&propsToRetrieve[][]=colorway&propsToRetrieve[][]=media.thumbUrl&propsToRetrieve[][]=title&propsToRetrieve[][]=productCategory&propsToRetrieve[][]=shortDescription&propsToRetrieve[][]=urlKey'
    print(url)
    #headers to bypass security
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'utf-8',
        'accept-language': 'en-US,en;q=0.9',
        'app-platform': 'Iron',
        'referer': 'https://stockx.com/',
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
    print(html)
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

    #second level functions -- require us to traverse a new array, the new array is the array above
    def createSizeData(self):
        output = self.searchShoe()
        shoeData = self.searchShoe()
        shoeSizes_array = []
        #convert to numpy
        print();
        for i in range (len(shoeData['ProductActivity'])):
            shoeSizes_array.append(float(shoeData['ProductActivity'][i]['shoeSize']))
        print(shoeSizes_array)
        #sort to remove duplicate values
        shoeSizes_array.sort(reverse=False)
        removeDuplicates(shoeSizes_array)
        skuUuid_array = []
        for i in range (len(shoeSizes_array)):
            for j in range (len(shoeData['ProductActivity'])):
                if(float((shoeData['ProductActivity'][j]['shoeSize'])) == shoeSizes_array[i]):
                    skuUuid_array.append("skuUuid: " + shoeData['ProductActivity'][j]['skuUuid'])
                    break;
        print(len(skuUuid_array))
        print(len(shoeSizes_array))
        print(skuUuid_array)
        print(shoeSizes_array)    
        def getSizeData(self):
            return shoeSizes_array
        def getSkuUuidData(self):
            return skuUuid_array
    def getSizeData_array(self):
        #searches for individual shoe data
        output = self.searchShoe()
        shoeData = self.searchShoe()
        #initiates empty array to be returned later
        shoeSizes_array = []
        #convert to numpy
        print();
        #searches through all the available 250 datapoints
        for i in range (len(shoeData['ProductActivity'])):
            #appends every single size to shoeSizes_array
            shoeSizes_array.append(float(shoeData['ProductActivity'][i]['shoeSize']))
        #resorts array in ascending order to omit duplicate values
        shoeSizes_array.sort(reverse=False)
        removeDuplicates(shoeSizes_array)
        return shoeSizes_array
    #gets Size at specific skuUuid    
    def getSizeAtSkuUuid(self, skuUuid):
        allSizeData_array = self.getAllSizeData();
        for i in range(len(self.getAllSizeData())):
            if ("skuUuid: " + skuUuid == allSizeData_array[i][1]):
                return allSizeData_array[i][0];

    def getskuUuidData_array(self):
        #same search process as earlier -- when refactoring make a function for this
        shoeData = self.searchShoe()
        shoeSizes_array = self.getSizeData_array()
        #initiates empty array to be returned later
        skuUuid_array = []
        #Loops through all different shoe sizes available for particular shoe
        for i in range (len(shoeSizes_array)):
            #Loops through all 250 datapoints available for particular shoe
            for j in range (len(shoeData['ProductActivity'])):
                #finds matching skuUuid for each shoe size to create priceHistory log later on
                if(float((shoeData['ProductActivity'][j]['shoeSize'])) == shoeSizes_array[i]):
                    #appends to SkuUuid array and traverses to next item in shoeSize_array via break statement
                    skuUuid_array.append("skuUuid: " + shoeData['ProductActivity'][j]['skuUuid'])
                    break;
        return skuUuid_array
    #input size and return skuUuid    
    def getskuUuidAtSize(self,size):
        #gets the size data array and converts the size to a string
        allSizeData_array = self.getAllSizeData();
        size = float(size)
        size = str(size)
        print(size)
        #compares with the size data array until corresponding skuUuid is found
        for i in range(len(self.getAllSizeData())):
            if(size == allSizeData_array[i][0]):
                return allSizeData_array[i][1]

    #convert both arrays to Numpy arrays to merge into a 2D array, and returns 2D array
    def getAllSizeData(self):
        sizeData_array = np.array(self.getSizeData_array())
        skuUuidData_array = np.array(self.getskuUuidData_array())
        return np.vstack((sizeData_array, skuUuidData_array)).T

    #this is for tertiary level methods, we are traversing through the 3rd level array relative to our initial search    
    def searchPriceHistory(self, size):
        skuUuid = self.getskuUuidAtSize(size)
        print(skuUuid)
        url = f'https://stockx.com/api/products/{skuUuid}/activity?limit=1000&page=1&sort=createdAt&order=DESC&state=480&currency=USD&country=US'

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

    def getPriceHistory(self, size):
        priceHistory_array = self.searchPriceHistory(size)
        return priceHistory_array

#helper functions

#removes duplicate values in array -- array must be sorted first
def removeDuplicates(arr):
    for i in range(len(arr)-1,0,-1):
        if arr[i] == arr[i-1]:
            del arr[i]
    return arr

#print(Shoe.createObjectID('f', 0), Shoe.createTitle('f', 0), Shoe.createProductCategory('f', 0), Shoe.createGender('f', 0), Shoe.createSkUuid_array(9));
shoe1 = Shoe(Shoe.createObjectID('f', 0), Shoe.createTitle('f', 0), Shoe.createProductCategory('f', 0), Shoe.createGender('f', 0));
shoes_array.append(shoe1)
print(shoe1.getGender())
#print(shoes_array)
print(shoe1.getObjectID())
print(shoe1.searchShoe())
print(shoe1.getSizeData_array())
print(shoe1.getskuUuidData_array())
print(shoe1.getAllSizeData())
print(shoe1.getSizeAtSkuUuid("81c712df-6bad-41d4-a20a-9abc13a19f11"))
print(shoe1.getskuUuidAtSize(14))
print(shoe1.searchPriceHistory(14))
print(shoe1.getPriceHistory(14))

    
'''
class ShoeSize(Shoe):
    def __init__(self, size, skuUID, priceHistory)
    def createSkUuid_array(self, index):
        print(self)
        size_array = []
        #takes sizes out of her eand ahve it extend the shoe class, then reference the shoe object
        class Size():
            def __init__(self, size, skuUID, priceHistory):
                self.size = size
                self.skuUID = skuUID
                self.priceHistory = priceHistory
            
            def createSize(self,index):
                shoeData = self.searchShoe()
                return shoeData['productActivity'][index]['shoeSize']

            def createSkuUID(self, index):
                shoeData = self.searchShoe()
                return shoeData['productActivity'][index]['skuUuid']

            def createPriceHistory(value):
                return value
        newSize = Size(Size.createSize(self, index), Size.createSkuUID(self, index), Size.createPriceHistory(9))
        size_array.append(newSize)
        return size_array
    



    
#Shoes_array.append(Shoe(search('f')))


1. Create a for loop that appends all SkUuid's to the shoe (refer to google doc on what to append)
2. Create another loop that stores the priceHistory array (Date, Price) in the skUuid object
3. Create a for loop to append all the shoes to the shoe_array
4. Now you can do the fun stuff
'''