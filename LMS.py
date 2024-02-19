import codecs

def menu():

    while True:
        print("*** MENU***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Quit")
        seciminiz=int(input("Enter your choice(1-4):"))
        lib = Library("books.txt")
        if seciminiz==1:
            lib.listBook(1)
            print("\n")

        elif seciminiz==2:

            btitle = input("Book title:")
            bauthor = input("Book author:")
            fry = input("First release year:")
            nof = input("Number of pages:")
            binformation = btitle + "," + bauthor + "," + fry + "," + nof

            print(lib.addingBook(binformation))

        elif seciminiz==3:
            lib.removeBook()

        elif seciminiz==4:
            print("Exit!")
            break
        else:
            print("Please enter a number between 1 and 4!")


class Library:

    def __init__(self, dosyaadi):
        self.dosyaadi = dosyaadi
        self.file = open(self.dosyaadi, "a+", encoding="utf-8")

    def addingBook(self, list,menu=0):

        self.list = list
        self.file.write(list)
        self.file.write("\n")
        if menu==0: self.file.close()

        return "The book added succesfully!"

    def listBook(self,menu=0):
        f = codecs.open(self.dosyaadi, "r", "utf-8")
        txt= f.read().splitlines()
        books=[]
        bnames=[]
        for book in txt:
            txt_list= book.split(",")
            books.append(txt_list)

        for i in books:
            bnames.append(i[0])
            if menu==1: print("Book Title:"+str(i[0])+" Book Author:"+str(i[1]))
        return books

    def removeBook(self):
        rtitle = input("Please Enter Book Title To Remove:")
        bookname= self.listBook(2)
        i=0
        open(self.dosyaadi, 'w').close()
        # f = open('books16.txt', 'r+')
        # f.truncate(0)  #
        for bname in bookname:
            if bname[0] == rtitle: i=i+1
            else: self.addingBook(str(bname).replace("[","").replace("]","").replace("'",""),3)
        if i != 0: print("The book deleted!")
        else: print("The library has not the book.")
        self.file.close


    def __del__(self):
        self.file.close()


menu();