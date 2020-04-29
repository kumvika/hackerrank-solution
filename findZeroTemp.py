n = int(input())
temp_arr = input().split()
min_temp = max(temp_arr)
for temp in temp_arr:
    if abs(temp) < min_temp:
        min_temp = abs(temp)

print(min_temp)





