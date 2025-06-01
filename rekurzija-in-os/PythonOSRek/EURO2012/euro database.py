#1. import the database module
#2. connect to the database EURO2012.db
#3. set up a cursor (call it c) to fectch information from the database
def menu(question):
    print("1-Teams from Euro 2012")
    print("2-Most shots on target")
    print("3-Worst Passers")
    print("4-Most offsides")
    print("5-Dirtiest teams")
    print("6-Quit")
    response=""
    while response not in ("1","2","3","4","5","6"):
        response=input("choose from the menu")
    return response
def main ():
    selection=""
    while selection not in ("1","2","3","4","5"):
        selection=menu("What do you want to know")
        if selection=="1":
            c.execute("SELECT Team FROM TEAMS")# this fetches the Teams from the TEAMS table in the database add SQL code to sort the teams in order
            rows=c.fetchall()
            print(rows)
            main()
        if selection=="2":
            #add a database query to get the Team and their shots on target (put them in order-biggest first)
            #fetch all the results and put them into a variable
            #print the results of the query i.e. the variable
            main()
        if selection=="3":
            #You need to find the Passes Completed field and get the teams who completed less than 1000 passes use WHERE
            main()
        if selection=="4":
           #this should be easy
            main()
        if selection=="5":
            #you will be used to it by now!
            main()
        #add another option
    input("Hit enter to exit")
main()


    
