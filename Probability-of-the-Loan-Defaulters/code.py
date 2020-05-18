# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)

fico_count = len(df['fico'])
fico_c = len(df[df['fico']>700])

p_a = fico_c/fico_count

purpose_count= len(df[df['purpose']== 'debt_consolidation'])
purpose_total_count = len(df['purpose'])

p_b = purpose_count/purpose_total_count

print("P(A) : ",p_a)
print("P(B) : ",p_b)

df1 = df[df['purpose']== 'debt_consolidation']

p_a_b = len(df1[df1['fico']>700])/len(df1)


print ("P(A|B) :", p_a_b)

if p_a_b == p_b:
    result = True
else:
    result = False

print("Independency check : ", result)
# code ends here
# code ends here




# --------------
# code starts here

df.columns

prob_lp = len(df[df['paid.back.loan']== 'Yes'])/len(df['paid.back.loan'])
prob_cs = len(df[df['credit.policy']=='Yes'])/len(df['credit.policy'])

new_df = df[df['paid.back.loan']=='Yes']

prob_pd_cs = len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)

bayes = (prob_pd_cs * prob_lp)/prob_cs

print(bayes)

# code ends here


# --------------
# code starts here

import matplotlib.pyplot as plt

df.purpose.value_counts(normalize = True).plot(kind= 'bar')

df1 = df[df['paid.back.loan']=='No']

df1.purpose.value_counts(normalize = True).plot(kind='bar')

plt.show()
# code ends here


# --------------
# code starts here
df.columns

inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

plt.hist(df['installment'])

plt.hist(df['log.annual.inc'])

plt.show()
# code ends here


