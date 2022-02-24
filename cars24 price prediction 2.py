#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries
import bs4
from bs4 import BeautifulSoup
import requests
import re
import time
from datetime import datetime

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from selenium import webdriver
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


# For city Hyderabad
driver_H =webdriver.Chrome(r"D:/chromedriver.exe")
driver_H.get('https://www.cars24.com/buy-used-cars-hyderabad/?itm_source=Cars24Website&itm_medium=sticky_header')
ScrollNumber_H = 500
for i in range(1,ScrollNumber_H):
    driver_H.execute_script("window.scrollTo(1,50000000)")
    time.sleep(5)
file_H = open('cars24_Hyderabad.html', 'w', encoding='utf-8')
file_H.write(driver_H.page_source)
file_H.close()
driver_H.close()


# In[3]:


data_H = open('cars24_Hyderabad.html','r')
soup_H = BeautifulSoup(data_H, 'html.parser')


# In[4]:


# For Mumbai
driver_M =webdriver.Chrome(r"D:/chromedriver.exe")
driver_M.get('https://www.cars24.com/buy-used-car?sort=P&storeCityId=2378&pinId=400001')
ScrollNumber_M = 500
for i in range(1,ScrollNumber_M):
    driver_M.execute_script("window.scrollTo(1,50000000)")
    time.sleep(5)
file_M = open('cars24_Mumbai.html', 'w', encoding='utf-8')
file_M.write(driver_M.page_source)
file_M.close()
driver_M.close()


# In[5]:


data_M = open('cars24_Mumbai.html','r')
soup_M = BeautifulSoup(data_M, 'html.parser')


# In[6]:


# For Bangalore
driver_B =webdriver.Chrome(r"D:/chromedriver.exe")
driver_B.get('https://www.cars24.com/buy-used-car?sort=P&storeCityId=4709&pinId=560001')
ScrollNumber_B = 500
for i in range(1,ScrollNumber_B):
    driver_B.execute_script("window.scrollTo(1,50000000)")
    time.sleep(5)
file_B = open('cars24_Bangalore.html', 'w', encoding='utf-8')
file_B.write(driver_B.page_source)
file_B.close()
driver_B.close()


# In[7]:


data_B = open('cars24_Bangalore.html','r')
soup_B = BeautifulSoup(data_B, 'html.parser')


# In[8]:


# For Chennai
driver_C =webdriver.Chrome(r"D:/chromedriver.exe")
driver_C.get('https://www.cars24.com/buy-used-car?sort=P&storeCityId=5732&pinId=600001')
ScrollNumber_C = 500
for i in range(1,ScrollNumber_C):
    driver_C.execute_script("window.scrollTo(1,50000000)")
    time.sleep(5)
file_C = open('cars24_Chennai.html', 'w', encoding='utf-8')
file_C.write(driver_C.page_source)
file_C.close()
driver_C.close()


# In[9]:


data_C = open('cars24_Chennai.html','r')
soup_C = BeautifulSoup(data_C, 'html.parser')


# In[10]:


# For New Delhi
driver_D =webdriver.Chrome(r"D:/chromedriver.exe")
driver_D.get('https://www.cars24.com/buy-used-car?sort=P&storeCityId=2&pinId=110001')
ScrollNumber_D = 500
for i in range(1,ScrollNumber_D):
    driver_D.execute_script("window.scrollTo(1,50000000)")
    time.sleep(5)
file_D = open('cars24_Delhi.html', 'w', encoding='utf-8')
file_D.write(driver_D.page_source)
file_D.close()
driver_D.close()


# In[11]:


data_D = open('cars24_Delhi.html','r')
soup_D = BeautifulSoup(data_D, 'html.parser')


# In[12]:


#Storing different classes

main_div = 'col-4'
sub_div = '_1l4fi'
subsub_div = {'name':'_1jpRU','price':'_7udZZ','emi':'_2HFRN' , 'features':'bVR0c'}


# In[13]:


#Creating empty list to store all the details
name_H, name_D, name_M, name_B, name_C = [],[],[],[],[]
price_H, price_D, price_M, price_B, price_C = [],[],[],[],[]
emi_H, emi_D, emi_M, emi_B, emi_C = [],[],[],[],[]
features_H, features_D, features_M, features_B, features_C = [],[],[],[],[]
city_H, city_D, city_M, city_B, city_C = [],[],[],[],[]


# In[14]:


# creating list
name = []
price = []
emi = []
features = []
city = []


# In[15]:


soups = [soup_H, soup_D, soup_M, soup_B, soup_C]


# In[16]:


# Hyderabad
for x in soup_H.find_all('div',{'class':main_div}):
        for i in x.find_all('div',{'class':sub_div}):
    
            try:
                a = i.find('div',{'class':subsub_div['name']})
                name_H.append(a.text)
            except:
                name_H.append(np.nan)
            
            try:
                a = i.find('div',{'class':subsub_div['price']})
                price_H.append(a.text)
            except:
                price_H.append(np.nan)
        
    
            try:
                a = i.find('div',{'class':subsub_div['emi']})
                emi_H.append(a.text)
            except:
                emi_H.append(np.nan)
        
            try:
                a = i.find('ul',{'class':subsub_div['features']})
                features_H.append("\n".join([subsub_div.text for subsub_div in a]))
            except:
                features_H.append(np.nan)
            try:
                city_H.append('Hyderabad')
            except:
                city_H.append(np.nan)


# In[17]:


# Delhi          
for x in soup_D.find_all('div',{'class':main_div}):
        for i in x.find_all('div',{'class':sub_div}):
    
            try:
                a = i.find('div',{'class':subsub_div['name']})
                name_D.append(a.text)
            except:
                name_D.append(np.nan)
            
            try:
                a = i.find('div',{'class':subsub_div['price']})
                price_D.append(a.text)
            except:
                price_D.append(np.nan)
        
    
            try:
                a = i.find('div',{'class':subsub_div['emi']})
                emi_D.append(a.text)
            except:
                emi_D.append(np.nan)
        
            try:
                a = i.find('ul',{'class':subsub_div['features']})
                features_D.append("\n".join([subsub_div.text for subsub_div in a]))
            except:
                features_D.append(np.nan)
            try:
                city_D.append('Delhi')
            except:
                city_D.append(np.nan)


# In[18]:


# Mumbai         
for x in soup_M.find_all('div',{'class':main_div}):
        for i in x.find_all('div',{'class':sub_div}):
    
            try:
                a = i.find('div',{'class':subsub_div['name']})
                name_M.append(a.text)
            except:
                name_M.append(np.nan)
            
            try:
                a = i.find('div',{'class':subsub_div['price']})
                price_M.append(a.text)
            except:
                price_M.append(np.nan)
        
    
            try:
                a = i.find('div',{'class':subsub_div['emi']})
                emi_M.append(a.text)
            except:
                emi_M.append(np.nan)
        
            try:
                a = i.find('ul',{'class':subsub_div['features']})
                features_M.append("\n".join([subsub_div.text for subsub_div in a]))
            except:
                features_M.append(np.nan)
            try:
                city_M.append('Mumbai')
            except:
                city_M.append(np.nan)


# In[19]:


# Bangalore         
for x in soup_B.find_all('div',{'class':main_div}):
        for i in x.find_all('div',{'class':sub_div}):
    
            try:
                a = i.find('div',{'class':subsub_div['name']})
                name_B.append(a.text)
            except:
                name_B.append(np.nan)
            
            try:
                a = i.find('div',{'class':subsub_div['price']})
                price_B.append(a.text)
            except:
                price_B.append(np.nan)
        
    
            try:
                a = i.find('div',{'class':subsub_div['emi']})
                emi_B.append(a.text)
            except:
                emi_B.append(np.nan)
        
            try:
                a = i.find('ul',{'class':subsub_div['features']})
                features_B.append("\n".join([subsub_div.text for subsub_div in a]))
            except:
                features_B.append(np.nan)
            try:
                city_B.append('Bangalore')
            except:
                city_B.append(np.nan)


# In[20]:


# Chennai          
for x in soup_C.find_all('div',{'class':main_div}):
        for i in x.find_all('div',{'class':sub_div}):
    
            try:
                a = i.find('div',{'class':subsub_div['name']})
                name_C.append(a.text)
            except:
                name_C.append(np.nan)
            
            try:
                a = i.find('div',{'class':subsub_div['price']})
                price_C.append(a.text)
            except:
                price_C.append(np.nan)
        
    
            try:
                a = i.find('div',{'class':subsub_div['emi']})
                emi_C.append(a.text)
            except:
                emi_C.append(np.nan)
        
            try:
                a = i.find('ul',{'class':subsub_div['features']})
                features_C.append("\n".join([subsub_div.text for subsub_div in a]))
            except:
                features_C.append(np.nan)
            try:
                city_C.append('Chennai')
            except:
                city_C.append(np.nan)


# In[21]:


# storing all the elements from all the cities into single list.

name = name + name_H + name_D + name_M + name_B + name_C 
price = price + price_H + price_D + price_M + price_B + price_C
emi = emi + emi_H + emi_D + emi_M + emi_B + emi_C
features = features + features_H + features_D + features_M + features_B + features_C
city = city + city_H + city_D + city_M + city_B + city_C


# In[22]:


#Checking whether all the elements stored have same length or not.
print(len(name))
print(len(price))
print(len(emi))
print(len(features))
print(len(city))


# In[23]:


#Creating a Data Frame
df = pd.DataFrame({"Car Name":name, 'Price':price, 
                  "EMI":emi, "Features":features,"Location":city})


# In[24]:


df.head()


# #### Extracting other details using "REGULAR EXPRESSIONS"
# 

# In[25]:


regex = r'^\d+\s(\w+)\s'
df['Car Brand'] = df['Car Name'].apply(lambda x: re.compile(regex).findall(x)[0])

regex = r'^\d+\s\w+\s(.*?)\s\w+$'
df['Model'] = df['Car Name'].apply(lambda x: re.compile(regex).findall(x))

regex = r'â‚¹(.*)'
df['Price'] = df['Price'].apply(lambda x: re.compile(regex).findall(x)[0])

regex = r'^\d+'
df['Model Year'] = df['Car Name'].apply(lambda x: re.compile(regex).findall(x)[0])

regex = r'\w+$'
df['Gear'] = df['Car Name'].apply(lambda x: re.compile(regex).findall(x))

regex = r'^(.*)\skm'
df['Driven (Kms)'] = df['Features'].apply(lambda x: re.compile(regex).findall(x)[0])

regex = r'\n(\d+)\w+\sOwner\n'
df['Ownership'] = df['Features'].apply(lambda x: re.compile(regex).findall(x)[0])

regex = r'\n(.*)$'
df['Fuel'] = df['Features'].apply(lambda x: re.compile(regex).findall(x)[0])

regex = r'â‚¹(.*)/month'
df['EMI (monthly)'] = df['EMI'].apply(lambda x: re.compile(regex).findall(x)[0])


# In[26]:


df.head()


# In[27]:


#Removing unwanted columns & rearranging wanted columns
cols = ['Car Name', 'Features', 'EMI']
columns = ['Car Brand', 'Model', 'Price', 'Model Year','Location' ,'Fuel', 'Driven (Kms)', 'Gear', 'Ownership', 'EMI (monthly)']
df = df.drop(cols,axis=1)
df = df[columns]


# In[28]:


#Cleaning the format of different columns
df['Model'] = df['Model'].apply(lambda x: ''.join(x))
df['Gear']  = df['Gear'].apply(lambda x: ''.join(x))
df['Price'] = df['Price'].apply(lambda x: x.replace(',',''))
df['EMI (monthly)'] = df['EMI (monthly)'].apply(lambda x: x.replace(',',''))
df['Driven (Kms)'] = df['Driven (Kms)'].apply(lambda x: x.replace(',',''))


# In[29]:


df


# In[30]:


#Storing the DataFrame to a 'CSV' file
df.to_csv("Cars24.csv")


# In[286]:


#Loading the DataFrame
df = pd.read_csv("Cars24.csv")
df.drop('Unnamed: 0',axis=1,inplace=True)
df.head()


# In[287]:


#Removing duplicated rows
df = df.drop_duplicates(keep='first')


# In[288]:


#Finding number of "Missing / NAN" values
df.isnull().sum().sort_values(ascending=False)


# In[289]:


#Removing the rows which have missing values
columns = ['Model','Gear']
df = df.dropna(subset = columns).reset_index(drop=False)


# In[290]:


#Checking 'NAN' values after removing rows
df.isnull().sum()


# #### Analysing the Data
# ##### Names of the columns

# In[291]:


df.columns


# In[292]:


df.info()


# In[293]:


#Number of rows in a DataFrame
df.index


# In[294]:


#Checking Datatype of all columns
df.dtypes


# In[295]:


# Gathering all "Statistical Details" of different columns
df.describe(include='all')


# In[296]:


df = df.drop('index',axis=1)


# ## Analysing & Visualizing the Data
# ###### 1) Total number of cars in different Cities

# In[297]:


df.Location.unique()


# In[298]:


plt.figure(facecolor='black',figsize=(9,7))
sns.set(rc={'figure.figsize':(8,6)})
a = sns.countplot(x = 'Location',data=df,edgecolor='black',palette='coolwarm_r')
for p in a.patches:
    a.annotate(format(p.get_height(),'.1f'),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
              va='center',xytext=(0,6.5),textcoords='offset points',fontsize=14,color='gold',fontweight='bold')
plt.title("Total number of Cars in different Cities",fontsize=22,color='lightpink')
plt.xticks(rotation=0,fontsize=14,fontweight='bold',color='white')
plt.yticks(fontsize=12,fontweight='bold',color='black')
a.set_facecolor('black')
a.set_ylabel("No. of Cars", fontsize =15, color='lightgreen',fontweight='bold')
a.spines['left'].set_color('black')
a.spines['top'].set_color('black')
a.spines['bottom'].set_color('white')
a.spines['right'].set_color('black')
plt.grid(False)


# mumbai has most used cars followed by delhi&chennai

# #### 2) Percentage of cars available for sale in different cities
# 

# In[299]:


count = df['Location'].value_counts()
count = count.reset_index().rename(columns={'Location':'Count','index':'Location'})
colors = sns.set_palette('dark:salmon',5)
patches,text, pcts= plt.pie(x='Count',labels='Location',autopct='%1.0f%%',data=count,colors=colors,radius=1.5,shadow=True,
                    textprops={'fontsize': 14})
for i, patch in enumerate(patches):
    text[i].set_color(patch.get_facecolor())
plt.setp(pcts, color='snow',fontweight='bold')
plt.show()


# #### 3) No. of different Brands in all Cities
# 

# In[300]:


# checking for all the brands of car avilable in diffrent cities 
brand_count = df['Car Brand'].value_counts().sort_values(ascending=False).reset_index().rename(
    columns = {'index':'Brand','Car Brand':'Count'})


# In[301]:


plt.figure(facecolor='black',figsize=(24,16))
sns.set(rc={'figure.figsize':(22,14)})
a = sns.barplot(y ='Brand',x='Count',data=brand_count,palette='spring_r',edgecolor='black')
plt.xticks(rotation=0,fontsize=16,fontweight='bold',color='white')
plt.yticks(fontsize=16,fontweight='bold',color='white')
for p in a.patches:
    width = p.get_width()
    plt.text(60+p.get_width(),p.get_y()+0.55*p.get_height(),'{:1.1f}'.format(width),ha='center',
             va='center',fontsize=14,color='gold',fontweight='bold')
a.set_xlabel("No. of Cars", fontsize = 18,color='lightgreen')
a.set_ylabel("Brand Name", fontsize =18, color='lightgreen')
plt.title("Total number of different Brands in all Cities",fontsize=28,color='cyan')
a.set_facecolor('black')
a.spines['left'].set_color('white')
a.spines['top'].set_color('black')
a.spines['bottom'].set_color('black')
a.spines['right'].set_color('black')
plt.grid(False)


