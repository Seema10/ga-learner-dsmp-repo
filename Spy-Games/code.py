# --------------
##File path for the file 
file_path 

#Code starts here


def read_file(path):
    file = open(file_path,"r")
    sentence = file.readline()
    return sentence
    file.close()

sample_message= str(read_file(file_path))
print(sample_message)
    



# --------------
#Code starts here
file_path_1
file_path_2

message_1=read_file(file_path_1)
message_2=read_file(file_path_2)

print("message1", message_1)
print("message2",message_2)

#print(int(message_2)//int(message_1))
def fuse_msg(message_a, message_b):
    quotient=int(message_b)//int(message_a)
    return str(quotient)

secret_msg_1 = fuse_msg(message_1,message_2)
print(secret_msg_1)










# --------------
#Code starts here
file_path_3

message_3 = read_file(file_path_3)

print("message 3:", message_3)

def substitute_msg(message_c):
    if message_c=='Red' :
        sub='Army General'
    if message_c=='Green':
        sub='Data Scientist'
    if message_c=='Blue':
        sub='Marine Biologist'
    return sub

secret_msg_2=substitute_msg(message_3)
print("secret msg2 :",secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

message_4 = str(read_file(file_path_4))
message_5 = str(read_file(file_path_5))

print("message 4:",message_4)
print("message 5:",message_5)

def compare_msg(message_d, message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list=[i for i in a_list if i not in b_list]
    final_msg= " ".join(c_list)
    return final_msg

secret_msg_3 = str(compare_msg(message_4, message_5))
print("secret msg3 :", secret_msg_3)
    




# --------------
#Code starts here
file_path_6
message_6= str(read_file(file_path_6))

print("message 6 :",message_6)

def extract_msg(message_f):
    a_list= message_f.split()
    #return a_list
    even_Word = lambda x : len(x)%2==0
    
    b_list= filter(even_Word,a_list)
   
    final_msg= " ".join(b_list)
    return final_msg

secret_msg_4 = extract_msg(message_6)
print("secret msg 4:",secret_msg_4)



# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg = " ".join(message_parts)

def write_file(secret_msg, path):
    file=open(path,"a+")
    file.write(secret_msg)
    
    file.close()

secret_message = write_file(secret_msg,final_path)
print("secret_msg :")


