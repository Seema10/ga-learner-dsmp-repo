# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
path
data=np.genfromtxt(path,delimiter=',',skip_header=1)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#print(data.shape)

census=np.concatenate((data, new_record),axis=0)
print(census)


#Code starts here



# --------------
#Code starts here
age = census[:,0]
max_age= np. max(age)
min_age= np.min(age)
age_mean= np.mean(age)
age_std= np.std(age)

print("Max Age: ", max_age)
print("Min Age: ",min_age)
print("Mean Age: ",age_mean)
print("std deviatio Age: ",age_std)




# --------------
#Code starts here
race_0= census[census[:,2]==0]
#for i in range (len(census)) if census[i:2]==0]
race_1= census[census[:,2]==1]
race_2= census[census[:,2]==2]
race_3= census[census[:,2]==3]
race_4= census[census[:,2]==4]

len_0= len(race_0)
len_1= len(race_1)
len_2= len(race_2)
len_3= len(race_3)
len_4= len(race_4)

list1= [len_0,len_1,len_2,len_3,len_4]

min_citizen= min(list1)
min_index=list1.index(min_citizen)

minority_race=min_index
print(minority_race)



#print(race_0)


# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]

working_hours_sum= sum(senior_citizens[:,6])

senior_citizens_len= len(senior_citizens)

avg_working_hours=(working_hours_sum/senior_citizens_len)

print("Avg working hours: ",avg_working_hours)


# --------------
#Code starts here
high= census[census[:,1]>10]

low= census[census[:,1]<=10]

avg_pay_high=np.mean(high[:,7])

avg_pay_low= np.mean(low[:,7])

print("Avg high pay: ",avg_pay_high)
print("Avg high low: ",avg_pay_low)


