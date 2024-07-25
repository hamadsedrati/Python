"""
###################
for i in range(0, 201):
    print(i)
    if i == 100:
        print("It's 100!")
        break
##################


###################
#when to use try except?

user input
sockets
file handling (opening, writing, reading)
requests
reading from list
import
proxies
###################


#####################
myinfo = {
    "myscore": 100,
    "myname": "hatim",
    "universty": "UCD"
}

keys = myinfo.keys()

for i in keys:
    print(myinfo[i])
########################




import requests

image_url = input("Enter the image URL: ")
extension = image_url.split(".")[-1]
image_name = input("Enter the image name: ")+"."+extension
path = input("Where do you want to save the file? (full path): ")


response = requests.get(image_url)

with open(f"{path}{image_name}", "wb") as image:
    image.write(response.content)
"""




