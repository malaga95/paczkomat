#Setting values
items_amount = input("Hello, thank You for choosing us to deliver\n How many items would You like to send ? \n")
items_amount = int(items_amount)
#Getting properly items amount
while items_amount <= 0:
   print("Sorry, you gave incorrect value")
   break 
while items_amount > 99:
   print("Slow down a little bit, maximum amount of packages that you can add at once is 99.")
   break
else:   
#Value to incrementate
   counter = 0
   #Setting up packages
   #temp = 0
   #Making a value that will count total weight of items to create packages
   total_weight = 0
   max_weight = 10
   #Setting packages amount to incrementate
   package_amount = 0
   

   #Setting value for weight after weight extension. 
   package_weight = 0

#PROGRAM TERAZ DZIELI PRZEDMIOTY, POPRAW TAK ABY PO PRZEKROCZENIU DANEJ WAGI TWORZYŁ NOWA PACZKE Z CAŁYM PRZEDMIOTEM



# "for" each item unique
   for counter in range (items_amount):
      weight = input(f'Please enter weight of {counter + 1} item: ')
      weight = int(weight)
      if weight > max_weight and total_weight <=20:
         #counter = counter - 1
         weight = 0
         weight = input(f'Weight of each unique item must not extend 10 kg please try again. \n Please enter weight of {counter + 1} item:  ')
         weight = int(weight)

      total_weight += weight
      print(f'Current package weight is : {total_weight}')
      #creating new package if weight extended expected value
      if total_weight > 20:
         print("Each package must be at maximmum weight of 20 kg's")
         package_weight = 0
         #Setting weight of new package after weight extension.
         package_weight = total_weight - weight
         #adding a package
         package_amount += 1
         total_weight = weight
         print(f'Current package weight is : {total_weight}')
   #print(f'Amount of packages : {package_amount + 1}')
   print(f'Total number of packages is : {package_amount}')


    #package_weight = input("Podaj ile waży paczka\n ")
    
    #if package_weight == 0