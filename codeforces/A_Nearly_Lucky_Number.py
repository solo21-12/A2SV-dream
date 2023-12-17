n = input()

count_lucky = sum([1 for digit in n if digit in '47'])

is_nearly_lucky = all([digit in '47' for digit in str(count_lucky)])

if is_nearly_lucky:
    print("YES")
else:
    print("NO")
