# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

data = pd.read_csv(path)

data['Gender'].replace('-','Agender', inplace= True)
gender_count= data['Gender'].value_counts()

gender_count.plot( kind ='bar', stacked= True, figsize =(10,15))

plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()

plt.pie (alignment)
plt.legend ('Character Alignment')
plt.show()


# --------------
#Code starts here

sc_df = data[['Strength', 'Combat']]
sc_covariance = sc_df.Strength.cov(sc_df.Combat)
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance/(sc_strength * sc_combat)


ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.Intelligence.cov(ic_df.Combat)
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance/(ic_combat* ic_intelligence)

print("Combat Related to pearson's strength : ", sc_pearson)
print("Combat Related to pearson's intelligence : ",ic_pearson)



# --------------
#Code starts here

total_high = data['Total'].quantile(0.99)

super_best = data[data['Total']> total_high]

#super_best.columns

super_best_names = list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here

import matplotlib.pyplot as plt

fig,(ax_1, ax_2, ax_3)= plt.subplots(1,3)

ax_1.set_title("Intelligence")
ax_1.boxplot(data['Intelligence'])


ax_2.set_title("speed")
ax_2.boxplot(data['Speed'])

ax_3.set_title("Power")
ax_3.boxplot(data['Power'])

plt.show()


