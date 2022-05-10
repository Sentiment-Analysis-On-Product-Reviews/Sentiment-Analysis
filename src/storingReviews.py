# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:44:19 2022

@author: AneeshDixit
"""

from ExtractingReviews import ExtractingReviews
import pandas as pd
from bs4 import BeautifulSoup


class StoringReviews:
    def __init__(self):
        self.search_query = input("Enter your product for getting reviews: ")

    def storeReviews(self):

        gettingReviews = ExtractingReviews(self.search_query)

        data_asin = []
        link = []
        reviews = []

        response = gettingReviews.getAmazonSearch()

        soup = BeautifulSoup(response.content, features="lxml")
        tags = {tag.name for tag in soup.find_all()}

        for tag in tags:
            for i in soup.find_all(tag):
                if i.has_attr("data-asin"):
                    if len(i['data-asin']) != 0:
                        data_asin.append("".join(i['data-asin']))

        for i in range(2, 4):
            response = gettingReviews.searchASIN(data_asin[i])
            soup = BeautifulSoup(response.content, features="lxml")
            for i in soup.findAll("a", {'data-hook': "see-all-reviews-link-foot"}):
                link.append(i['href'])

        for j in range(len(link)):
            for k in range(15):
                response = gettingReviews.searchReviews(
                    link[j]+'&pageNumber='+str(k))
                soup = BeautifulSoup(response.content, features="lxml")
                for i in soup.findAll("span", {'data-hook': "review-body"}):
                    reviews.append(i.text)

        rev = {'reviews': reviews}
        review_data = pd.DataFrame.from_dict(rev)

        return review_data, reviews
