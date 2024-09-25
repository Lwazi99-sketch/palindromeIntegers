#Write a program called 'palindromeprime.py‘ that finds all palindromic primes between twointegers supplied as input (start and end points are excluded)

#Lwazi Somtsewu 
# 22 August 2024

# 22 August 2024
N =eval(input("Enter the start point N:\n"))
M =eval(input("Enter the start point M:\n"))
print("The palindromic primes are:")
for j in range(N+1,M):    # start at N+1 anD end before M 
    primenumber= True 
    if j == 1: 
        primenumber= False # because 1 is not a prime number 
    for i in range(2,j//2+1): # start at 2 and end at j//2+1 ,checking divisors from 2 to j//2+1
        if j % i ==0:# means this is a even number 
            primenumber=False 
            break
    if primenumber:
        string=str(j)[::-1]
        if str(j)==string:
            print(j)


