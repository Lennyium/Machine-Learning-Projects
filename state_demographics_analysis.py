import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

states_files = glob.glob('states*.csv')

states_list = []
for state in states_files:
  df = pd.read_csv(state)
  states_list.append(df)

states = pd.concat(states_list)

print(states.columns)
print(states.dtypes)
#print(states.head())

states.Income = states['Income'].replace('[$]', '', regex=True)

states[['Men', 'Women']] = states['GenderPop'].str.split('_', expand=True)
states['Men'] = states['Men'].str.replace('M', '')
states['Women'] = states['Women'].str.replace('F', '')

states.Women = pd.to_numeric(states.Women)
states.Men = pd.to_numeric(states.Men)

print(states.head())

plt.scatter(states.Women, states.Income)
plt.xlabel('Women')
plt.ylabel('Income')
plt.show()
plt.clf()

states.Women = states.Women.fillna(states.TotalPop - states.Men)

print(states.Women)

print(states.duplicated())
states = states.drop_duplicates()

plt.scatter(states.Women, states.Income)
plt.xlabel('Women')
plt.ylabel('Income')
plt.show()
plt.clf()

print(states.columns)


states.Hispanic = states['Hispanic'].replace('%', '', regex=True)
states.White = states['White'].replace('%', '', regex=True)
states.Black = states['Black'].replace('%', '', regex=True)
states.Native = states['Native'].replace('%', '', regex=True)
states.Asian = states['Asian'].replace('%', '', regex=True)
states.Pacific = states['Pacific'].replace('%', '', regex=True)

states.Hispanic = pd.to_numeric(states['Hispanic'])
states.White = pd.to_numeric(states['White'])
states.Black = pd.to_numeric(states['Black'])
states.Native = pd.to_numeric(states['Native'])
states.Asian = pd.to_numeric(states['Asian'])
states.Pacific = pd.to_numeric(states['Pacific'])

states.Hispanic = states['Hispanic'].fillna(0)
states.White = states['White'].fillna(0)
states.Black = states['Black'].fillna(0)
states.Native = states['Native'].fillna(0)
states.Asian = states['Asian'].fillna(0)
states.Pacific = states['Pacific'].fillna(0)

labels = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']
data_list = [states.Hispanic, states.White, states.Black, states.Native, states.Asian, states.Pacific]
plt.hist(states.Hispanic, label=['Hispanic'])
plt.xlabel("Percentage of Population")
plt.ylabel("Frequency")
plt.title("Stacked Population Distributions")
plt.show()
plt.clf()

plt.hist(states.White, label=['White'])
plt.xlabel("Percentage of Population")
plt.ylabel("Frequency")
plt.title("Stacked Population Distributions")
plt.show()
plt.clf()

plt.hist(states.Black, label=['Black'])
plt.xlabel("Percentage of Population")
plt.ylabel("Frequency")
plt.title("Stacked Population Distributions")
plt.show()
plt.clf()

plt.hist(states.Native, label=['Native'])
plt.xlabel("Percentage of Population")
plt.ylabel("Frequency")
plt.title("Stacked Population Distributions")
plt.show()
plt.clf()

plt.hist(states.Asian, label=['Asian'])
plt.xlabel("Percentage of Population")
plt.ylabel("Frequency)")
plt.title("Stacked Population Distributions")
plt.show()
plt.clf()

plt.hist(states.Pacific, label=['Pacific'])
plt.xlabel("Percentage of Population")
plt.ylabel("Frequency")
plt.title("Stacked Population Distributions")
plt.show()
plt.clf()
