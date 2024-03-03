# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:22:01 2024

@author: deoka
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://jntuhaac.in/AcademicAuditCell/ViceChancellor"

   
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
        
    text = soup.find(class_ = "body_content").get_text()
    text = text.replace('\n','').replace('\t','').replace('\r','')
    part = url.rsplit('/', 1)[-1]
    name = part + ".txt"
         
    with open(name, 'w', encoding='utf-8') as file:
        file.write(text)
        
    print(text)    
    print("text file {} saved successfully".format(name))
else:
    print(f"Error: Unable to fetch content from {url}. Status code: {response.status_code}")

