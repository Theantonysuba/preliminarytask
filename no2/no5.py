
def searchname(search):
    infile = open("names.txt","r")
    for s in infile:
        if s[:len(search)].lower() == search.lower():
            print(s)

def searchage(search):
    infile = open("names.txt","r")
    for s in infile:
        s_to_list = s.split()
        if s_to_list[1] == search:
            print(s)




input_choice = input("Press 1 to search with name, press 2 to search with age:")
 
if int(input_choice) == 1:
    search = input("Enter search item:")
    print(searchname(search))
elif int(input_choice) == 2:
    search = input("Enter search age:")
    print(searchage(search))
else:
    print("You entered an invalid option")
    



