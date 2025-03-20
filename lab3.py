# # #program to find the numbers multiple of 5 and 7 between 1500 and 2700 inclusive

# for i in range (1499,2701):
#     if i%5==0:
#         print(i,"is a multiple of 5")
#     elif i%7==0:
#         print(i,"is a multiple of 7")    
#     else:
#         pass


# #program to convert celsius into farenheit and farenheit into celsius

# temp=float(input("Enter a temperature value in farenheit:"))

# temp=((temp-32)/9)*5

# print(temp)

# temp=float(input("Enter a temperature value in celsius:"))

# temp=temp/5*9+32

# print(temp)



# #wap to guess a number between 1 to 9

# num=int(input("enter a number between 1 to 9:"))

# if(num>=1 and num<=9):
#     print("Well guessed!")
# else:
#     while  not( num>=1 and num<=9):
#         num=int(input("enter a number between 1 to 9:"))
#     else:
#         print("Well guessed!")    

# #wap to print the following pattern using nestted for loop
# # *
# # **
# # ***
# # ****
# # *****
# # ****
# # ***
# # **
# # *

# k=0
# for i in range(9):
#     if(i<=4):
#         for j in range(i+1):
#             print("*" ,end="")
#         print("")
#     else:    
#         for j in range(i+1-(k+2)):
#             print("*",end="")
#         print("") 
#         k=k+2



#write a program that takes a workd from user and reverse it

# word=input("Enter a word:")

# word=word[::-1]
# print(word)



#write a program to tell no of odd and even numbers in the given series

# num=(1,2,3,4,5,6,7,8,9)      
# c1,c2=0,0
# for item in num:
#       if(item%2==0):
#             c1+=1
#       else:
#             c2+=1
# print("number of even digits is ",c1 ,"number of odd digits is ",c2)




##print each item and its type in list

# data=[1,2.3,1+2j,True,'w3resource',(0,-1),[5,12],{"class":"Six"}]

# for i in range(len(data)):
#       print(data[i]," of datatype ",type(data[i]))




#write a program that prints all numbers from 0 to 6 except 3 and 6

# for i in range(7):
#     if(i==3 or i==6):
#         continue
#     else:
#         print(i,end=" ")



#write a program to print fibonacci series between 0 to 50 
# 0 1 1 2 3 5 8 13 21 ...

n1=0
n2=1

print(n1,n2,end=" ")

while (n1+n2<=50):
    temp=n2
    n2=n1+n2
    n1=temp
    print(n2,end=" ") 