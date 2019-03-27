# -*- coding: utf-8 -*-

print("hello world")

# a = 123
# print(type(a))

# b = "123"
# print(type(b))

# c = 2
# d = 8.0
# print ("加=" + str(c + d) + "\n", "減=" + str(c - d) + "\n", "乘=" + str(
#     c * d) + "\n", "除=" + str(c / d) + "\n", "C的d次方=" + str(
#         c**d) + "\n", "無條件捨去=" + str(c // d))

# e = -9
# f = 7
# print(abs(e))
# print(max(e, f))
# print(min(e, f))

# g = input("整數一:")
# print("g=", g)

# h=input("Your name:")
# print("Your name is",h)

# i=int(input("number1:"))
# j=int(input("number2:"))
# print ("1+2=" + str(i + j)+"\n" , "1-2=" + str(i - j))

# battery = int(input("輸入電量:"))
# if battery >80:
#  print ("抓寶去囉")
# elif 30>battery:
#  print("回家ㄅ")
# else:
#  print("打場傳說對決ㄅ")

# for k in range(0,10):
#     print(k)

# m = int(input("nember1:"))
# n = int(input("nember2:"))
# for l in range(m,n):
#     print(l)

# for o in range(0,11):
#     for p in range(0,6):
#         print(o*p,end=" ")
#     print(end ="\n")


# name ="eva"
# print (name)

# 安安="ooo"
# print(安安)

# PIE =  5
# PIE=6
# print(PIE)


# p=["lynn",1,3,True]

# print (len(p))

# for i  in range (0,len(p)):
#   print (p[i])


# q=[1,3,5,7,9]
# for i in range (0,len(q)):
#     print(q[i]*q[i])
#     q[i]=q[i]*q[i]
# print(q)

# ans =25
# print ("請從1-100中猜一數字")
# for i in range(0,3):
#     guess = int(input())
#     if ans==guess :
#       print("恭喜你猜對囉")
#       break
#     elif ans<guess:
#       print("數字再小一點")
#     else
#       print("數字再大一點")
# if ans ==guess :
#     print("")
# else:
#     print("3次機會用完囉")


# r=[10,30,50,70,90]
# for grade in r :
#     print(grade,end=' ')
# print(end ="\n")

# average = sum(r)/ len (r)
# print ("平均成績"+str(average))


# for i in range(0,len(r)):
#     r[i]=r[i]**0.5*10
#     print (r[i],end=' ')
# print(end ="\n")

# new_average = sum(r)/ len (r)
# print ("新平均成績"+str(new_average))


s = ["1", 2, 3, 4, 5]
print (s[:])


people = []

for i in range(0, 10):
    i = int(input("輸入數字"))
    people.append(i)
print(people)

for q in range(0, 5):

    a = int(input("頭在哪?"))
    b = int(input("尾在哪?"))
    print("總和"+str(sum(people[a:b])))


# a = [['a','b'] , ['c','d']]
# b = ['eating' , 'sleep']
# c = 'eating'

# print("--- test 二維陣列 ---")
# for test1 in a :
#     print(test1)

# print("--- test 一維陣列 ---")
# for test1 in b :
#     print(test1)

# print("--- test 字串 ---")
# for test1 in c :
#     print(test1)
