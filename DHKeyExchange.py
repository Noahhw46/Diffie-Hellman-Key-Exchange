import random

p = int(input("enter P: ")) #public modulus - agreed upon by both - should be prime
g = int(input("enter G: ")) #public number - agreed upon by both

a = int(input("enter your lone secret: ")) #private random number, picked by you
b = random.randint(90, 180) #your friends private random number

A = ((pow(g, a)) % p) #public key established by you
print("Your public key is: " + str(A))

B = ((pow(g, b)) % p) #public key established by your friend
print("Your friends public key is: " + str(B)) 

Ka = ((pow(B, a)) % p) #secret shared by both, established by you
Kb = ((pow(A, b)) % p) #secret shared by both, established by your friend

print("Secret key for A = ", str(Ka))
print("Secret key for B = ", str(Kb))

#testing commits