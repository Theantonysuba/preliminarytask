def searchage():
    infile = open("names.txt","r")
    for s in infile:
        s_to_list = s.split()
        if s_to_list[1] == "5":
            print(s)

print(searchage())