# #### 4) Average Price of all the brands
# 

# In[302]:


# checking for average price for diffrent brands
avg_price = df.groupby(by=['Car Brand'])['Price'].mean().sort_values(ascending=False).reset_index().rename(
    columns={'Price':'Avg Price'})
avg_price['Avg Price'] = avg_price['Avg Price'].astype(int)


# In[303]:


plt.figure(facecolor='black',figsize=(24,17))
sns.set(rc={'figure.figsize':(22,16)})
a = sns.barplot(y ='Car Brand',x='Avg Price',data=avg_price,palette='RdBu_r',edgecolor='none')
plt.xticks(rotation=0,fontsize=16,fontweight='bold',color='black')
plt.yticks(fontsize=16,fontweight='bold',color='gold')
for p in a.patches:
    width = p.get_width()
    plt.text(65000+p.get_width(),p.get_y()+0.55*p.get_height(),'{:1.1f}'.format(width),ha='center',
             va='center',fontsize=14,fontweight='bold',color='lightgreen')
plt.title("Average Price of all Brands",fontsize=28,color='pink')
a.set_facecolor('black')
a.spines['left'].set_color('white')
a.spines['top'].set_color('black')
a.spines['bottom'].set_color('black')
a.spines['right'].set_color('black')
plt.grid(False)


# MG and KIA have higher average even if they are affordable sagment cars bcz they are new to indian market.
# 
# Where as few like 'Fiat','Datsun','Chevrolet' has very low average resale value as it may be due to the affordablity of brand or the models of car may be very older versions

# #### 5) Total no. of different Car Brands in Hyderabad
# 

# In[304]:


hyd_city = df.loc[(df['Location'] == 'Hyderabad')]
hyd_brands = hyd_city['Car Brand'].value_counts().sort_values(ascending = False).reset_index().rename(columns={
    'Car Brand':'Count','index':'Brand'})


# In[305]:


sns.set(rc={'figure.figsize':(22,7.5)})
fig, ax = plt.subplots()
ax.set_facecolor('snow')
plt.scatter('Brand','Count',data=hyd_brands,color='k',marker='D')
plt.xticks(rotation=0,fontsize=16,fontweight='bold')
plt.yticks(fontsize=16,fontweight='bold')

plt.title("Total no. of different car brands in Hyderabad",fontsize=28,color='maroon')
plt.xlabel("Brand Name", fontsize = 18,color='darkred')
plt.ylabel("No. of Cars", fontsize =18, color='darkred')
plt.grid(False)


# 'Maruti' followed by 'Hyundai'  are available easily in Hyderabad Whereas Brands like 'ford','Mahindra' etc are least available

# #### 6) Total no. of different Car Brands in Delhi
# 

# In[306]:


delhi_city = df.loc[(df['Location'] == 'Delhi')]
delhi_brands = delhi_city['Car Brand'].value_counts().sort_values(ascending = False).reset_index().rename(columns={
    'Car Brand':'Count','index':'Brand'})


# In[307]:


sns.set(rc={'figure.figsize':(22,7.5)})
fig, ax = plt.subplots()
ax.set_facecolor('mintcream')
plt.plot('Brand','Count',data=delhi_brands,color='k')
plt.scatter('Brand','Count',data=delhi_brands,color='r',marker='D')
plt.xticks(rotation=60,fontsize=16,fontweight='bold')
plt.yticks(fontsize=16,fontweight='bold')

plt.title("Total no. of different car brands in Delhi",fontsize=28,color='maroon')
plt.xlabel("Brand Name", fontsize = 18,color='darkred')
plt.ylabel("No. of Cars", fontsize =18, color='darkred')
plt.grid(False)


# In[ ]:


'Maruti' followed by 'Hyundai'  are available easily in Delhi Whereas Brands like 'volvo','Mercedes' etc are least available


# #### 7) Total no. of different Car Brands in Mumbai
# 

# In[308]:


mumbai_city = df.loc[(df['Location'] == 'Mumbai')]
mumbai_brands = mumbai_city['Car Brand'].value_counts().sort_values(ascending = False).reset_index().rename(columns={
    'Car Brand':'Count','index':'Brand'})


# In[309]:


sns.set(rc={'figure.figsize':(22,7.5)})
a = sns.barplot(x ='Brand',y='Count',data=mumbai_brands)
plt.xticks(rotation=60,fontsize=16,fontweight='bold')
plt.yticks(fontsize=16,fontweight='bold')
for p in a.patches:
    a.annotate(format(p.get_height(),'.1f'),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
              va='center',xytext=(0,6.5),textcoords='offset points',fontsize=14,color='white')
a.set_xlabel("Brand Name", fontsize = 18,color='darkred')
a.set_ylabel("No. of Cars", fontsize =18, color='darkred')
plt.title("Total no. of different car brands in Mumbai",fontsize=28,color='maroon')
a.set_facecolor('black')
plt.grid(False)


# 'Maruti' followed by 'Hyundai'  are available easily in Mumbai Whereas Brands like 'Audi','Jaguar' etc are least available

# #### 8) Total no. of different Car Brands in Bangalore
# 

# In[310]:


bangalore_city = df.loc[(df['Location'] == 'Bangalore')]
bangalore_brands = bangalore_city['Car Brand'].value_counts().sort_values(ascending = False).reset_index().rename(columns={
    'Car Brand':'Count','index':'Brand'})


# In[311]:


sns.set(rc={'figure.figsize':(22,7.5)})
fig, ax = plt.subplots()
ax.set_facecolor('ivory')
plt.stem('Brand','Count',data=bangalore_brands)
plt.xticks(rotation=60,fontsize=16,fontweight='bold')
plt.yticks(fontsize=16,fontweight='bold')
plt.title("Total no. of different car brands in Bangalore",fontsize=28,color='maroon')
plt.xlabel("Brand Name", fontsize = 18,color='darkred')
plt.ylabel("No. of Cars", fontsize =18, color='darkred')
plt.show()


# 'Maruti' followed by 'Hyundai'  are available easily in Bangalore Whereas Brands like 'Mahindra','Datsun' etc are least available

# #### 9) Total no. of different Car Brands in Chennai
# 

# In[312]:


chennai_city = df.loc[(df['Location'] == 'Chennai')]
chennai_brands = chennai_city['Car Brand'].value_counts().sort_values(ascending = True).reset_index().rename(columns={
    'Car Brand':'Count','index':'Brand'})


# In[313]:


sns.set(rc={'figure.figsize':(22,7.5)})
a = sns.barplot(x ='Brand',y='Count',data=chennai_brands,hatch=('*'),color='k',edgecolor='none')
plt.xticks(rotation=60,fontsize=16,fontweight='bold')
plt.yticks(fontsize=16,fontweight='bold')
for p in a.patches:
    a.annotate(format(p.get_height(),'.1f'),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
              va='center',xytext=(0,8),textcoords='offset points',fontsize=14,color='black',fontweight='bold')
a.set_xlabel("Brand Name", fontsize = 18,color='white')
a.set_ylabel("No. of Cars", fontsize =18, color='white')
#plt.title("Total no. of different car brands in Chennai",fontsize=28,color='maroon')
a.set_facecolor('snow')
plt.grid(False)


# In[ ]:


'Maruti' followed by 'Hyundai'  are available easily in Chennai Whereas Brands like 'Fiat','Jeep' etc are least available


# #### 10) Number of Cars based on Fuel type in all cities
# 

# In[314]:


fuel_gear = df.groupby(by=['Fuel'])['Location'].count().sort_values(ascending=True).reset_index().rename(
    columns={'Location':'Count'})
fuel_gear


# In[315]:


