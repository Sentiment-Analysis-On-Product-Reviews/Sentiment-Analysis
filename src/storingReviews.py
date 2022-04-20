# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:44:19 2022

@author: AneeshDixit
"""

from ExtractingReviews import ExtractingReviews
import pandas as pd
from bs4 import BeautifulSoup


search_query = input("Enter your product for getting reviews: ")

gettingReviews = ExtractingReviews(search_query)

data_asin = []
link = []
reviews = []

response = gettingReviews.getAmazonSearch()

# print(response)
soup = BeautifulSoup(response.content, features="lxml")
tags = {tag.name for tag in soup.find_all()}
# print(tags)
for tag in tags:

    # find all element of tag
    for i in soup.find_all(tag):

        # if tag has attribute of class
        if i.has_attr("data-asin"):

            if len(i['data-asin']) != 0:
                data_asin.append("".join(i['data-asin']))

# print(data_asin)

for i in range(2, 4):
    response = gettingReviews.searchASIN(data_asin[i])
    # print(response)
    soup = BeautifulSoup(response.content, features="lxml")
    for i in soup.findAll("a", {'data-hook': "see-all-reviews-link-foot"}):
        link.append(i['href'])

# print(link)

for j in range(len(link)):
    for k in range(25):
        response = gettingReviews.searchReviews(link[j]+'&pageNumber='+str(k))
        #response = response.text
        soup = BeautifulSoup(response.content, features="lxml")
        for i in soup.findAll("span", {'data-hook': "review-body"}):
            reviews.append(i.text)
# print(reviews)

rev = {'reviews': reviews}  # converting the reviews list into a dictionary
# converting this dictionary into a dataframe
review_data = pd.DataFrame.from_dict(rev)
review_data.to_csv('Scraping reviews.csv', index=False)

print(review_data.head())
