#!/usr/bin/env python
# coding: utf-8

# In[192]:


cd Desktop


# In[193]:


import pandas as pd

# Replace 'your_file_path.xlsx' with the actual path to your Excel file
excel_file_path = 'Data Set.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path, header=None)

# Display the DataFrame to see its structure
print(df)


# In[194]:


df.head(10)


# In[195]:


rows_to_remove = [0,2,3,4,6] 
# Use drop to remove the specified rows
df_filtered = df.drop(rows_to_remove)

# Reset the index if after removing rows
df_filtered.reset_index(drop=True, inplace=True)

column_to_remove = df.columns[1]
df_final = df_filtered.drop(column_to_remove, axis=1)

# Display the DataFrame after removing column
print("\nDataFrame after removing rows:")
df_final.head()


# In[196]:


# Calculate the sum of values in the first row of df_final
sum_of_values_2019 = df_final.iloc[1,1:].sum()

# Print the sum of values in the first row
print("\nSum of values:", sum_of_values_2019)


# ## **SUM OF TOTAL DEATHS OF YEAR 2019**

# In[197]:


print(sum_of_values_2019)


# # DEATH COUNT FOR 2020

# In[198]:


cd Desktop


# In[199]:


import pandas as pd

# Specify the file path
file_path = '2020.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, header = None)

# Display the DataFrame
df.head(10)


# In[200]:


rows_to_remove = [0,2,3,4,6,7,8,9,10,11]
df_dropped = df.drop(rows_to_remove)
df_dropped.head()


# In[201]:


# Calculate the sum of values in the first row of df_final
sum_of_values_2020 = df_dropped.iloc[1,1:].sum()

# Print the sum of values in the first row
print("\nSum of values:", sum_of_values_2020)


# ## SUM TOTAL OF DEATHS FOR YEAR 2020

# In[202]:


print(sum_of_values_2020)


# # DEATH COUNT FOR 2021

# In[203]:


cd Desktop


# In[204]:


import pandas as pd

# Specify the file path
file_path = '20211.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, header = None)

# Display the DataFrame
df.head(10)


# In[205]:


row_to_remove = [0,1,2,3,5,6,7,9]
df_dropped = df.drop(row_to_remove)


# In[206]:


df_dropped = df_dropped.reset_index(drop=True)
df_dropped.head()


# In[207]:


row_to_drop = [2,3,4,5,6,7,8,9,10]
df_final = df_dropped.drop(row_to_drop)
# Reset the index after dropping rows
df_final = df_final.reset_index(drop=True)
df_final.head(2)


# In[208]:


df_final = df_final.drop(df_final.columns[1], axis=1)
df_final.head(2)


# In[209]:


# Convert columns to numeric
df_final.iloc[:, 1:] = df_final.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Calculate the sum of values
sum_of_values_2021 = df_final.iloc[1, 1:].sum()
print("Sum of values:", sum_of_values_2021)


# ## SUM TOTAL OF DEATHS FOR YEAR 2021

# In[210]:


print(sum_of_values_2021)


# # DEATH COUNT FOR 2022

# In[211]:


cd Desktop


# In[212]:


import pandas as pd

# Specify the file path
file_path = '20222.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, header = None)

# Display the DataFrame
df.head()


# In[213]:


rows_to_remove = [0,1,2,3,4,5]
df_dropped = df.drop(rows_to_remove)
df_dropped = df_dropped.reset_index(drop=True)
df_dropped.head(120)


# In[214]:


df_dropped.columns
Total_death_values = df.iloc[:, 2].tolist()
print("Values in the second column:\n", Total_death_values)
Sum_of_values_2022 = Total_death_values[7]
print("\nTotal death values:", Sum_of_values_2022)


# ## SUM TOTAL OF DEATHS FOR YEAR 2022

# In[215]:


print(Sum_of_values_2022)


# # DEATH COUNT FOR 2023

# In[216]:


cd Desktop


# In[217]:


import pandas as pd

# Specify the file path
file_path = '2023.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, header = None)

# Display the DataFrame
df.head()


# In[218]:


rows_to_remove = [0]
df_dropped = df.drop(rows_to_remove)
df_dropped.head()


# In[219]:


df_dropped.columns
Total_death_values = df.iloc[:, 2].tolist()
print("Values in the second column:\n", Total_death_values)
Sum_of_values_2023 = Total_death_values[2]
print("\nTotal death values:", Sum_of_values_2023)


# ## SUM TOTAL OF DEATHS FOR YEAR 2023

# In[220]:


print(Sum_of_values_2023)


# 

# # GRAPHS 

# ### BAR GRAPH

# In[221]:


import matplotlib.pyplot as plt
import pandas as pd

data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Total Number of Deaths': [585899, 603077, 585899, 193778, 196724]}

df = pd.DataFrame(data)

plt.barh(df['Year'], df['Total Number of Deaths'], color='skyblue')
plt.xlabel('Total Number of Deaths')
plt.ylabel('Year')
plt.title('Total Number of Deaths by Year')
plt.show()


# ### LINE GRAPH

# In[222]:


import matplotlib.pyplot as plt

data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Total Number of Deaths': [585899, 603077, 585899, 193778, 196724]}

plt.plot(data['Year'], data['Total Number of Deaths'], marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Total Number of Deaths')
plt.title('Total Number of Deaths Over the Years')
plt.grid(True)


for year, deaths in zip(data['Year'], data['Total Number of Deaths']):
    plt.text(year, deaths, f'{deaths}', ha='left', va='bottom')

plt.show()


# ### PIE CHART

# In[223]:


import matplotlib.pyplot as plt

data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Total Number of Deaths': [585899, 603077, 585899, 193778, 196724]}

plt.pie(data['Total Number of Deaths'], labels=data['Year'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.axis('equal')
plt.title('Distribution of Total Deaths by Year')

plt.show()

