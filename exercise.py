def count_above_50(numbers):
    count = 0
    for n in numbers:
        if n > 50:
            count += 1
    return count
my_list = [22,70,98,44,67]
print(count_above_50(my_list))       
 