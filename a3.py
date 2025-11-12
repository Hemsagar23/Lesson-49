file = open("Codingal2.txt", "r")
Counter = 0

Content = file.read()
CoList = Content.split("\n")
print(CoList)
Counter = len(CoList)

print("This is the number of lines in the file")
print(Counter)