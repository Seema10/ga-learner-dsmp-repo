# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path)

categorical_var= bank.select_dtypes(include='object')

print("Categorical Variable: \n", categorical_var)

numerical_var = bank.select_dtypes(include='number')

print("Numerical Variable: \n", numerical_var)




# code ends here


# --------------
# code starts here

banks = bank.drop(columns='Loan_ID')

print(banks.isnull().sum())

bank_mode= banks.mode

banks= banks.fillna(bank_mode)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here


import pandas as pd
import numpy as np

#banks['LoanAmount']
avg_loan_amount = banks.pivot_table(index= ['Gender','Married','Self_Employed'], values=['LoanAmount'],aggfunc= np.mean)

print("Average Loan amount of person: \n",avg_loan_amount)
# code ends here




# --------------
# code starts here

loan_approved_se = ((banks['Self_Employed']=='Yes')& (banks
['Loan_Status']=='Y')).sum()

loan_approved_nse =((banks['Self_Employed']=='No')& (banks['Loan_Status']=='Y')).sum()

Loan_Status = 614

percentage_se= (loan_approved_se*100)/Loan_Status
percentage_nse = (loan_approved_nse*100)/Loan_Status

print("Percentage of loan approval for self-employed people: ", percentage_se)
print("Percentage of loan approval for not self-employed people: ", percentage_nse)
# code ends here


# --------------
# code starts here

loan_term= banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)

big_loan_term = len(loan_term[loan_term>=25])

print (big_loan_term)


# code ends here


# --------------
# code starts here

loan_groupby= banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()

print(mean_values)



# code ends here


