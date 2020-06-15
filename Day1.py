#print ("hello world")

'''
name = input ("best country in the world:")
print (name)
'''
'''
if (name.lower()=="china"):
    print ("-------")
    print (name + " is the best!")
elif (name == "Japan"):
    print (name + " is the 2nd best.")
else:
    print ("Nah that's not the best country.")
'''

fruits = ['apple, grannysmith, gala', 'orange, mandarin, bloodorange', 'banana, big, small', 'peach, sweet, not sweet']
for fruit in fruits:
    templist=fruit.split(",")
    print(fruit)
    print(templist)
