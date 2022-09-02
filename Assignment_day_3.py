print ("Assignment of Balamurali Krishna S")
print("Printing all Prime Numbers between 1 to 200: ")
for num in range(1, 200 + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)