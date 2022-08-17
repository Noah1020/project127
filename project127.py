from urllib import request
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import requests
import pandas as pd



start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(start_url)
soup = bs(page.text, "html.parser")


table = soup.find("table")


temp_list = []

table_row = table.find_all("tr")

for tr_tag in table_row:
    td = tr_tag.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)


name = []
distance = []
mass = []
radius = []

for d in range(1,len(temp_list)):
    name.append(temp_list[d][1])
    distance.append(temp_list[d][3])
    mass.append(temp_list[d][5])
    radius.append(temp_list[d][6])


df = pd.DataFrame(list(zip(name, distance, mass, radius)), columns = ["name", "distance", "mass", "radius"])
df.to_csv("stars.csv")



