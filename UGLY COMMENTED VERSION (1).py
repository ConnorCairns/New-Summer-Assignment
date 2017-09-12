#Connor Cairns TASK 3 STOCK CONTROL
import sqlite3
import datetime
conn = sqlite3.connect("Task 3 Database.db")
c = conn.cursor()

def addItem():
    GTIN8 = input("Please enter the GTIN-8 code: ") #Taking inputs to put into th database
    itemName = input("Please enter the item name: ")
    currentStock = input("Please enter the current stock: ")
    reOrderStock = input("Please enter the re-order limit: ")
    targetStock = input("Please enter the target stock: ")
    price = input("Please enter the price:£")
    c.execute("""INSERT INTO tblTask3 (GTIN8,itemName,currentStock,reOrderStock,targetStock,price) 
                 VALUES(?,?,?,?,?,?)""",(GTIN8,itemName,currentStock,reOrderStock,targetStock,price,)) #putting items into the database
    conn.commit() #commiting the changes

def viewItems():
    c.execute("SELECT * FROM tblTask3") #selecting the database
    rows = c.fetchall() #setting a variable for the database
    for eachRow in rows: #formatting and then printing information from the database
        print("\nGTIN-8 Code:{0} \nItem Name:{1} \nCurrent Stock:{2} \nRe-Order Level:{3} \nTarget Stock:{4} \nPrice: £{5}".format(eachRow[0],eachRow[1],eachRow[2],eachRow[3],eachRow[4],eachRow[5]))

def editStock():
    print("Please enter the GTIN-8 code of the item you want to edit")
    code = input()
    c.execute("SELECT GTIN8,itemName,currentStock FROM tblTask3 WHERE GTIN8="+code) #selecting the variables I need with the key the user entered
    row=c.fetchall()    
    print("You selected: ",row) #Showing the user what item they selected
    print("Enter what stock value you want to set it to")
    stock = input()
    c.execute("UPDATE tblTask3 set currentStock="+stock+ " WHERE GTIN8="+code) #updating the item the user wanted
    conn.commit()
    print("Successfully updated stock levels")

def deleteItem():
    print("Please enter the GTIN-8 code of the item you want to delete")
    code = input()
    c.execute("SELECT GTIN8,itemName FROM tblTask3 WHERE GTIN8="+code) #selecting the variables I need with the key the user entered
    row=c.fetchall()
    c.execute("DELETE from tblTask3 WHERE GTIN8="+code) #deleting the item
    conn.commit()
    print("You have successfully deleted the following item: ") #Giving the user confirmation of what item was deleted
    for eachRow in row:
        print("\nGTIN-8 Code:{0} \nItem Name:{1}".format(eachRow[0],eachRow[1]))
def orderStock():
    c.execute("SELECT GTIN8,itemName,targetStock FROM tblTask3 WHERE currentStock < reOrderStock") #Selecting the items where the current stock is less than the re order stock
    row=c.fetchall()
    c.execute("UPDATE tblTask3 set currentStock = targetStock WHERE currentStock < reOrderStock") #Updating the stock of the items where the current stock is less than the re order stock
    conn.commit()
    print("You have successfully restocked the following items: ") #Giving the user confirmation of what items were updated
    x = open("reciept.txt", "a")
    date = datetime.date.today()
    for eachRow in row:
        print("\nGTIN-8 Code:{0} \nItem Name:{1} \nNew Stock Amount:{2}".format(eachRow[0],eachRow[1],eachRow[2]))
        x.write("\n" + str(date) + "\nGTIN-8 Code:{0} \nItem Name:{1} \nUpdated stock level:{2} \n".format(eachRow[0],eachRow[1],eachRow[2]))
    print("\nSuccessfully written to text file")
def shop():
    print("Please enter the GTIN-8 code of the item you want to buy")
    code = input()
    c.execute("SELECT GTIN8,itemName FROM tblTask3 WHERE GTIN8="+code) #Selecting the item the user wanted from the key they entered
    row=c.fetchall()
    print("You selected: ",row) #Telling the user what item they selected
    c.execute("SELECT price FROM tblTask3 WHERE GTIN8="+code) #Selecting the price of the item from the database
    price=c.fetchall()
    for eachRow in price:
        newPrice = ("{0}".format(eachRow[0])) #formatting the price
        print("The price is: £"+newPrice)
        print("How many do you want to buy?")
        amount = int(input())
        total = int(newPrice) * int(amount) #working out the total price
        print("Purchase successful, total cost: £"+str(total))
    c.execute("SELECT currentStock FROM tblTask3 WHERE GTIN8="+code) #selecting the stock from the database
    stock=c.fetchall()
    for eachRow in stock:
        newStock = ("{0}".format(eachRow[0]))
        totalStock = int(newStock) - amount #working out the new stock
        c.execute("UPDATE tblTask3 set currentStock="+str(totalStock)+" WHERE GTIN8="+code) #updating the stock in the database
        conn.commit()
    
while True:
    print("-"*35)
    print("Welcome to the stock level viewer!")
    print("-"*35)
    print("\n")
    print("1 - Add item to database")
    print("2 - View items from database")
    print("3 - Delete an item from the database")
    print("4 - Re-Order Stock")
    print("5 - Manually edit stock")
    print("6 - Shop")
    
    response = input()
    if response == "1":
        addItem()
    elif response == "2":
        viewItems()
    elif response == "3":
        deleteItem()
    elif response == "4":
        orderStock()
    elif response == "5":
        editStock()
    elif response == "6":
        shop()
    else:
        print("Invalid input")
    
