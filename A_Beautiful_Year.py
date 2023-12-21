def has_distinct_digits(year):
    return len(set(str(year))) == len(str(year))


def find_next_distinct_year(current_year):
    next_year = current_year + 1
    while not has_distinct_digits(next_year):
        next_year += 1
    return next_year


year = int(input())

result = find_next_distinct_year(year)
print(result)
