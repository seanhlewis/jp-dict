# Simple translator for JP words written by Sean Lewis
# Uses an offline txt of the FreeDict EN-JP dictionary

jpdict = {}
with open("jp-dict.txt", 'r') as content:
     for line in content:
         if " : " in line.strip():
            (key, val) = line.strip().split(" : ")
            jpdict[key] = val

#print(jpdict)
search = "query"
while search != "":
    search = input("Please enter JP word to translate: ")
    print(jpdict.get(search, "Unknown JP word, please enter again."))