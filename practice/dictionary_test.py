


mylist = {1, 2, 3, 4,}

my_dictionary = {"key" : "value" , "key2" : "value"}

myPhones = {"iPhone" : 1000 , "sansung S9" : 900}

print(myPhones)

#access keys

iPhone_Price = myPhones["iPhone"]
print("iPhone price: "+str(iPhone_Price))

#change key values

myPhones["iPhone"] = 500
print(myPhones)

#clear values

myPhones.clear()
print(myPhones)