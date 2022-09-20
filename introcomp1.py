# Question 1
nums = list(range(30,65,5))

nums.sort(reverse=True)

x = 65
nums.insert(0,x)
 
print(nums)

# Question 2

e_list = []
for number in range(0,21):
    e_list += [number]

e_list.remove(0)

print(e_list)
print(len(e_list))
print(e_list[-1])
print(e_list[0])

Sum=sum(e_list)
print(Sum)

# Question 3

weather={"sunny":"play","rainy":"watch TV","cloudy":"walk"}
for key, value in weather.items():

        print("When",key, "let us", value )
        

