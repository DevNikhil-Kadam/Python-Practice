# indx = [0,1,2,3,4]
nums = [1,2,3,4,5]
# idx = -[5,4,3,2,1]
output = []

output.append(nums[-1])

for i in range(0,len(nums)-1):
    output.append(nums[i]) 
print(output)
