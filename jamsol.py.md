```python
import json
import yaml
import os
import sys


def jtest(filename):
    if len(filename) > 1 and os.path.exists(filename):
        try:
            file = open(filename, "r")
            json.load(file)
            file.close()
            print(f"\n[+] {filename} is JSON")
        except:
            print("\n[-] Probably not JSON")
    else:
        print("\n[?] Bad filename or path")


def ytest(filename):
    if len(filename) > 1 and os.path.exists(filename):
        try:
            file = open(filename, "r")
            yaml.safe_load(file.read())
            file.close()
            print(f"\n[+] {filename} is YAML")
        except:
            print("\n[-] Probably not YAML")
    else:
        print("\n[?] Bad filename or path")


def y2jconv(filename):
    dest = input("\n[?] Name for the new JSON file: ")
    if len(filename) > 1:
        try:
            sourceFile = open(filename, "r")
            sourceContent = yaml.safe_load(sourceFile)
            sourceFile.close()
        except:
            print("\n[?] Is this a YAML file?")
        else:
            output = json.dumps(sourceContent)
            if os.path.exists(dest):
                print("\n[-] File already exists")
                exit(1)
            else:
                targetFile = open(dest, "w")
                targetFile.write(output)
                targetFile.close()
def j2yconv(filename):
    dest = input("\n[?] Name for the new YAML file: ")
    if len(filename) > 1 and os.path.exists(filename):
        try:
            sourceFile = open(filename, "r")
            sourceContent = json.load(sourceFile)
            sourceFile.close()
        except:
            print("\n[?] Is this a JSON file?")
        else:
            output = yaml.dump(sourceContent)
            if os.path.exists(dest):
                print("\n[-] File already exists")
                exit(1)
            else:
                targetFile = open(dest, "w")
                targetFile.write(output)
                targetFile.close()



print("\nWelcome to the YAML to JSON suite!\n*****************************************\nCHOOSE AN OPTION BELOW\n*****************************************\n")
print("JSONTEST\n--This will let you test if a file is JSON")
print("YAMLTEST\n--This will let you test if a file is YAML")
print("Y2J\n--This can help you convert a file from YAML to JSON")
print("J2Y\n--This can help you convert a file from JSON to YAML")
userIn = input("Choose an option: ")
if userIn == "JSONTEST":
    jtest(input("Give me a file to check: "))
elif userIn == "YAMLTEST":
    ytest(input("Give me a file to check: "))
elif userIn == "Y2J":
    y2jconv(input("Give me the YAML file to convert: "))
elif userIn == "J2Y":
    j2yconv(input("Give me the JSON file to convert: "))
else: 
    print("[-] Try again")

def main():
    print("That was fun")

```