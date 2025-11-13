with open("project.txt", "w") as f:
    f.write("This is a file handling project.\n")
    f.write("We are learning different access modes.\n")
print("Step 1: File created and text written using 'w' mode.")

with open("project.txt", "r") as f:
    print("\nStep 2: Reading file using 'r' mode:")
    print(f.read())

with open("project.txt", "a") as f:
    f.write("This line was added using append mode.\n")
print("\nStep 3: Added new line using 'a' mode.")

with open("project.txt", "r") as f:
    print("\nStep 4: Final file content:")
    print(f.read())