sns.set(rc={'figure.figsize':(10,6)})
a = sns.barplot(x ='Fuel',y='Count',data=fuel_gear,palette='magma_r')
plt.xticks(rotation=0,fontsize=14,fontweight='bold')
plt.yticks(fontsize=14,fontweight='bold')
for p in a.patches:
    a.annotate(format(p.get_height(),'.1f'),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
              va='center',xytext=(0,6.5),textcoords='offset points',fontsize=12.6)
a.set_xlabel("Fuel Type", fontsize = 18,color='darkred')
a.set_ylabel("No. of Cars", fontsize =18, color='darkred')
plt.title("No. of Cars based on Fuel type",fontsize=22,color='maroon')
a.set_facecolor('snow')
a.spines['left'].set_color('black')
a.spines['top'].set_color('black')
a.spines['bottom'].set_color('black')
a.spines['right'].set_color('black')
plt.grid(False)


# #### 11) No. of Cars based on Fuel type in different Cities
# 

# In[316]:


fuel_location = df.groupby(by=['Location','Fuel'])['Gear'].count().reset_index().rename(
    columns={'Gear':'Count','Count':'Fuel'})
fuel_location = fuel_location.sort_values(by=['Location','Count'],ascending=True).reset_index()
fuel_location = fuel_location.drop('index',axis=1)
fuel_location


# we have PEtrol+CNG cars in delhi and mumbai only

# In[317]:


sns.set(rc={'figure.figsize':(25,10)})
a = sns.countplot(y = 'Location',hue='Fuel',data=df)
plt.xticks(rotation=0,fontsize=18,fontweight='bold')
plt.yticks(fontsize=18,fontweight='bold')
for p in a.patches:
    width = p.get_width()
    plt.text(20+p.get_width(),p.get_y()+0.55*p.get_height(),'{:1.1f}'.format(width),ha='center',va='center',fontsize=14)
a.set_xlabel("Location", fontsize = 20,color='darkred')
a.set_ylabel("No. of Cars", fontsize =20, color='darkred')
plt.title("No. of Cars based on Fuel type in different Cities",fontsize=28,color='maroon')
a.set_facecolor('aliceblue')
plt.legend(loc='lower right',title='Fuel',prop={'size': 20})
a.grid(False)


# #### 12) No. of cars in different Cities based on Model Year
# 

# In[318]:


fuel_location = df.groupby(by=['Location','Model Year'])['Gear'].count().reset_index().rename(
    columns={'Gear':'Count','Count':'Model Year'})
fuel_location = fuel_location.sort_values(by=['Location','Count'],ascending=True).reset_index()
fuel_location = fuel_location.drop('index',axis=1)


# In[319]:


sns.set(rc={'figure.figsize':(25,30)})
a = sns.countplot(y = 'Model Year',hue='Location',data=df,edgecolor='black',palette='coolwarm_r')
plt.xticks(rotation=0,fontsize=20,fontweight='bold')
plt.yticks(fontsize=20,fontweight='bold')
for p in a.patches:
    width = p.get_width()
    plt.text(7+p.get_width(),p.get_y()+0.55*p.get_height(),'{:1.1f}'.format(width),ha='center',va='center',fontsize=14,
            color='white')
a.set_ylabel("Model Year", fontsize = 24,color='darkred')
a.set_xlabel("No. of Cars", fontsize =24, color='darkred')
plt.title("No. of cars in different Cities based on Model Year",fontsize=29,color='maroon')
a.set_facecolor('black')
plt.legend(loc='upper right',title='Cities',prop={'size': 18})
a.grid(False)


# Most cars are avilable from year '2014' to '2019'

# #### 13) No. of Cars in different cities based on Gear
# 

# In[320]:


location_gear = df.groupby(by=['Location','Gear'])['Ownership'].count().reset_index().rename(
    columns={'Ownership':'Count'})
location_gear


# 'Manual' cars are easily avilable as they are almost 5 times of 'Automatic' 

# In[321]:


sns.set(rc={'figure.figsize':(10.5,6.5)})
plt.xticks(rotation=0,fontsize=13.5,fontweight='bold')
plt.yticks(fontsize=13.5,fontweight='bold')
a = sns.pointplot(x='Location',y='Count',hue='Gear',data=location_gear,palette='spring')
a.set_facecolor('black')
a.set_xlabel("Location", fontsize = 18,color='maroon')
a.set_ylabel("No. of Cars", fontsize =18, color='maroon')
plt.title("Cars in different cities based on Gear",fontsize=20,color='maroon')
plt.grid(False)


# #### 14) No. of Cars in different cities based on Ownership
# 

# In[322]:


location_owner = df.groupby(by=['Location','Ownership'])['Gear'].count().reset_index().rename(
    columns={'Gear':'Count'})
location_owner


# You can get '1st ownership' cars easily in all the citys

# In[323]:


sns.set(rc={'figure.figsize':(10.5,6.5)})
a = sns.barplot(x='Location',y='Count',data=location_owner,hue='Ownership',palette='tab10')
for p in a.patches:
    a.annotate(format(p.get_height(),'.1f'),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
              va='center',xytext=(0,6.5),textcoords='offset points',fontsize=9)
a.set_facecolor('white')
a.set_xlabel("Location", fontsize = 15,color='maroon')
a.set_ylabel("No. of Cars", fontsize =15, color='maroon')
plt.title("Cars in different cities based on Ownership",fontsize=20,color='maroon')
plt.xticks(rotation=0,fontsize=13,fontweight='bold')
plt.yticks(fontsize=13,fontweight='bold')
a.spines['left'].set_color('black')
a.spines['top'].set_color('black')
a.spines['bottom'].set_color('black')
a.spines['right'].set_color('black')
a.grid(False)


# In[324]:


df['Car Brand'].unique()


# #### 15) Average Price, EMI, Driven(Kms) based on Fuel type in Bangalore
# 

# In[325]:


models = df.groupby(by=['Location','Fuel']).mean()
models = models.astype(int)
models = models.reset_index()
bangalore = models[models['Location']=='Bangalore']
bangalore


# EMI of the cars soaly depends on the year of registration and Km driven

# In[326]:


f, axes = plt.subplots(1, 3, figsize=(18,6))
#1st plot
a = sns.barplot(x='Fuel',y='Price',data=bangalore,palette='rocket',ax =axes[0])
a.set_facecolor('azure')
a.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in a.patches:
    a.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
a.set_ylabel("Average Price", fontsize =14, color='maroon')
a.set_title("Average Price of vehicle based on Fuel", fontsize =14, color='maroon')
#2nd plot
b = sns.barplot(x='Fuel',y='Driven (Kms)',data=bangalore,palette='rocket',ax =axes[1])
b.set_facecolor('azure')
b.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in b.patches:
    b.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
b.set_ylabel("Average Driven (Kms)", fontsize =14, color='maroon')
b.set_title("Driven (Kms) of vehicle based on Fuel", fontsize =14, color='maroon')
#3rd plot
c = sns.barplot(x='Fuel',y='EMI (monthly)',data=bangalore,palette='rocket',ax =axes[2])
c.set_facecolor('azure')
c.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in c.patches:
    c.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
c.set_ylabel("Average EMI (Monthly)", fontsize =14, color='maroon')
c.set_title("Monthly EMI of vehicle based on Fuel", fontsize =14, color='maroon')
a.grid(False)
b.grid(False)
c.grid(False)


# #### 16) Average Price, EMI, Driven(Kms) based on Fuel type in Chennai
# 

# In[327]:


models = df.groupby(by=['Location','Fuel']).mean()
models = models.astype(int)
models = models.reset_index()
chennai = models[models['Location']=='Chennai']
chennai


# In[328]:


f, axes = plt.subplots(1, 3, figsize=(18,6))
#1st plot
a = sns.barplot(x='Fuel',y='Price',data=chennai,palette='Blues_d',ax =axes[0])
a.set_facecolor('mintcream')
a.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in a.patches:
    a.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
a.set_ylabel("Average Price", fontsize =14, color='maroon')
a.set_title("Average Price of vehicle based on Fuel", fontsize =14, color='maroon')
#2nd plot
b = sns.barplot(x='Fuel',y='Driven (Kms)',data=chennai,palette='Blues_d',ax =axes[1])
b.set_facecolor('mintcream')
b.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in b.patches:
    b.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
b.set_ylabel("Average Driven (Kms)", fontsize =14, color='maroon')
b.set_title("Driven (Kms) of vehicle based on Fuel", fontsize =14, color='maroon')
#3rd plot
c = sns.barplot(x='Fuel',y='EMI (monthly)',data=chennai,palette='Blues_d',ax =axes[2])
c.set_facecolor('mintcream')
c.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in c.patches:
    c.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
c.set_ylabel("Average EMI (Monthly)", fontsize =14, color='maroon')
c.set_title("Monthly EMI of vehicle based on Fuel", fontsize =14, color='maroon')
plt.tight_layout()
a.grid(False)
b.grid(False)
c.grid(False)


# #### 17) Average Price, EMI, Driven(Kms) based on Fuel type in Delhi
# 

# In[329]:


models = df.groupby(by=['Location','Fuel']).mean()
models = models.astype(int)
models = models.reset_index()
delhi = models[models['Location']=='Delhi']
delhi


# In[330]:


f, axes = plt.subplots(1, 3, figsize=(18,6))
#1st plot
a = sns.barplot(x='Fuel',y='Price',data=delhi,palette='coolwarm',ax =axes[0])
a.set_facecolor('mintcream')
a.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in a.patches:
    a.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
a.set_ylabel("Average Price", fontsize =14, color='maroon')
a.set_title("Average Price of vehicle based on Fuel", fontsize =14, color='maroon')
#2nd plot
b = sns.barplot(x='Fuel',y='Driven (Kms)',data=delhi,palette='coolwarm',ax =axes[1])
b.set_facecolor('mintcream')
b.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in b.patches:
    b.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
b.set_ylabel("Average Driven (Kms)", fontsize =14, color='maroon')
b.set_title("Driven (Kms) of vehicle based on Fuel", fontsize =14, color='maroon')
#3rd plot
c = sns.barplot(x='Fuel',y='EMI (monthly)',data=delhi,palette='coolwarm',ax =axes[2])
c.set_facecolor('mintcream')
c.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in c.patches:
    c.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
c.set_ylabel("Average EMI (Monthly)", fontsize =14, color='maroon')
c.set_title("Monthly EMI of vehicle based on Fuel", fontsize =14, color='maroon')
plt.tight_layout()
a.grid(False)
b.grid(False)
c.grid(False)


# In Delhi Driven Km , price and emi are almost similer except the driven KM of petrol cars

# #### 18) Average Price, EMI, Driven(Kms) based on Fuel type in Hyderabad
# 

# In[331]:


models = df.groupby(by=['Location','Fuel']).mean()
models = models.astype(int)
models = models.reset_index()
hyderabad = models[models['Location']=='Hyderabad']
hyderabad


# In[332]:


f, axes = plt.subplots(1, 3, figsize=(18,6))
#1st plot
a = sns.barplot(x='Fuel',y='Price',data=hyderabad,palette='viridis_r',ax =axes[0])
a.set_facecolor('mintcream')
a.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in a.patches:
    a.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
a.set_ylabel("Average Price", fontsize =14, color='maroon')
a.set_title("Average Price of vehicle based on Fuel", fontsize =14, color='maroon')
#2nd plot
b = sns.barplot(x='Fuel',y='Driven (Kms)',data=hyderabad,palette='viridis_r',ax =axes[1])
b.set_facecolor('mintcream')
b.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in b.patches:
    b.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
b.set_ylabel("Average Driven (Kms)", fontsize =14, color='maroon')
b.set_title("Driven (Kms) of vehicle based on Fuel", fontsize =14, color='maroon')
#3rd plot
c = sns.barplot(x='Fuel',y='EMI (monthly)',data=hyderabad,palette='viridis_r',ax =axes[2])
c.set_facecolor('mintcream')
c.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in c.patches:
    c.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
c.set_ylabel("Average EMI (Monthly)", fontsize =14, color='maroon')
c.set_title("Monthly EMI of vehicle based on Fuel", fontsize =14, color='maroon')
plt.tight_layout()
a.grid(False)
b.grid(False)
c.grid(False)


# #### 19) Average Price, EMI, Driven(Kms) based on Fuel type in Mumbai
# 

# In[333]:


models = df.groupby(by=['Location','Fuel']).mean()
models = models.astype(int)
models = models.reset_index()
mumbai = models[models['Location']=='Mumbai']
mumbai


# In[334]:


f, axes = plt.subplots(1, 3, figsize=(18,6))
#1st plot
a = sns.barplot(x='Fuel',y='Price',data=mumbai,palette='YlOrBr',ax =axes[0])
a.set_facecolor('mintcream')
a.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in a.patches:
    a.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
a.set_ylabel("Average Price", fontsize =14, color='maroon')
a.set_title("Average Price of vehicle based on Fuel", fontsize =14, color='maroon')
#2nd plot
b = sns.barplot(x='Fuel',y='Driven (Kms)',data=mumbai,palette='icefire',ax =axes[1])
b.set_facecolor('mintcream')
b.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in b.patches:
    b.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
b.set_ylabel("Average Driven (Kms)", fontsize =14, color='maroon')
b.set_title("Driven (Kms) of vehicle based on Fuel", fontsize =14, color='maroon')
#3rd plot
c = sns.barplot(x='Fuel',y='EMI (monthly)',data=mumbai,palette='icefire',ax =axes[2])
c.set_facecolor('mintcream')
c.set_xlabel("Fuel", fontsize = 18,color='maroon')
for p in c.patches:
    c.annotate(format(p.get_height()),(p.get_x()+p.get_width()/2.,p.get_height()),ha='center',
               va='center',xytext=(0,9),textcoords='offset points',fontsize=11.5)
c.set_ylabel("Average EMI (Monthly)", fontsize =14, color='maroon')
c.set_title("Monthly EMI of vehicle based on Fuel", fontsize =14, color='maroon')
plt.tight_layout()
a.grid(False)
b.grid(False)
c.grid(False)


# #### 20) Car with highest & lowest price in Hyderabad
# 

# In[335]:


by_model = df.groupby(by=['Location','Car Brand','Model']).median()
by_model = by_model.reset_index()
model_h = by_model[by_model["Location"]=='Hyderabad'].sort_values('Price',ascending=False)


# In[336]:


def max_min(column):
    high = model_h[column].idxmax()
    high_model = pd.DataFrame(model_h.loc[high])
    low = model_h[column].idxmin()
    low_model = pd.DataFrame(model_h.loc[low])
    high_low = pd.concat([high_model,low_model],axis=1)
    return high_low
max_min('Price')


# #### 21) Car with highest & lowest price in Delhi
# 

# In[337]:


model_d = by_model[by_model["Location"]=='Delhi'].sort_values('Price',ascending=False)


# In[338]:


def max_min(column):
    high = model_d[column].idxmax()
    high_model = pd.DataFrame(model_d.loc[high])
    low = model_d[column].idxmin()
    low_model = pd.DataFrame(model_d.loc[low])
    high_low = pd.concat([high_model,low_model],axis=1)
    return high_low
max_min('Price')


# #### 22) Car with highest & lowest price in Mumbai
# 

# In[339]:


model_m = by_model[by_model["Location"]=='Mumbai'].sort_values('Price',ascending=False)


# In[340]:


def max_min(column):
    high = model_m[column].idxmax()
    high_model = pd.DataFrame(model_m.loc[high])
    low = model_m[column].idxmin()
    low_model = pd.DataFrame(model_m.loc[low])
    high_low = pd.concat([high_model,low_model],axis=1)
    return high_low
max_min('Price')


# #### 23) Car with highest & lowest price in Bangalore
# 

# In[341]:


model_b = by_model[by_model["Location"]=='Bangalore'].sort_values('Price',ascending=False)


# In[342]:


def max_min(column):
    high = model_b[column].idxmax()
    high_model = pd.DataFrame(model_b.loc[high])
    low = model_b[column].idxmin()
    low_model = pd.DataFrame(model_b.loc[low])
    high_low = pd.concat([high_model,low_model],axis=1)
    return high_low
max_min('Price')


# #### 24) Car with highest & lowest price in Chennai
# 

# In[343]:


model_c = by_model[by_model["Location"]=='Chennai'].sort_values('Price',ascending=False)


# In[344]:


def max_min(column):
    high = model_c[column].idxmax()
    high_model = pd.DataFrame(model_c.loc[high])
    low = model_c[column].idxmin()
    low_model = pd.DataFrame(model_c.loc[low])
    high_low = pd.concat([high_model,low_model],axis=1)
    return high_low
max_min('Price')


# #### 25) High budget & Low budger car among all cities
# 

# In[345]:


price = df.sort_values(by='Price',ascending=False)


# In[346]:


def max_min(column):
    high = price[column].idxmax()
    high_model = pd.DataFrame(price.loc[high])
    low = price[column].idxmin()
    low_model = pd.DataFrame(price.loc[low])
    high_low = pd.concat([high_model,low_model],axis=1)
    return high_low
max_min('Price')


# #### 26) Comparision of car brand count in different Cities
# 

# In[347]:


by_model = df.groupby(by=['Car Brand','Location'])['Price'].count().reset_index().rename(
    columns={'Price':'Count'})
sns.set(rc={'figure.figsize':(15,6)})
a = sns.scatterplot(y='Count',x='Car Brand',hue='Location',data=by_model)

a.set_ylabel("Count", fontsize = 18,color='maroon')
a.set_xlabel("Car Brand", fontsize =18, color='maroon')
a.set_title("Car Brands count in different Cities", fontsize =20, color='maroon')
a.set_facecolor('#FFE6F5')
plt.xticks(rotation = 90,fontsize=13,color='k',fontweight='bold')
plt.yticks(fontsize=13,color='k',fontweight='bold')
a.grid(False)
plt.show()


# #### 27) Car Brand vs Average Price
# 
# 

# In[348]:


sns.set(rc={'figure.figsize':(28,10.5)})
a = sns.boxplot(x='Car Brand',y='Price',data=df,palette='bright')
a.set_xlabel("Car Brand", fontsize = 24,color='darkred')
a.set_ylabel("Average Price", fontsize =24, color='darkred')
plt.xticks(rotation=90,fontsize=20,fontweight='bold')
plt.yticks(fontsize=20,fontweight='bold')
a.set_title("Box Plot for Brand vs Average Price", fontsize =28, color='maroon')
a.set_facecolor('snow')
a.grid(False)
plt.show()


# #### 28) Heat Map for Correlation
# 

# In[349]:


sns.set(rc={'figure.figsize':(9,5)})
sns.heatmap(df.corr(),annot=True,cmap='viridis')
plt.xticks(fontsize=12,color='k',fontweight='bold')
plt.yticks(fontsize=12,color='k',fontweight='bold')
plt.show()


# <!-- ### Conclusion
# The availability of cars in 'Delhi'(2200+) is the highest among other 4 cities.
# 
# Compared to other 4 cities 'Hyderabad'(415+) has less available cars.
# 
# 'Maruti' brand cars are widely available with a count of around 2800 cars in all the cities, followed by Hyundai(1240+), Honda(449), Toyota(280+)
# 
# Most of the cars runs with 'Petrol' with a count of 3663.
# 
# High budget car among all cities:
#  **Toyota Land CruiserLC200 VX 2 PREMIUM (3495000/-), 2010 Model, available in Mumbai
# Low budget car among all cities:
#  **Maruti AltoLX (91000/-), 2008 Model, available in Delhi
# #### Hyderabad City
# 
# Most available brands - Maruti(248), Hyundai(112), Honda(17), Toyota(11), Volkswagon(9)
# 
# Cars availability - Petrol(319), Diesel(85), Petrol+CNG(9), Petrol+LPG(4)
# 
# Recent year models availability - 2016(21), 2017(47), 2018(43), 2019(30), 2020(3)
# 
# Availability based on Gear - Automatic(25), Manual(392)
# 
# High Budget car - Toyota Innova Crysta2.4 VX 8 STR (1801049/-), 2018 Model
# 
# Low Budget car - Hyundai AccentGLE (166099/-), 2008 Model
# #### Delhi City
# 
# Most available brands - Maruti(1069), Hyundai(404), Honda(173), Toyota(150), Renault(82)
# 
# Cars availability - Petrol(1122), Diesel(993), Petrol+CNG(81)
# 
# Recent year models availability - 2016(216), 2017(217), 2018(210), 2019(122), 2020(61), 2021(2)
# 
# Availability based on Gear - Automatic(182), Manual(2014)
# 
# High Budget car - Toyota Fortuner2.8 4x2 AT (2918399/-), 2018 Model
# 
# Low Budget car - Cheverlet SparkLS 1.0 (112000/-), 2010 Model
# #### Mumbai City
# 
# Most available brands - Maruti(802), Hyundai(331), Honda(176), Toyota(93), Volkswagon(84)
# 
# Cars availability - Petrol(1083), Diesel(579), Petrol+CNG(71), Petrol+LPG(1)
# 
# Recent year models availability - 2016(224), 2017(219), 2018(148), 2019(95), 2020(37)
# 
# Availability based on Gear - Automatic(258), Manual(1476)
# 
# High Budget car - Toyota Land CruiserLC200 VX 2 PREMIUM (3495000/-), 2010 Model
# 
# Low Budget car - Tata NanoXT TWIST (125000/-), 2014 Model
# #### Bangalore City
# 
# Most available brands - Maruti(378), Hyundai(228), Honda(41), Renault(29), Volkswagon(9)
# 
# Cars availability - Petrol(658), Diesel(116), Petrol+CNG(1), Petrol+LPG(5), Electric(1)
# 
# Recent year models availability - 2016(77), 2017(71), 2018(54), 2019(37), 2020(7), 2021(1)
# 
# Availability based on Gear - Automatic(70), Manual(711)
# 
# High Budget car - MG HECTORSHARP 2.0 DIESEL (1964099/-), 2019 Model
# 
# Low Budget car - Chevorlet SparkLS 1.0 (189499/-), 2009 Model
# #### Chennai City
# 
# Most available brands - Maruti(300), Hyundai(167), Honda(42), Volkswagon(23), Ford(16)
# 
# Cars availability - Petrol(481), Diesel(124), Petrol+LPG(4)
# 
# Recent year models availability - 2016(81), 2017(79), 2018(68), 2019(41), 2020(6)
# 
# Availability based on Gear - Automatic(60), Manual(549)
# 
# High Budget car - Tata HexaVaricor 400 XT (1801499/-), 2019 Model
# 
# Low Budget car - ChevorletSparkLS 1.0 (171799/-), 2011 Model
# 
# The above data in conclusion may change upon time to time because the data in the website is not static. -->

# ### Feature Engineering
# In this step of the project we will extract all the required feture for our model devlopment and convert the categorical features into numerical feature

# In[350]:


df.isnull().sum()


# In[351]:


df.info()


# In[352]:


#Droping Brand Name
df.drop('Car Brand', inplace=True, axis=1)


# In[353]:


categorial_features = df.select_dtypes(include=[np.object])
categorial_features.head()


# In[354]:


for col in categorial_features:
    print('\n%s column: '%col)
    print(df[col].value_counts())
    print('*'*20)


# In[355]:


df = df[df.Fuel != 'Petrol + CNG']


# In[356]:


df = df[df.Ownership != 'Fourth & Above ']


# In[357]:


df.columns


# In[358]:


for col in categorial_features:
    print('\n%s column: '%col)
    print(df[col].value_counts())
    print('*'*20)


# In[359]:


#applying get dummies of panda for one hot encoding 
data_new= pd.get_dummies(df,drop_first = True)


# In[360]:


data_new.head()


# In[361]:


