for _ in range(int(input())):
    string_input = input().strip()
    count_zero = string_input.count("0")
    count_one = string_input.count('1')
    new_string = ""
    
    for i in range(len(string_input)):
        if string_input[i] == '0' and count_one < 1:
            break
        if string_input[i] == '1' and count_zero < 1:
            break
        if string_input[i] == '0' and count_one > 0:
            new_string += '1'
            count_one -= 1
        elif string_input[i] == '1' and count_zero > 0:
            new_string += '0'
            count_zero -= 1
    
    print(abs(len(string_input) - len(new_string)))
