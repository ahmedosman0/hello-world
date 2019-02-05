# Print a list containing numbers from 0 to 20

nums=[]
for number in range(0,21):
    nums.append(number)
print(nums)

# print from 0 to 200 using nums list
print([10 * x for x in nums])

# convert nums list to string list
print(list(map(str, nums)))