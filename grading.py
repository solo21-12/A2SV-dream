def gradingStudents(grades):
    ans = []
    for i in grades:
        if i < 38:
            ans.append(i)
        else:
            next_multiple = ((i // 5) + 1) * 5
            if next_multiple - i < 3:
                ans.append(next_multiple)
            else:
                ans.append(i)
    return ans
