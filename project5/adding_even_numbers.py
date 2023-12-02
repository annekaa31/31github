#You are going to write a program that calculates the sum of all the even numbers\n
#from 1 to X.\n
#If X is 100 then the first even number would be 2 and the last one is 100:

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total_res = 0
for i in range(2, target + 1, 2):
  total_res += i
print(total_res)
