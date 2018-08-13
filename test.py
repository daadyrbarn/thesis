## Take a list of values and calculate the average values.
#  Also calculate difference between each value and the avg.
#  Also also print the values as absolute (positive) numbers.

numbers = [113, 200, 144, 99, 145]

avg_num = sum(numbers)/len(numbers)
print(avg_num)

dev_list = []

for x in numbers:
    a = x - avg_num
    dev_list.append(a)
print(dev_list)

print([abs(n) for n in dev_list])
