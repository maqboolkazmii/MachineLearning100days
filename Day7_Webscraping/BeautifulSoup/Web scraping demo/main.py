# if you want to Scrape web
# - Use API
# - Html Webscraping

# Step 0
# install required libraires:
# pip intall requests ,bs4 ,html5lib

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/"

# step 1: Get the Html
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)
#Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)
#Step 3: HTML Tree Traversal
title = soup.title
#print(title)


# commonly used type of object
# Print(type(title)) #1.Tag
# print(type(title.string)) #2. Nevagational String
# print(type(soup)) #3. BeautifulSoup
# 4.Comment


#Get the title of HTML page
paras = soup.find_all('p')
#print(paras)

anchors = soup.find_all('a')
# print(anchors)

#frist element paragraph
#print(soup.find('p'))
#print(soup.find('p')['class']) #get calss of frist elemnt


#find all the element with class text-sm
#print(soup.find_all('p', class_="text-sm"))

#get the text from the tags/soup

# print(soup.find('p').get_text())
# print(soup.get_text())


#get all the anchors tags from the page
# anchors =soup.find_all('a')
# all_links = set()

# #get all the links on the page
# for link in anchors:
#     if(link.get('href')!='#'):
#         linktext = "https://codewithharry.com" +link.get('href')
#         all_links.add(link)
#         print(linktext)


#comment
markup= "<p> <!-- this is a comments --> </p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))