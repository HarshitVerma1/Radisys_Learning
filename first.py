# print (("%s xyz %d")%("abc",34))
# print('Hello Harshit!')
# print ("Hello","Radhe",end="\n")

# ========================================================================

# amazon_cart=['notebooks','sun glasses','toy','bag']
# amazon_cart[0]='laptops'
# my_cart=amazon_cart
# my_cart[0]='gum'
# print(amazon_cart); # ['gum', 'sun glasses', 'toy', 'bag']
# print(my_cart); # ['gum', 'sun glasses', 'toy', 'bag']

# ========================================================================

# amazon_cart=['notebooks','sun glasses','toy','bag']
# amazon_cart[0]='laptops'
# my_cart=amazon_cart[:]
# my_cart[0]='gum'
# print(amazon_cart); # ['laptops', 'sun glasses', 'toy', 'bag']
# print(my_cart); # ['gum', 'sun glasses', 'toy', 'bag']

# ========================================================================

# check_functions=['notebooks','sun glasses','toy','bag']
# print(check_functions[::-1]) # Temporary Reversed
# print(check_functions)
# check_functions.reverse() # Permanent reversed
# print(check_functions)

# ========================================================================

# print(range(1,10)) # range(1,100)
# print(list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ========================================================================

# one_char='!'
# my_lst = one_char.join(['Hi','I','am','Harshit','Verma'])
# print(my_lst) #   Hi!I!am!Harshit!Verma

# ========================================================================

# # List Unpacking
# a,b,c,*others=[8,4,7,4,23,21,56,76]
# print('a:',a,'\nb:',b,'\nc:',c,'\nothers:',others) # Output is given below
## a: 8
## b: 4
## c: 7
## others: [4, 23, 21, 56, 76]

# ========================================================================

# Dictionary
# Dict = dict([(1, 'Geeks'), (2, 'For')])
# print("\nDictionary with each item as a pair: ")
# print(Dict,'\n') # {1: 'Geeks', 2: 'For'}

# ========================================================================

# user = {'name': 'harshit verma', 'Age': 18, 'can_swim': False}
# print(user.items())
# for x in user:
#     print(x)  # prints all keys
# for x in user.keys():
#     print(x)  # prints all keys
# for x in user.values():
#     print(x)  # print all values
# for x in user.items():
#     print(x)  # All (key,values) prints


# # ========================================================================

# for i, char in enumerate('Hello'):
#     print(i, char, "\n")

# # ========================================================================

# new_lst = ['Harshit', 'aadi', 'mohit', 'radhe']
# print(list(enumerate(new_lst)))
# print(dict(enumerate(new_lst)))
# print(set(enumerate(new_lst)))


# # ========================================================================

# i = 0
# while(i < 50):
#     print(i, end=" ")
#     i += 1
# else:
#     print("else "+str(i))
# print('successfully executed!!')

# # ========================================================================

## arguments(*args) and keyword_arguments(**Kwargs)
# Rule--> def anyFunction(parameter,*args,default_parameter='hi',**Kwargs)


# def FunctionName(value, *args, **Kwargs):
#     print(args, "\n", Kwargs)
#     total, summ = 0, 0
#     for item in Kwargs.values():
#         summ += item
#     total = summ+sum(args)
#     print(total)
#     return total
# FunctionName(76, 1, 2, 3, 4, 5, num1=1, num2=2, num3=3, num4=4, num5=5)


# # ========================================================================
# ** Scope of variables

# total = 0
# def count():
#     global total
#     total += 1
#     return total
# count()
# count()
# count()
# count()
# print(count())

# # ========================================================================
# *Scope of local variable
# def outer():
#     x = "local"
#     def inner():
#         nonlocal x             # it is outer variable
#         x = "nonlocal"
#         print("innner:", x)
#     inner()
#     print("outer:", x)
# outer()

# ========================================================================
