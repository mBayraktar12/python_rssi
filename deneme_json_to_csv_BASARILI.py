#!/usr/bin/env python
# coding: utf-8

# In[101]:


import csv
import json


# In[102]:


with open('df2_indent.json') as data_file:
    data = json.load(data_file)


# In[103]:


print(type(data))


# In[104]:


for i in range(len(data)):
    print(data[0]["beaconDataList"][i]["macAddress"])


# In[117]:


with open("test.csv", "w",newline='') as csvfile:
    fieldnames =["macAddress","rssi"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    for i in range(542):
        writer.writerow({"macAddress":data[0]["beaconDataList"][i]["macAddress"],"rssi":data[0]["beaconDataList"][i]["rssi"]})

