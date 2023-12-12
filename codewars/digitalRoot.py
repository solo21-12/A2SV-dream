def digital_root(n):
    while len(str(n)) > 1:
        counter = 0
        for i in str(n):
            counter += int(i)

        n = counter
    return n
