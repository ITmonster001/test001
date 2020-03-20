# -*- coding:utf-8 -*-
# @Time:2020/3/16 22:28
# @Author:xuzy
# @Email:1186136511@qq.com
# @File:review.py
# @Software:PyCharm Community Edition
'''
# 异或^,二进制下相同位置的不同数值变为1，相同数值变为0，计算完毕后，在转化为10进制
arr = [21,31,4,3,2,5,6]
a = arr[0]^arr[1] # 2,3
b = arr[1]^arr[3] # 3,3
print(a,b)

# 幂次方 c的b次方
c = 2
b = 5
print(c**b)


# 赋值运算符
e = 2
f = 3
e -= f
f -= e
g = -1%4
i = 1%4
j = -5%4
print(g,i,j)
'''
# nums= [1,1,2,1,3,4,5,6,6,7]
# list_nums = []
# for i in range(len(nums)):
#     if nums[i] not in nums[i+1:]:
#         list_nums.append(nums[i])
#
# print(list_nums)
# for i in range(len(nums)):
#     if  i in nums[i+1:]: # 如果当前元素在当前位置之后仍出现
#         print("当前检查的是第{}个元素".format(i+1))
#         a = nums.count(nums[i]) # 获取该元素的重复次数
#         print("{}重复的次数为{}".format(i,a))
#         for j in range(a+1):
#             nums.remove(nums[i])
#     else:
#         pass
# print(nums)
def list_uniq(nums):
    if type(nums) is not list:
        print("传入数据非列表！")

    a = []
    b = []
    c = []
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            a.append(nums[i])
        else:
            b.append(nums[i])

    for j in range(len(b)):
        if b[j] not in a:
            c.append(b[j])
    return c

def get_repetition(nums):
    a = [] # 定义一个变量，存放重复的值，并进行最终输出
    b = {} # 定义一个字典，存放重复的值和对应的出现次数
    for i in range(len(nums)): # 遍历列表，将重复的值和重复的次数提出来，放到一个字典里面
        if nums[i] in nums[i+1:]:
            b[nums[i]] = nums.count(nums[i])

    b = sorted(b.items(),key=lambda items:items[1],reverse=True) # 对字典 根据value值进行降序排列，返回列表
    for j in range(len(b)): # 将最新列表中的每个值里面的第一个值取出来，放到一个新的列表中
        a.append(b[j][0])
    return a
# list_nums = [0,0,1,1,2,3,4,4,1,5,6,7,7,7,7,8,8,9]
# print(get_repetition(list_nums))



def login():
    name = input("请输入名字：")

    if name not in password.keys() or name == "":
        print("请输入正确的用户名")
        login()
    else:
        for i in range(1,4):
            pwd = input("请输入密码：")
            if pwd != password[name]:
                print("第{}次密码输入错误，还剩{}次输入机会".format(i,3-i))
            else:
                print("登录成功")


password = {"admin":"123321","user1":"123456"}
# login()

# def f(str,*args,**kwargs):
#     print(str,args,kwargs)
# import copy
# a= [1,2,3,4,["a","b"]]
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)

# keys = ["A","B","C"]
# values = ["1","2","3"]
# c = {}
# for i in range(len(keys)):
#         c[keys[i]] = values[i]
# print(c)
#
# num = []
# for i in range(1,1000):
#     if i%7 == 0 and i%5 == 3:
#         num.append(i)
# print(num)
def optimal():
    for a in range(1,100//5+1):
        for b in range(1,100//3+1):
            for c in range(1,200+1):
                money = a*5 + b*3 + c*0.5
                if money <= 100 and a+b+c == 100:
                    print(a,b,c)
# optimal()
#
# a = [0,1,2,3,4,5,6]
# print(a[::])
# print(a[::3])
'''
n = 7
data = [1,1,2,3,2,5,5]
def get_num(n,data):
    if  1<= n <=1000 and n%2 == 1 and len(data) == n:
        for i in data:
            if data.count(i)%2 == 1:
                return i
print(get_num(n,data))
'''
def myOrder(data,n,m):
    if n in range(len(data)) and m in range(len(data)):
        cut = sorted(data[n:m])
        return "".join(cut)


data1 = "abdfcssjjjj"
n = 0
m = 9
print(myOrder(data1,n,m))





