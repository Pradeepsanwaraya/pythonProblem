s = input("Enter string: ")

highest = 0
second = 0
second_char = ""

for ch in s:
    count = 0

    for x in s:
        if ch == x:
            count += 1

    if count > highest:
        second = highest
        highest = count
        second_char = ch

    elif count > second and count != highest:
        second = count
        second_char = ch

print(second_char)
