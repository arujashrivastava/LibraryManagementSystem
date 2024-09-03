class Library:
    def __init__(self,mylist,myname):
        self.list1=mylist
        self.name=myname

    def lend(self):
        print(ArujaLibrary.list1)
        le = input("Write the name of the book you want to issue:")
        if d1[le] == "Available":
            var1 = input("Enter your name:")
            d1.update({le: var1})
            print("Thank You! You can take the book from the shelf and please do return it within a week")
        else:
            print("This book is already issued by", d1[le])

    def added(self,vary):
        self.list1.append(vary)

    def retur(self):
        var3 = input("Name of the book that you want to return:")
        d1.update({var3: "Available"})
        print("Keep the book in the library shelf. Thanks for Issuing")

ArujaLibrary=Library(["Harry Potter","Goosebumps","Bhagwat Gita","Ramayana","Perfume: Story Of a Murderer"],"Aruja")
d1={"Harry Potter":"Available","Goosebumps":"Available","Bhagwat Gita":"Available","Ramayana":"Available","Perfume: Story Of a Murderer":"Available"}
print("Welcome to Aruja's Library")
while True:
    print(d1)
    num1=int(input("Enter a number, of your choice:\n1.Display Books\n2.Lend Books\n3.Add Books\n4.Return book"))
    if num1==1:
        print(ArujaLibrary.list1)
        continue

    elif num1==2:
        ArujaLibrary.lend()
        continue

    elif num1==3:
        print("We appriciate you for adding your book in our library")
        var2=input("What's tha name of your book:")
        d1.update({var2:"Available"})
        ArujaLibrary.added(var2)
        print("Thank You! Please do visit again.")
        continue

    elif num1==4:
        ArujaLibrary.retur()
        continue

    else:
        print("Invalid Input")
        continue