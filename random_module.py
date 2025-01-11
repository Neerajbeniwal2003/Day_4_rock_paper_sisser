#so first A MODULE is use for large code which is very difficult to understand so 
#we made different MODULES to make it simple
#we can make and import module and use it in our code or program
#for example-

# import random #here random is python intergrater module
# rand_number=random.randint(1,10)
# print(rand_number)

# import my_module #this is the module from my file from Day 4 folder
# print(my_module.my_age)

# import random
# random_number_0to1=random.random()*10 #for print random number between 0 to 1 * 10
# #here random is a module ad random() is a function
# print(random_number_0to1)

#for print random float number 
# import random
# random_float_number=random.uniform(1,10)
# print(random_float_number)

#now Head or tail game
import random
random_number=random.randint(1,2)
if random_number==1:
    print("tails")
else:
    print("Heads")
print(random_number)



