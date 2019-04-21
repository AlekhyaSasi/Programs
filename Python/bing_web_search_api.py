import json
#regex import for formatting html
import re
#pretty print import to make the json print beautiful
from pprint import pprint

#enter your sunscription key here
subscription_key = " "
assert subscription_key
"""
Bing Web Search API endpoint. If you run into any authorization errors,
double-check this value against the Bing search endpoint in your Azure dashboard.

"""
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"
#the search_term is your query for which you wish to know the results for
search_term = "Waterfall"

import requests

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
"""
include metadata in the request header such as headers, authorization/subscription key, content type, cache-control , parameters
"""
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()
x = search_results.get('webPages').get('value')[1]
pprint(x) #pretty print
#printing first value in web pages
y = x.get('name')
print(y)
z = x.get('snippet')
#code to strip html tags and display only the content
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)
print (striphtml(z))
#code to obtian first video url from the response list
k = search_results.get('videos').get('value')[0]
#pprint(k)
name = k.get('description')
url = k.get('contentUrl')
print("Here's " + name + " video " + url)
