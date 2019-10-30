#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import LabelEncoder
from pandas import read_csv as r_c
from sklearn.utils import resample as RS
from sklearn.model_selection import train_test_split as TTS
from sklearn.linear_model import LogisticRegression as LR 
from sklearn.metrics import accuracy_score as a_s
from sklearn.metrics import confusion_matrix as c_m
from sklearn.metrics import classification_report as c_r


# In[2]:


data_lst=r_c('/Users/jiezou/Documents/GitHub/DataMining_project/listings.csv')
data_lst.shape
data_lst.isnull().sum()


# In[3]:


data_lst.dtypes


# In[4]:


data_lst_1= data_lst.dropna(subset=['city'])
data_lst_1.to_csv('data_lst_1.csv',index=0)
data_lst_1.shape


# In[5]:


data_lst_1.city.describe() 


# In[6]:


data_lst_sf=data_lst_1[data_lst_1['city'].str.contains('San Francisco')]
data_lst_sf.to_csv('data_lst_sf.csv',index=0)
data_lst_sf.shape


# In[13]:


data_lst_cutc= data_lst_sf.drop(['listing_url','scrape_id','last_scraped','experiences_offered','thumbnail_url','medium_url','picture_url','xl_picture_url','host_url','host_name','host_location','host_acceptance_rate','host_thumbnail_url','host_picture_url','host_neighbourhood','host_listings_count','street','neighbourhood_group_cleansed','market','smart_location','country_code','country','latitude','longitude','is_location_exact','square_feet','guests_included','extra_people','minimum_minimum_nights','maximum_minimum_nights','minimum_maximum_nights','maximum_maximum_nights','minimum_nights_avg_ntm','maximum_nights_avg_ntm','calendar_updated','has_availability','availability_30','availability_60','availability_90','availability_365','calendar_last_scraped','number_of_reviews_ltm','first_review','last_review','review_scores_accuracy','requires_license','license','jurisdiction_names','is_business_travel_ready','require_guest_profile_picture','require_guest_phone_verification','calculated_host_listings_count','calculated_host_listings_count_entire_homes','calculated_host_listings_count_private_rooms','calculated_host_listings_count_shared_rooms','reviews_per_month'],1)
data_lst_cutc.to_csv('data_lst_cutc.csv',index=0)
data_lst_cutc.shape


# In[15]:


data_lst_cutc.head()


# In[16]:


data_lst_cutc.tail()