data_new.columns


# In[362]:


data_new.head()


# In[363]:


# New shape of the data 
data_new.shape


# In[364]:


## Lets Check the correlation
# Finding correlation between Independent and dependent attributes
plt.figure(figsize = (18,18))
sns.heatmap(df.corr(), annot = True, linewidths=1,linecolor='black',fmt=' .2f' )
plt.show()


# In[365]:


new_data=data_new[['Location_Chennai','Location_Delhi','Location_Hyderabad','Location_Mumbai','Fuel_Petrol','Gear_Manual','Price','Model Year','Driven (Kms)','Ownership','EMI (monthly)']].copy()


# In[366]:


plt.figure(figsize=(20,20))
new_data.corr()['Price'].sort_values(ascending=False).drop(['Price']).plot(kind='barh',color='c')
plt.xlabel('Feature', fontsize=14)
plt.ylabel('Columns with target name', fontsize=14)
plt.title('Correlation',fontsize=18)
plt.grid(True)
plt.show()


# Here we can see Features on the Right side of the 0.0 are having positive corelation with the targat,
# and Features on the left of the 0.0 are having negative or 0 correlation.
# 
# ### Checking Outliers
# We will check the ouliers presnt in the numercal columns.

# In[367]:


new_data.columns


# In[368]:


new_data['Model Year'].plot.box()


# In[369]:


new_data['Driven (Kms)'].plot.box()


# In[370]:


new_data['Ownership'].plot.box()


# In[371]:


new_data['Price'].plot.box()


# In[372]:


new_data['EMI (monthly)'].plot.box()


# In[373]:


### Removing Outliers
from scipy.stats import zscore
z=np.abs(zscore(new_data))
np.where(z>3)


# In[374]:


df_new = new_data[(z<3).all(axis=1)]
print(new_data.shape)
print(df_new.shape)


# In[375]:


Loss_percentage=(2714-2430)/2714*100
print(Loss_percentage)


# #### loss percentage is 10% which is acceptable

# ### Checkign Skewness
# 

# In[376]:


new_data.skew()


# #### Lets remove the skewness
# 
# 

# In[377]:


new_data['Driven (Kms)'] = np.sqrt( new_data['Driven (Kms)'] )
new_data['Gear_Manual'] = np.sqrt( new_data['Gear_Manual'] )
new_data['Ownership'] = np.sqrt( new_data['Ownership'] )
new_data['Location_Hyderabad'] = np.sqrt( new_data['Location_Hyderabad'] )
new_data['EMI (monthly)'] = np.sqrt( new_data['EMI (monthly)'] )


# In[378]:


## Scaling the data Using StandardScaler
# Dividing into Feature and Target data
x=new_data.drop(['Price'],axis=1)
y=new_data['Price']


# In[379]:


x.shape


# In[380]:


y.shape


# In[381]:


from sklearn.preprocessing import StandardScaler
SDC=StandardScaler()
x=SDC.fit_transform(x)


# In[382]:


new_data.columns


# In[383]:


x=pd.DataFrame(data= x, columns=['Location_Chennai', 'Location_Delhi', 'Location_Hyderabad',
       'Location_Mumbai', 'Fuel_Petrol', 'Gear_Manual', 'Model Year',
       'Driven (Kms)', 'Ownership', 'EMI (monthly)'])


# ## VIF Calculation
# 

# In[384]:


import statsmodels.api as sm
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor


# In[385]:


def calc_vif(x):
    vif=pd.DataFrame()
    vif['variables']=x.columns
    vif['VIF FACTOR']=[variance_inflation_factor(x.values,i) for i in range(x.shape[1])]
    return(vif)


# In[386]:


calc_vif(x)


# In[387]:


from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

from sklearn.neighbors import KNeighborsRegressor

from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


# In[388]:


lr=LinearRegression()
for i in range(0, 1000):
    x_train, x_test, y_train, y_test= train_test_split(x,y,random_state= i,test_size=0.20)
    lr.fit(x_train,y_train)
    pred_train= lr.predict(x_train)
    pred_test= lr.predict(x_test)
    if round(r2_score(y_train,pred_train)*100,1)== round(r2_score(y_test,pred_test)*100,1):
        print("At Random state ", i, "The Model performing Well")
        print("At Random State", i)
        print("Training Accuracy score is",r2_score(y_train,pred_train)*100 )
        print("Testing Accuracy Score is", r2_score(y_test,pred_test)*100)


# In[389]:


x_train_b, x_test_b, y_train_b, y_test_b= train_test_split(x,y,random_state=306,test_size=0.20)


# In[390]:


lr.fit(x_train_b, y_train_b)
lr_pred=lr.predict(x_test_b)
print(r2_score(y_test_b,lr_pred))


# ## Cross Validation of Model
# 

# In[391]:


test_accuracy= r2_score(y_test_b,lr_pred)

from sklearn.model_selection import cross_val_score
for i in range(2,10):
    cv_score=cross_val_score(lr,x,y,cv=i, scoring='r2')
    cv_mean=cv_score.mean()
    print(f"At cross fold {i} the Cross Val score is {cv_mean*100} and Accuracy score is {test_accuracy*100}")


# In[392]:


print('Error:')

print('Mean Absolute Error:',mean_absolute_error(y_test_b,lr_pred))
print('Mean Squared Error:', mean_squared_error(y_test_b,lr_pred))
print('Root Mean Square Error:', np.sqrt(mean_squared_error(y_test_b,lr_pred)))


# ### 2. Lasso
# 

# In[393]:


ls=Lasso()
ls.fit(x_train_b, y_train_b)
ls.score(x_train_b, y_train_b)
ls_pred=ls.predict(x_test_b)

lsd=r2_score(y_test_b, ls_pred)
print('R2 score:', lsd*100)

rdscore= cross_val_score(ls,x,y,cv=7,scoring='r2')
lsc=rdscore.mean()
print('Cross val Score :', lsc*100)


# In[394]:


print('Error:')

print('Mean Absolute Error:',mean_absolute_error(y_test_b,ls_pred))
print('Mean Squared Error:', mean_squared_error(y_test_b,ls_pred))
print('Root Mean Square Error:', np.sqrt(mean_squared_error(y_test_b,ls_pred)))


# In[395]:


plt.figure(figsize=(8,7))
plt.scatter(x=y_test_b, y= ls_pred, color='r')
plt.plot(y_test_b,y_test_b, color='b')
plt.xlabel('Actual Price', fontsize= 14 )
plt.ylabel('predicted Price', fontsize= 18)
plt.show()


# ## 3. Ridge
# 

# In[396]:


rd= Ridge()
rd.fit(x_train_b, y_train_b)
rd.score(x_train_b, y_train_b)
rd_pred= rd.predict(x_test_b)

rds=r2_score(y_test_b, rd_pred)
print('r2 score: ', rds*100)

rdcvscore= cross_val_score(rd,x,y,cv=7, scoring='r2')
rdcv=rdcvscore.mean()
print('Cross val Score', rdcv*100)


# In[397]:


print('Error:')

print('Mean Absolute Error:',mean_absolute_error(y_test_b,rd_pred))
print('Mean Squared Error:', mean_squared_error(y_test_b,rd_pred))
print('Root Mean Square Error:', np.sqrt(mean_squared_error(y_test_b,rd_pred)))


# In[398]:


plt.figure(figsize=(8,7))
plt.scatter(x=y_test_b, y= rd_pred, color='r')
plt.plot(y_test_b,y_test_b, color='b')
plt.xlabel('Actual Price', fontsize= 14 )
plt.ylabel('predicted Price', fontsize= 18)
plt.show()


# ### 4. Decision TreeRegressor
# 

# In[399]:


dt=DecisionTreeRegressor()
dt.fit(x_train_b, y_train_b)
dt.score(x_train_b, y_train_b)
dt_pred=dt.predict(x_test_b)

dt_score=r2_score(y_test_b, dt_pred)
print('R2 Score:', dt_score*100)

dtcvscore=cross_val_score(dt,x,y,cv=7,scoring='r2')
dtcv=dtcvscore.mean()
print('Cross Val Score:', dtcv*100)


# In[400]:


print('Error:')

print('Mean Absolute Error:',mean_absolute_error(y_test_b,dt_pred))
print('Mean Squared Error:', mean_squared_error(y_test_b,dt_pred))
print('Root Mean Square Error:', np.sqrt(mean_squared_error(y_test_b,dt_pred)))


# In[401]:


plt.figure(figsize=(8,7))
plt.scatter(x=y_test_b, y= dt_pred, color='r')
plt.plot(y_test_b,y_test_b, color='b')
plt.xlabel('Actual sale', fontsize= 14 )
plt.ylabel('predicted sale', fontsize= 18)
plt.show()


# ### 5. KNeighborsRegressor
# 

# In[402]:


kn=KNeighborsRegressor()
kn.fit(x_train_b, y_train_b)
kn.score(x_train_b,y_train_b)
kn_pred=kn.predict(x_test_b)

kn_score= r2_score(y_test_b, kn_pred)
print('R2 Score: 0', kn_score*100)

kn_cvscore=cross_val_score(kn,x,y, cv=7, scoring='r2')
cv_mean=kn_cvscore.mean()
print('Cross val Score :',cv_mean*100 )


# In[403]:


print('Error:')

print('Mean Absolute Error:',mean_absolute_error(y_test_b,kn_pred))
print('Mean Squared Error:', mean_squared_error(y_test_b,kn_pred))
print('Root Mean Square Error:', np.sqrt(mean_squared_error(y_test_b,kn_pred)))


# In[404]:


plt.figure(figsize=(8,7))
plt.scatter(x=y_test_b, y= kn_pred, color='r')
plt.plot(y_test_b,y_test_b, color='b')
plt.xlabel('Actual sale', fontsize= 14 )
plt.ylabel('predicted sale', fontsize= 18)
plt.show()


# ### 6. Ensemble Techniques
# ##### RandomForestRegressor

# In[405]:


rf=RandomForestRegressor()
rf.fit(x_train_b, y_train_b)
rf.score(x_train_b,y_train_b)
rf_pred=rf.predict(x_test_b)

rf_score= r2_score(y_test_b, rf_pred)
print('R2 score:', rf_score*100)

rfcv=cross_val_score(rf,x,y, cv=7, scoring='r2')
rfcvscore=rfcv.mean()
print('Cross val Score :',rfcvscore*100 )


# In[406]:


print('Error:')

print('Mean Absolute Error:',mean_absolute_error(y_test_b,rf_pred))
print('Mean Squared Error:', mean_squared_error(y_test_b,rf_pred))
print('Root Mean Square Error:', np.sqrt(mean_squared_error(y_test_b,rf_pred)))


# In[407]:


plt.figure(figsize=(8,7))
plt.scatter(x=y_test_b, y= rf_pred, color='r')
plt.plot(y_test_b,y_test_b, color='b')
plt.xlabel('Actual sale', fontsize= 14 )
plt.ylabel('predicted sale', fontsize= 18)
plt.show()


# ##### GradientBoostingRegressor
# 

# In[408]:


from sklearn.ensemble import GradientBoostingRegressor
gb=GradientBoostingRegressor()
gb.fit(x_train_b, y_train_b)
gb.score(x_train_b,y_train_b)
gb_pred=rf.predict(x_test_b)

gb_score= r2_score(y_test_b, gb_pred)
print('R2 score:', gb_score*100)

gbcv=cross_val_score(gb,x,y, cv=7, scoring='r2')
gbcvscore=gbcv.mean()
print('Cross val Score :',gbcvscore*100 )


# In[409]:


print('Error:')

print('Mean Absolute Error:',mean_absolute_error(y_test_b,gb_pred))
print('Mean Squared Error:', mean_squared_error(y_test_b,gb_pred))
print('Root Mean Square Error:', np.sqrt(mean_squared_error(y_test_b,gb_pred)))


# In[410]:


plt.figure(figsize=(8,7))
plt.scatter(x=y_test_b, y= gb_pred, color='r')
plt.plot(y_test_b,y_test_b, color='b')
plt.xlabel('Actual sale', fontsize= 14 )
plt.ylabel('predicted sale', fontsize= 18)
plt.show()


# ### Lets Try Hyper Parameter Tuning
# ### We will try Hyper parameter Tuning on KNeighborsRegressor, RandomForestRegressor, GradientBoostingRegressor

# In[411]:


from sklearn.model_selection import GridSearchCV
parameters={'n_neighbors':[1,2,3,5,6,7,8,9,10,15],'weights':['uniform', 'distance'], 'algorithm':['auto','ball_tree','kd_tree'],'leaf_size':[10,20,30,40,50] }
kn=KNeighborsRegressor()
knclf=GridSearchCV(kn,parameters)
knclf.fit(x_train_b, y_train_b)
print(knclf.best_params_)


# In[412]:


kn=KNeighborsRegressor(algorithm='ball_tree', n_neighbors=5, weights='distance', leaf_size=30)
kn.fit(x_train_b, y_train_b)
kn.score(x_train_b,y_train_b)
kn_pred=kn.predict(x_test_b)

kn_score= r2_score(y_test_b, kn_pred)
print('R2 Score: ', kn_score*100)

kn_cvscore=cross_val_score(kn,x,y, cv=7)
cv_mean=kn_cvscore.mean()
print('Cross val Score :',cv_mean*100 )


# In[413]:


# Random Forest
from sklearn.model_selection import GridSearchCV
parameters={'criterion':['mse', 'mae'],'max_features':['auto', 'sqrt', 'log2'],'n_estimators':[10,20,30,70, 100], 'min_samples_split':[1,2,3,4,10]}
rf=RandomForestRegressor()
rfclf=GridSearchCV(rf, param_grid=parameters, n_jobs=-1)
rfclf.fit(x_train_b, y_train_b)
print(rfclf.best_params_)


# In[414]:


rf=RandomForestRegressor(criterion='mse', max_features='auto', min_samples_split=4, n_estimators=100)
rf.fit(x_train_b, y_train_b)
rf.score(x_train_b,y_train_b)
rf_pred=rf.predict(x_test_b)

rf_score= r2_score(y_test_b, rf_pred)
print('R2 score:', rf_score*100)

rfcv=cross_val_score(rf,x,y, cv=7, scoring='r2')
rfcvscore=rfcv.mean()
print('Cross val Score :',rfcvscore*100 )


# #### GradientBoostingRegressor hyper parameter tuning.
# 

# In[415]:


from sklearn.ensemble import GradientBoostingRegressor
parameters={'loss':['lad', 'huber'],'criterion':['friedman_mse', 'mae'], 'learning_rate':[0.001,0.01,0.1], 'n_estimators':[10,20,100]}
gb=GradientBoostingRegressor()
gbclf=GridSearchCV(gb, param_grid=parameters, n_jobs=-1)
gbclf.fit(x_train_b, y_train_b)
print(gbclf.best_params_)


# In[416]:


gb=GradientBoostingRegressor(criterion='friedman_mse',learning_rate=0.1, loss='huber', n_estimators= 100)
gb.fit(x_train_b, y_train_b)
gb.score(x_train_b,y_train_b)
gb_pred=rf.predict(x_test_b)

gb_score= r2_score(y_test_b, rf_pred)
print('R2 score:', gb_score*100)

gbcv=cross_val_score(gb,x,y, cv=7, scoring='r2')
gbcvscore=gbcv.mean()
print('Cross val Score :',gbcvscore*100 )


# In[417]:


import pickle
filename='Car_Price_Prediction.pkl'
pickle.dump(kn,open(filename,'wb'))


# In[422]:


import numpy as np
a=np.array(y_test_b)
predicted= np.array(dt.predict(x_test_b))
df_com= pd.DataFrame({'original':a, 'predicted':predicted}, index= range(len(a)))
df_com


# In[ ]:





# In[ ]:




