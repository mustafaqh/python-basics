from math import sqrt
import os
#funtcion that return the mean valu for a list's elements
def mean(lst):
    m=sum(lst)/len(lst)
    return m

#function that return the standard deviation for list's elements
def std(lst):
    x=mean(lst)
    sum=0
    for i in lst:
        sum += (i-x)**2
    std=sqrt(sum/len(lst))
    return(std)
    

#program starts
#reading the first file "file_10000integers_A.txt" 
#and return a list 
home= os.getcwd()

file_1_name="file_10000integers_A.txt"
list_1=[]
path_1=home+"/file_10000integers_A.txt"
with open (path_1,"r") as file_1:
    for line in file_1:
        n=line.split(', ')
        for ele in n:
            list_1.append(int(ele))

#reading the second file "file_10000integers_B.txt" 
# and return a list
file_2_name="file_10000integers_B.txt"
list_2=[]
path_2=home+"/file_10000integers_B.txt"
with open (path_2,"r") as file_2:
    string_2=file_2.read()
    str_lst_2=string_2.split(':')
    for s in str_lst_2:
        list_2.append(int(s))
        
#print every file's namen mean valu for integers in 
# #this file and the standard deviation. 
print(file_1_name,"\n","the mean value  = ",mean(list_1),"\n","the standard deviation = ",std(list_1))
print()
print(file_2_name,"\n","the mean value = ",mean(list_2),"\n","the standard deviation = ",std(list_2))
print




    
    


    

    
