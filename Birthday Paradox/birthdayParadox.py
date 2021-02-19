
def birthday(n):
    if n < 1:
        return - 1
    prob = 1
    for i in range(1, n+1):
        prob = prob * (365 - (i - 1)) / 365
    return 1 - prob

size = input("Please enter the size of the group of people (min. 1): ")
while (not size.isdigit()) or (float(size) != int(size)) or (int(size) < 1):
    size = input("Please enter a valid size of the group of people (min. 1): ")
size = int(size)
print("\nThe probability that at least two people share a birthday in a group of {} people is {:.2f}%".format(size, birthday(size) * 100))