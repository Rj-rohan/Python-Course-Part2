#                     Functions and Recursion In Python
# Block of code that performs particular task
# "def" Keyword is used in function to define name of function
# Why Use ---  To decrease Redundancy in programming file

# def Cal_Sum(a,b,c):        #Function defination a,b and c are the PARAMETRES
#     return a+b+c            #Returning value 
# Answer=Cal_Sum(1,2,3)         #Calling  1,2,3 are actual values called ARGUMENTS
# print(Answer)



# Que.1 Average of three PARAMETRES by using Functions?

# def Avg(x,y,z):
#     return (x+y+z)/3
# average=Avg(5,10,15)
# print(average)


#   Que.2 Write a program to print length of list?

# country = ["India","England","America","Japan","Germany"]
# heroes = ["Ironman","Batman","Captain america","Spiderman"]
# def length_list(list):
#     print(len(list))

# length_list(country)
# length_list(heroes)


 # Que.3 Write a program to print thr elements of a list in a single line.(list is the parameter)? 

# heroes = ["Ironman","Batman","Captain america","Spiderman"]


# def print_list(list):
#     for item in list:
#         print(item,end=" ")

# print_list(heroes)

 
#    Que.4 Write a program to find Factorial of n (n is parametre)?

# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)

# cal_fact(5)


#  Que.5  Write a program to convert USD to INR?

# def convert(usd_val):
#     inr_val=usd_val*83
#     print(usd_val,"USD =",inr_val,"INR")

# convert(10)



#   Que.6 Write a function with input a value , if inputed value is odd
#         then print "ODD"  also if even print "EVEN"

# def print_ans(x=int(input("Enter a Number: "))):
#     if(x%2==0):
#         print("EVEN")
#     else:
#         print("ODD")

# print_ans()


#               RECURSION--- When a function calls itself repeatedly

#  Que.7 write any recursive function to print numbers from 5 to 1


# def print_num(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)    # calling recursively that's called Call Stack.

# print_num(5)




#   Que.8  Write a program to calculate Factorial of a number by using recursion 

# def cal_fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*cal_fact(n-1)

# value = cal_fact(6)
# print(value)