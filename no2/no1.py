def searchname():
    infile = open("names.txt","r")
    for s in infile:
        if s[0].lower() == "a":
            print(s)

print(searchname())