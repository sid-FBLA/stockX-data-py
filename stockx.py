import requests
import json

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

def createObjectID(query, index):
    output = searchInput(query);
    #objectID refers to ID when searching for exact shoe
    #
    return output['Products'][index]['objectID'] 

    #return output['Products'][0]['title']

def createTitle(query, index):
    output = searchInput(query);
    #objectID refers to ID when searching for exact shoe
    #
    return output['Products'][index]['title'] 

def createProductCategory(query, index):
    output = searchInput(query);
    #objectID refers to ID when searching for exact shoe
    #
    return output['Products'][index]['productCategory'] 


class shoe():
    #self operates the same way as "this" it's not an actual parameter
    def __init__(self, objectID, title, productCategory, skUuid):
        self.objectID = objectID
        self.title = title
        self.productCategory = productCategory
        self.skuUuid = skUuid

def createSkUuid(value):
    return value;
    '''skUuID_array = []
    output = searchInput(query);
    #objectID refers to ID when searching for exact shoe
    skUuid = output['Products'][index]['productCategory'] '''
    
#shoes_array.append(shoe(search('Epic React')))

print(createObjectID('Epic React', 0), createTitle('Epic React', 0), createProductCategory('Epic React', 0), createSkUuid(9));
shoes_array.append(shoe(createObjectID('Epic React', 0), createTitle('Epic React', 0), createProductCategory('Epic React', 0), createSkUuid(9)))
print(shoes_array)
