# a function that counts and returns the number of different integers in the list 
def count_different(lst):
    myset=set(lst)    #convert to set
    n=len(myset)
    return n          #returns the number of different integers in the list 
# function that count the occurrences of every interger in the lsit
def count_occurrences(lst):
    dict={}
    for int in lst:
        if int in dict:
          dict[int] += 1
        else:
          dict[int] =1
    return dict           #return a dictionary (number and count)

#program starts
import os
home= os.getcwd()
t_1_name="file_10000integers_A.txt" #the first text name
list_1=[]
path_1=home+"/file_10000integers_A.txt"
with open (path_1,"r") as file_1:   #read the first file 
    for line in file_1:
        n=line.split(', ')
        for ele in n:
            list_1.append(int(ele))  #return a list that contain the integers in the first file

t_2_name="file_10000integers_B.txt"  #the second text name
list_2=[]
path_2=home+"/file_10000integers_B.txt"
with open (path_2,"r") as file_2:     #read the second file
    string_2=file_2.read()
    str_lst_2=string_2.split(':')
    for s in str_lst_2:
        list_2.append(int(s))         #return a list that contain all the integers in the second text

#count the number of different integer in the list 
# that contain the integers in the first file
diff_1=count_different(list_1)   
#count the number of different integer in the list 
# that contain the integers in the second file
diff_2=count_different(list_2)   
#count the occurrence of every integer int tha list
#that contain the integers from the first file
occ_1=count_occurrences(list_1)
#count the occurrence of every integer int tha list
#that contain the integers from the second file
occ_2=count_occurrences(list_2)

print("text name :",t_1_name,"\n","the number of different numbers in the text  = ",diff_1,"\n","the number of times each integer occurs the text = " ,occ_1) 
print()
print("text name :",t_2_name,"\n","the number of different number in the text = ",diff_2,"\n","the number of times each integer occurs the  text = ",occ_2)
print()

