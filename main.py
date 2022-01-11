#!/usr/bin/env python3

import requests
import json
import os

url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=50"

if not os.path.isdir("./nfts/"):
    os.mkdir("./nfts/")

def GetNFTS(url):
    response = requests.request("GET", url)
    json_data = response.json()
    with open('response.json', 'w') as f:
            f.write(json.dumps(json_data, indent=4 * ' '))
    if json_data and 'assets' in json_data:
        for i in range(0,50):
            # Get the Image URL
            image_url = json_data['assets'][i]['image_url']
            # Get the name and collection
            name = json_data['assets'][i]['name']
            collection_name = json_data['assets'][i]['collection']['name']
            # Get the permanent link
            perma_link = json_data['assets'][i]['permalink']
            # Get the actual image
            image = requests.get(image_url, stream = True)
            # Get the file type from response headers
            file_type = str(image.headers['Content-Type']).replace("image/", "")
            if file_type == "svg+xml": file_type = "svg"
            # File name and extension
            file_name = f"nfts/{name}_{collection_name}.{file_type}"
            # Write the contents to a file
            with open(file_name, 'wb') as f:
                f.write(image.content)
                print(f"downloaded a {name} nft from {collection_name} collection as a {file_type}")

GetNFTS(url)