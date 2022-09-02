print ("Assignment of Balamurali Krishna S")

print("Printing all Prime Numbers between 1 to 200: ")

for num in range(1, 200 + 1):           #go through whole range to look for each number  
   if num > 1:                          #conditional to check if number greater than 1
       for i in range(2, num):          
           if (num % i) == 0:           #conditional to check if number is not a prime number
               break
       else:                            #else statement to print if it is prime number
           print(num)