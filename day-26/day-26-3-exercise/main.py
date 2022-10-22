f1 = open("file1.txt")
nff1 = [line.strip() for line in f1.readlines()]
f2 = open("file2.txt")
nff2 = [line.strip() for line in f2.readlines()]

mutual_numbers = [item for item in nff1 if item in nff2]

print(nff1)
print(nff2)
print(mutual_numbers)

