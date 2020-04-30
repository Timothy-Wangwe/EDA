#!/usr/bin/env python
# coding: utf-8

# ### Covid-19 Summary Statistics (Pie Charts)

# ##### Import 3rd party libraries

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


# ##### Set path to most current file
# _File is set according to current date_

# In[2]:


file = datetime.now().strftime("%d-%b-%Y")
path = f'Covid-19-Datasets/Covid-19-Api/Datasets/{file}.csv'


# ##### Import the data

# In[3]:


try:
    data = pd.read_csv(path, sep=',', index_col=0)
    data.head()
except FileNotFoundError:
    raise SystemExit(f'{path}\nFile in the above path does not exist.')


# ##### Create plot as function
# _Instantiate the pie plot as a function only to call it later on. This should <br>
# help with **clean** code._

# In[4]:


def visualize(country, data):
    labels = [f'Total Deaths: {TotalDeaths}',
              f'Total Recoveries: {TotalRecoveries}',
              f'Active Cases: {ActiveCases}']
    colors = ['crimson', 'forestgreen', 'tab:blue']
    
    df.plot(kind = 'pie',
            subplots = True,
            figsize = (7, 7),
            autopct = "%0.0f%%",
            shadow = True,
            explode = (0,0.05,0.05),
            labels = labels,
            colors = colors
           )
    plt.suptitle(f'{country}\n', 
                 size = 18,
                 weight = "bold",
                 color = "tab:green",
                 y = 1
                )
    plt.title(f'Covid-19 Summary\n{file} @ {TotalCases} Cases', color="teal", fontsize="12")
    plt.legend(title = f'Total Cases: {TotalCases}',
               loc = 'best', 
               bbox_to_anchor = (1, 0.75),
               markerfirst = False,
               framealpha = 0.5
              )
    plt.axis("off")
    plt.savefig(f'Images/{Name}({file})',
                format = 'svg', 
                quality = 95, 
                transparent = True, 
                bbox_inches = 'tight'
               )
    plt.show()


# ##### Prepare data and call function from above
# _Shape the data to fit the **visualize** function before calling it at the end._

# In[5]:


for count in range(data['Countries'].count()):
    country = data.iloc[count]
    Name = country[0]
    TotalCases = country[1]
    TotalDeaths = country[3]
    TotalRecoveries = country[5]
    ActiveCases = TotalCases - (TotalDeaths + TotalRecoveries)
    
    df = pd.DataFrame([TotalDeaths,TotalRecoveries, ActiveCases],
    index = ['Total Deaths', 'Total Recoveries', 'Active Cases'])
    
    if df[0][0] != 0 or df[0][1] != 0 or df[0][2] != 0:
        visualize(Name, df)
    else:
        print(f'''
        {Name} has:
        {TotalCases} Total Cases,
        {ActiveCases} Active Cases,
        {TotalDeaths} Total Deaths and
        {TotalRecoveries} Total Recoveries;
        its Visualization can therefore not be generated!!! 
        ''')


# In[ ]:




