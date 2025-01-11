# states_of_india=["delhi","mumbai","bangaluru","goa"]#this is the list
# print(states_of_india[1]) #to print a item in the list

# #to add item in the list
# states_of_india.append("odisha")
# print(states_of_india)

#to extend the list
# states_of_india.extend(["arunachal","kerela"])
# print(states_of_india)


#who will pay the bill?
# way 1
# import random
# friends=["ajeet","ritika","ayush","neeraj","karan"]
# random_number=random.randint(0,5)
# print(friends[random_number])

# way 2
# print(random.choice(friends))#here choice is a function

#Nested list -means list in the list
fruit=["apple","mango","banana","grapes"]
vegetable=["potato","cabbage","ginger"]
nested_list=[fruit,vegetable]
print(nested_list) #it will print the nested list 
#but if :-
print(nested_list[1]) #here the items are list then it will take from [fruit,vegetable]
print(nested_list[0])
print(nested_list[1][2]) #it means the we will get the item at 2 from list 1 which also behave as item in nested list
