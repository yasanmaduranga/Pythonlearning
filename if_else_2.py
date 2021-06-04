var1 = 1
var2 = 1
var3 = 5

if var1==var2:
    print("Hi")
else:
    print("Oh no..")

if var1==var2!=var3:
    print("yes")
else:
    print("no")


person1_name = input("What is your name ?")
person1_wallet = input("How much money do you have ?")

person2_name = input("What is your name ?")
person2_wallet = input("How much money do you have ?")

if float(person1_wallet)>float(person2_wallet):
    print(person1_name+" is recher than "+person2_name)
else: 
    print(person2_name+" is richer than "+person1_name)