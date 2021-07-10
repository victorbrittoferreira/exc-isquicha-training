## a trick to reverse a string

#x = 'atecubanos'
 
#print (x[::-1])


#x = 'Hello world'
#y = 'Hi this is a string'
## slice
#print (x[8])

## upper case
#print(x.upper())

## create a list
#print(x.split())

## create another list, but considering a paremetter
#print(y.split('i'))

## ways to format a string in

#1
#print ('The {0} {1} {2}'. format ('fox', 'brown', 'quick'))

#2
#print ('The {f} {f} {f}'. format (f = 'fox', b = 'brown', q = 'quick'))

#3
#animal = "fox"
#print ('The {a} {a} {a}'. format (a = animal))

#4
#result = 13.5534534
#print('Resultado {r: 5.2f}'.format (r = result))

## %s  another way inject string into print statement 
#print("Resultado  %s " %' foi esse')

#multiple itens
#print("Resultado  %s e %s" %('A', 'B'))
 
# like math = theres a equality parallel = signal
#a , b = 'A' , 'B'
#print("Resultado  %s e %s" %( b, a ))


### FIRST ASSESTMENT

#
#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
## Print out 'e' using indexing
#s = 'hello'
#print(s[1])
#print(s[0]+s[2:])

#Reverse the string 'hello' using slicing:
#print(s[::-1])

#Reassign 'hello' in this nested list to say 'goodbye' instead:
#x[2] = 'hello'
#
#list3 = [1,2,[3,4,'hello']]
#list3[2][2] = 'goodbye'
#print(list3)

#Sort the list below:
#list4 = [5,3,4,6,1]
#print(sorted(list4)) # sorted não modifica a lista, mas só para o uso
#print(list4)

#DICTIONARIES
#
#Using keys and indexing, grab the 'hello' from the following dictionaries:
#d = {'simple_key':'hello'}
#Grab 'hello'
#print(d['simple_key'])

#d = {'k1':{'k2':'hello'}}
## Grab 'hello'
#print(d['k1']['k2'])

## Getting a little tricker
#d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
##Grab hello
#print(d['k1'][0]['nest_key'][1][0])

## This will be hard and annoying! 
#d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#print(d['k1'][2]['k2'][1]['tough'][2][0])


#Can you sort a dictionary? Why or why not?
#Nope, coz its mappings not a sequence

#TUPLES
# 
#What is the major difference between tuples and lists?
#Tuple are immutable

#How do you create a tuple?
# setting it between ()

#SETS
#
#What is unique about a set?
#This shit dont repeat the same fucking values

#Use a set to find the unique values of the list below:
#list5 = [1,2,2,33,4,4,11,22,3,3,2]
#print(set(list5)) 


## For loops

my_list = [1,2,3,4,5,6]

#for num in my_list:
#    #print(num, 'hello')
#    if num % 2 == 0:
#        print( num ,"even")
#    else:
#        print( num ,"odd")

list_sum = 0

for num in my_list:
    list_sum = list_sum + num
    
## difference between print in or out of loop is:
    ## print each sum into the end    
    print(list_sum)

# print in the end
print(list_sum)