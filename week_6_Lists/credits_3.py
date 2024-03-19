credits_per_class = [4, 3, 3, 2]

total = 0

for credit_count in credits_per_class:  # this is a for loop, will repeat one time for each item in list
     total = total + credit_count
     print(f'{credit_count}, total so far {total}') # example of f'string

print(total)

# total_with_sum_function = sum(credits_per_class)
# print(total_with_sum_function) shorter way is to use sum()function shown here

if total >= 12:
    print('You are a full time student.')
elif total >= 6:
    print('You are a part time student.')  # code is broke bc two ifs, >= 6 mean if 12 or more will print the same
    # message. second 'if' should be 'elif'
else:
    print('You are less than part time.')
