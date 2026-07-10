number=int(input("Enter your employe number: "))
for i in range(number):
    name=input("Enter your employe name: ")
    employ_file=open("test1.txt","w")
    employ_file.write("\n")
    terminal_write=employ_file.write(name)
    employ_file.write("\n")
    employ_file.close()
