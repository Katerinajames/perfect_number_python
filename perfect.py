# https://www.geeksforgeeks.org/perfect-number-program-in-python/
p=int(input("Enter a number\n"))

sum=0 

for i in range (1,p):
	if p%i==0:
		sum=sum+i
		
if sum==p:
	print("The number %d is perfect"%(p))
else:
 
	print("The number %d is not  perfect"%(p))  
