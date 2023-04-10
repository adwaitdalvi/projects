#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import os


# In[45]:


file_path="D:\project\kaggle\sales\Data_Files"
file_path


# In[46]:


#list files available in directory
file_list=os.listdir(file_path)
file_list
AllSales=[f for f in file_list if f.endswith('.csv')]
AllSales


# In[47]:


#creating temp dataframe
All_Sales=pd.DataFrame()


# In[48]:


#combining multiple files int one
for file in AllSales:
    current_file=pd.read_csv(os.path.join(file_path, file))
    All_Sales=pd.concat([All_Sales, current_file])
All_Sales.to_csv('ALLSALESDATA.csv',index=False)


# In[49]:


df=pd.read_csv('ALLSALESDATA.csv')
df.head()


# In[50]:


#removing all the blank spaces in the dataset
blank_spc=pd.read_csv("ALLSALESDATA.csv", converters={'Order ID': str.strip(" "),'Product': str.strip(" "),'Quantity Ordered': str.strip(" "),'Price Each': str.strip(" "),'Order Date': str.strip(" "),'Purchase Address': str.strip(" ")})
blank_spc


# In[51]:


#Change the column name
chng_col_name = blank_spc.rename(columns={'Quantity Ordered': 'Qty', 'Price Each': 'Price Per Product'})
chng_col_name


# In[52]:


#check for the null values
Null_values=chng_col_name.isna()
Null_values


# In[53]:


#delete the rows with null values
Del_null_values=chng_col_name.dropna()
Del_null_values


# In[54]:


Sum_null_values=Del_null_values.isnull().sum()
Sum_null_values


# In[55]:


#Sumof duplicate values in dataset
Sum_null_values.duplicated().sum()


# In[56]:


#finding the duplicate values
a=Del_null_values[Del_null_values.duplicated()==True]
a


# In[57]:


#deleting the duplicate values
Del_dup_values = Del_null_values[~ Del_null_values.duplicated()]
Del_dup_values.info()
Del_dup_values.head()


# In[58]:


#listing the columns in dataset
Del_dup_values.columns


# In[59]:


#print last 5 obs
Del_dup_values.tail()


# In[60]:


#converting the column name to small case
col_name = list(Del_dup_values.columns)
col_name = [x.lower().strip() for x in col_name] 
Del_dup_values.columns = col_name
Del_dup_values.info()


# In[61]:


#Checking the unique values available in quantity ordered column
Del_dup_values['qty'].unique()


# In[62]:


#deleting the duplicate value
b = Del_dup_values[Del_dup_values['qty'] == 'Quantity Ordered']
b.head()


# In[63]:


#deleting the index with value 519
c=Del_dup_values.drop(index=519)
c


# In[64]:


#changing the datatype of the columns
c['qty']=c['qty'].astype(int)
c['price per product']=c['price per product'].astype(float)
c.info()
c.head()


# In[65]:


#recreating the index as the sequence was not correct
indexing = c.reset_index(drop=True)
indexing.head()


# In[66]:


#seperatig month from date
indexing['month']=pd.to_datetime(indexing['order date']).dt.month


# In[67]:


indexing.head()


# In[28]:


#Creating total sales column and rounding off the value with 2 decimals as imit
indexing['Total Sales']=indexing['qty']*indexing['price per product']
rounded=indexing.round(decimals=2)
rounded.head()


# In[29]:


#seperate the state from purchase address
import re
rounded['purchase address']=rounded['purchase address'].astype(str)
rounded['state']=rounded['purchase address'].str[-8: -6]
rounded.head()


# In[30]:


#What is the total number of sales in 2019?
Total_no_of_sales=rounded.groupby('order id')['order id'].count()
Total_no_of_sales


# In[31]:


#What is the annual & monthly revenue in 2019?
#annual 
Total_no_of_sales_anually=rounded['Total Sales'].sum()
Total_no_of_sales_anually


# In[32]:


#What was the best month for sales? How much was earned that month?
Total_sales_monthly=rounded.groupby('month')['Total Sales'].sum()
Total_sales_monthly


# In[33]:


sales_monthly=rounded.groupby('month')['Total Sales'].sum().reset_index()
sales_monthly


# In[34]:


import matplotlib.pyplot as plt
sales_monthly['Total_Sales'] = sales_monthly['Total Sales']/10000000
df=pd.DataFrame(sales_monthly)
df.plot(kind='bar', y='Total_Sales', x='month')
plt.title("Monthy Revenue")
plt.ylabel('Revenue (millions)')
plt.show()


# In[35]:


#Which market (state) generated the most sales on average?
rounded.groupby('state')['Total Sales'].sum().sort_values(ascending=False)


# In[36]:


#month with best sales
rounded.groupby('month')['Total Sales'].sum().sort_values(ascending=True)


# In[37]:


#product sold most
rounded.groupby('product')['product'].count().sort_values(ascending=False)


# In[38]:


rounded.groupby('order id')['order id'].count()


# In[39]:


rounded['order date']=pd.to_datetime(rounded['order date'])
rounded['Hour']=rounded['order date'].dt.hour
rounded['Minute']=rounded['order date'].dt.minute
rounded['Time']=rounded['order date'].dt.time
rounded


# In[40]:


Sales_time=rounded.groupby('Hour')['Hour'].count().sort_values(ascending=False)
Sales_time


# In[ ]:





# In[41]:


time_sales_df = rounded.groupby(['Hour'])['Total Sales'].sum().to_frame()
time_sales_df 


# In[71]:


USB_C=c.loc[c['product'] == "USB-C Charging Cable"]
USB_C.head()


# In[ ]:





# In[ ]:




