import random

def assign(x, nums, s):
    while True:
        y = random.randrange(0, 3)
        if y not in s:
            nums[y] = x
            s.add(y)
            break
    return nums

lst = [0] * 3
s = set()

x = assign("Goat", lst, s)
y = assign("Goat", x, s)
z = assign("Car", y, s)


inp = int(input("Enter Your Choice (0, 1, or 2): "))

revealed = -1
for i in range(3):
    if i != inp and z[i] == "Goat":
        revealed = i
        break
print(f"Revealing a goat at position {revealed}")

inp2 = input("Do You Wish To Change Your Choice? (Y/N): ")

if inp2 == "Y":
    for i in range(3):
        if i != inp and i != revealed:
            inp = i
            break

if z[inp] == "Car":
    print("You Won!")
else:
    print("You Lost!")

print(z)
