import  sqlite3
conn  =  sqlite3 . connect ( 'AssignDatabase.db' )
cursor  =  conn.cursor ()

cursor.execute("CREATE TABLE input(username char(30), itemname char(30));")

users=[]
items=[]

want='true'
want=input('''If you want to enter users list and items list 
Enter True or False: ''').lower()

while(want=='true'):
    if want=='true':
        # number of elements as input
        n = int(input("Enter number of users you want to add: "))
        # iterating till the range
        for i in range(0, n):
            userslistinput=input("Enter the users list input: ")
            users.append(userslistinput) # adding the element

        m = int(input("Enter number of items you want to add: "))        
        for j in range(0, m):
            itemslistinput=input("Enter the items list input: ")
            items.append(itemslistinput) # adding the element

        cursor.execute('''
                INSERT INTO input(username, itemname)
                VALUES (?,?)
                    ''', (userslistinput, itemslistinput))
        conn.commit ()
        print ( 'Data entered successfully.' )
        conn . close ()
        if (conn):
            conn.close()
            print("\nThe SQLite connection is closed.")
        # print(users)
        # print(items)
        break

    else:
        break