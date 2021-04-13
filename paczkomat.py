#Setting values
packages_amount = input("Hello, thank You for choosing us to deliver\n How many packages would You like to send ? \n")
packages_amount = int(packages_amount)
#Getting properly package amount
if packages_amount <= 0:
   print("Sorry, you gave incorrect value")
   break
   if packages_amount >= 99:
      print("Slow down a little bit, maximum amount of packages that you can add at once is 99.")
      break
else:
   continue
#Value to incrementate
counter = 0

for counter in range (packages_amount):
    print("czesc")

    #package_weight = input("Podaj ile waży paczka\n ")
    
    #if package_weight == 0