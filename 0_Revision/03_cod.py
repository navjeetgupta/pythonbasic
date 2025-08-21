import os

# choose the path of desired directory
path = './0_Revision'  # change this to your target directory
entries = os.listdir(path)
print(f"Contents of '{path}':")
for entry in entries:
    # print the entries now
    print(entry)