def filereader(file):
    """Read file and remove '\n'"""
    with open(file, mode="r") as file:
        f_read = file.readlines()
        f = [int(i.replace("\n", "")) for i in f_read]
        return f


file1 = filereader("file1.txt")
file2 = filereader("file2.txt")

# find duplicates and save to result
result = [n for n in file1 if n in file2]

# Write your code above 👆

print(result)
