row1 = [" ⚪️", " ⚪", " ⚪"]
row2 = [" ⚪️", " ⚪", " ⚪"]
row3 = [" ⚪️", " ⚪", " ⚪"]

map = [row1, row2, row3]
print(f"{row1} \n{row2} \n{row3}")

coordinate = input("Where would you like to place the treasure? ")

#let's say the user input is 13
horizontal = int(coordinate[0])
vertical = int(coordinate[1])

map[horizontal-1][vertical-1] = "🌟"

print(f"{row1} \n{row2} \n{row3}")