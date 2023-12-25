guest = input()
residence = input()
unordered = input()

new_word = [char for char in (guest + residence)]
new_word = "".join(sorted(new_word))

unordered = "".join(sorted([char for char in unordered]))
print("YES") if new_word == unordered else print("NO")
