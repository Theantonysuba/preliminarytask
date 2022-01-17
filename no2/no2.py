search = input("Enter search item:")

def searchname():
    infile = open("names.txt","r")
    for s in infile:
        if s[:len(search)].lower() == search.lower():
            print(s)

print(searchname())
