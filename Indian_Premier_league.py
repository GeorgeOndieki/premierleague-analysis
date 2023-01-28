#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Exploratory Data Analysis
# This the Analysis for India Premier league


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl as xl


# In[2]:


# we begin by importing data, both match and deliveries data set


# In[3]:


df1= pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\python practise files\Indian Premier League\matches.csv")
df2=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\python practise files\Indian Premier League\deliveries.csv")


# In[151]:


df1.shape


# In[152]:


df2.shape


# In[6]:


# we can merge both datasets into one dataset with id as acommon value


# In[7]:


df=pd.merge(df1,df2, on='id')


# In[8]:


df.head()


# In[9]:


# we get to understand our data


# In[10]:


df.shape


# In[11]:


df.dtypes


# In[12]:


# we convert date from object to datetype


# In[13]:


df.insert(4,'Date',pd.to_datetime(df.date))


# In[14]:


df.drop(columns='date',inplace=True)


# In[15]:


pd.options.display.max_columns = None


# In[16]:


df.head()


# In[17]:


# (1) As a sport analyst find out the most successful teams,players.


# In[18]:


# lets find the team which has won the league most


# In[65]:


B=df1.winner.value_counts()
B


# In[20]:


# showing on the graph 


# In[76]:


sns.barplot(y=B.index,x=B,orient='h')


# In[153]:


print("From our analysis acompany should endorse Mumbai Indians for its products since its the best team")


# In[23]:


# lets find the best team per season


# In[71]:


group=df1.groupby('season')
team = group['winner'].apply(lambda x: x.value_counts().idxmax())
print(team)


# In[ ]:


# lets see the team which won by maximum runs


# In[122]:


df1.iloc[df1['win_by_runs'].idxmax()]['winner']


# In[115]:


print('Mumbai is the team with the best batsman')


# In[ ]:


# Lets see the team which won by maximum wickets


# In[120]:


df1.iloc[df1['win_by_wickets'].idxmax()]['winner']


# In[ ]:


# lets see the team which won by mimimum wickets


# In[132]:


df1.iloc[df1[df1['win_by_wickets'].ge(1)].win_by_wickets.idxmin()]['winner']


# In[ ]:


# lets see the team which won by minimum runs


# In[131]:


df1.iloc[df1[df1['win_by_runs'].ge(1)].win_by_runs.idxmin()]['winner']


# In[133]:


print('From our analysis Mumbai Indians won through maximum runs and minimum runs,Kolkata Knight Riders won through maximum wickets and through mimimum wickets ')


# In[ ]:


# lets find the total number of seasons played


# In[134]:


len(df.groupby('season'))


# In[135]:


# which season had the most matches


# In[161]:


plt.figure(figsize=(20,9))
sns.countplot(x='season', data=df1,order=df.season.value_counts().index)


# In[25]:


# Lets find the best 10 players of the match of all times.


# In[156]:


Best=df1['player_of_match'].value_counts().head(10)


# In[160]:


plt.figure(figsize=(20,9))
sns.barplot(x=Best.index,y=Best,data=df1)


# In[ ]:


# CH Gayle should be considered for endorsement by company wanting to promote there products since he is the best.


# In[27]:


# lets find the best players per season


# In[75]:


grouped=df1.groupby('season')
best = grouped['player_of_match'].apply(lambda x: x.value_counts().idxmax())
print(best)


# In[29]:


# (2) Find the factors contributing to a win or loss of a team


# In[31]:


#The Total number of wins each time has won against each other by "'win_by_runs'"


# In[32]:


df.pivot_table(index='batting_team',columns='bowling_team',values='win_by_runs' , aggfunc='sum')


# In[33]:


#The Total number of wins each time has won against each other by "'win_by_wickets"


# In[34]:


df.pivot_table(index='batting_team',columns='bowling_team',values= 'win_by_wickets' , aggfunc='sum')


# In[35]:


# Lets see the factors affecting a win or a loss


# In[45]:


A=df[['win_by_runs','win_by_wickets','inning','over','ball','is_super_over', 'wide_runs',
       'bye_runs', 'legbye_runs', 'noball_runs', 'penalty_runs',
       'batsman_runs', 'extra_runs',]]


# In[150]:


A.corr()


# In[ ]:


# From the correlation matrix we can conclude that there is no strong correlation between all those factors to a team winning in
#any way.


# In[154]:


print("The End!")


# In[ ]:





# In[ ]:





# In[ ]:




