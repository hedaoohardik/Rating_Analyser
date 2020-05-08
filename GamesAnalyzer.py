#!/usr/bin/env python
# coding: utf-8

# # Problem Statement:
# To expose the best combination for strategy games available in the AppStore in order to get a good user rating (4.0/5.0 and above).
# 
# • Perform Data Preparation by cleaning the data and removing null values.
# • Identify Which genres have higher user ratings.
# • Identify the trend of user ratings based on pricing.
# • State your inferences.
# 

# ### 1. Cleaning data and removing null values

# In[3]:


#Importing pandas package
import pandas as pd


# In[42]:


#Reading the csv file
appstore = pd.read_csv(r'E:\CLG\6th sem\ML\Minor project\appstore_games (2).csv')
appstore


# In[43]:


#Renaming Columns
appstore.rename(columns={'Average User Rating':'Average_User_Rating', 'Primary Genre':'Primary_Genre', 'User Rating Count':'User_Rating_Count', 'In-app Purchases':'In_app_Purchases'},inplace=True)
appstore.columns


# In[23]:


#Generalising the coloumns
appstore = appstore.copy()
appstore['Genres'] = appstore['Genres'].str.replace(',', '').str.replace('Games', '').str.replace('Entertainment', '').str.replace('Strategy', '') 
appstore['Genres'] = appstore['Genres'].str.split(' ').map(lambda x: ' '.join(sorted(x)))
appstore['Genres']=appstore['Genres'].str.strip()
Non_Main_Genres=appstore[~appstore.Genres.str.contains('Puzzle') &                            ~appstore.Genres.str.contains('Action') &                            ~appstore.Genres.str.contains('Family')&                            ~appstore.Genres.str.contains('Education')&                            ~appstore.Genres.str.contains('Family')&                            ~appstore.Genres.str.contains('Adventure')&                           ~appstore.Genres.str.contains('Board')&                           ~appstore.Genres.str.contains('Role')].index
appstore.drop(Non_Main_Genres , inplace=True)
appstore.loc[appstore['Genres'].str.contains('Puzzle'),'Genres'] = 'Puzzle'
appstore.loc[appstore['Genres'].str.contains('Board'),'Genres'] = 'Puzzle'
appstore.loc[appstore['Genres'].str.contains('Action'),'Genres'] = 'Action'
appstore.loc[appstore['Genres'].str.contains('Adventure'),'Genres'] = 'Adventure'
appstore.loc[appstore['Genres'].str.contains('Role'),'Genres'] = 'Adventure'
appstore.loc[appstore['Genres'].str.contains('Family'),'Genres'] = 'Family'
appstore.loc[appstore['Genres'].str.contains('Education'),'Genres'] = 'Family'
appstore.shape


# In[24]:


#Null values in Average User Rating
appstore[appstore.Average_User_Rating.isnull()]


# In[25]:


#To prevent biased rating from the developer removing the apps having user count less than 200
appstore.drop(appstore[(appstore.User_Rating_Count <= 200) ].index, inplace=True) 
appstore.shape


# In[26]:


appstore


# In[27]:


#Removing null values
final_filter=appstore.dropna(subset=['Average_User_Rating'])
final_filter


# In[19]:


#Filling the null values of Language column
final_filter["Languages"] = final_filter["Languages"].fillna('EN')
final_filter.columns


# In[21]:


#Plot showing the Number of games vs Geners after filtering
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')

sns.set_style('darkgrid')
f, axes = plt.subplots (2,1, figsize=(8,8))

#Histogram
x=['Puzzle','Action','Adventure','Family']
y = [final_filter.Genres[(final_filter['Genres']=='Puzzle')].count(),final_filter.Genres[(final_filter['Genres']=='Action')].count(),     final_filter.Genres[(final_filter['Genres']=='Adventure')].count(),final_filter.Genres[(appstore['Genres']=='Family')].count()]

vis1= sns.barplot(x,y,palette='Accent',ax=axes[0])
vis1.set(xlabel='Genres',ylabel='Number of Games')
for p in vis1.patches:
             vis1.annotate("%.f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=11, color='gray', xytext=(0, 20),
                 textcoords='offset points')


#Pie Chart
NG = [final_filter.Genres[(final_filter['Genres']=='Puzzle')].count(),final_filter.Genres[(final_filter['Genres']=='Action')].count(),     final_filter.Genres[(final_filter['Genres']=='Adventure')].count(),final_filter.Genres[(final_filter['Genres']=='Family')].count()]
G = ['Puzzle','Action','Adventure','Family']

plt.pie(NG, labels=G, startangle=90, autopct='%.1f%%')
plt.show()


plt.ioff()


# ### 2.Identify which genres have higher user ratings

# In[34]:


#Sorting on the basis of average user rating from high to low
final_filter.sort_values('Average_User_Rating', ascending=False)


# In[35]:


#Identification of Genre having the higher user rating
identify=final_filter.groupby('Genres').Average_User_Rating.mean()
identify


# The mean shows that the Action Genre has the highest Average_User_Rating

# In[ ]:





# ### 3.Identify the trends of user ratings based on price

# In[39]:


#To analyise the trend we will plot a graph 
import matplotlib.pyplot as plt


# In[40]:


#Trend of average user rating based on price
final_filter.plot(kind='scatter',x='Average_User_Rating',y='Price',color='blue')
plt.show()


# In[41]:


#Trend of User rating count on price
final_filter.plot(kind='scatter',x='User_Rating_Count',y='Price',color='red')
plt.show()


# ### 4. Inferences and Conclusions
# We basically implemented a program which shows which Genre is having the highest average user rating from the appstore by providing analysis on the main basis of average user rating, pricing and removing of null values. The analysis was carried out by the use of Pandas and matplotlib.pyplot packages. Also, we got to know the basic intuition behind the recommendation engines. Obviously, there’s a lot more to the recommendation engines than this as there are multiple features and factors which influence the recommendations and not just the ratings.

# In[ ]:




