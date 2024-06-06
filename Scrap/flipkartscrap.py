import requests as rq
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

response = rq.get(url)

checkheader = rq.get(url,headers={'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})

# print(checkheader)

# print(response.content)

soup = BeautifulSoup(response.content,"html.parser") 

# print(soup)

all_info = soup.findAll('div',{'class': 'tUxRFH'})


# Name = soup.find('div',{'class': "KzDlHZ"})
# ProductName = Name.text.split('-')[0].strip()

# print(ProductName)

# Star = soup.find('div',{'class': 'XQDdHH'})
# StarRating = Star.text

# print(StarRating)

# extra = soup.findAll('li',{'class': 'J+igdf'})
# # print(extra)
# Processor = extra[0].text
# print(Processor)
# Ram = extra[1].text
# print(Ram)
# OS = extra[2].text
# print(OS)
# Storage = extra[3].text
# print(Storage)
# Display = extra[4].text
# print(Display)
# Warranty = extra[5].text
# print(Warranty)

# Og_price = soup.findAll('div',{'class': 'yRaY8j ZYYwLA'})

# for PriceText in Og_price:
#     OriginalPrice = PriceText.text

#     print(OriginalPrice)

# SP_Price = soup.findAll('div',{'class':'Nx9bqj _4b5DiR'})

# for SPText in SP_Price:
#     Sellingprice = SPText.text

#     print(Sellingprice)

ColumnNames = ['Product Name', 'Star Rating', 'Processor', 'RAM', 'OS', 'Storage', 'Display', 'Warranty', 'Original Price', 'Selling Price']

Laptop_List = []

for soup in all_info:
    # name
    Name = soup.find('div',{'class': "KzDlHZ"})
    ProductName = Name.text.split('-')[0].strip()

    # Stars 
    Star = soup.find('div',{'class': 'XQDdHH'})
    if Star:
     for SRating in Star:
        StarRating = SRating.text

    extra = soup.findAll('li',{'class': 'J+igdf'})
    
    # processor
    Processor = extra[0].text
    
    #RAM
    RAM = extra[1].text
    
    # OS
    OS = extra[2].text
    
    # Storage
    Storage = extra[3].text
    
    # Display
    Display = extra[4].text
    
    # Warranty
    Warranty = extra[5].text
    
    # Original Price
    Og_price = soup.findAll('div',{'class': 'yRaY8j ZYYwLA'})
    for PriceText in Og_price:
        OriginalPrice = PriceText.text

    # Selling Price
    SP_Price = soup.findAll('div',{'class':'Nx9bqj _4b5DiR'})
    for SPText in SP_Price:
        Sellingprice = SPText.text

    Laptop_List.append([ProductName,StarRating,Processor,RAM,OS,Storage,Display,Warranty,OriginalPrice,Sellingprice])

    df = pd.DataFrame(Laptop_List, columns=ColumnNames)

    print(df)   

    df.to_csv('LaptopList.csv',index = False)

