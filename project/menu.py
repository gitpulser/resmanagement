from time import sleep
from IPython.display import Markdown, display
import sqlite3
conn = sqlite3.connect('./Menu.db')
bill=[]
update=[]
#soupRecommended, starterRecommended, mainRecommended, breadsRecommended, riceRecommended, sweetsRecommended, drinksRecommended = '','','','','','',''

quant = []

def main():
    

    def Recommended1():
        print("~~~~~Recommended Items For the Day are~~~~~ \n")
        print("Soup :       ", soupRecommended)
        print("Starter :    ", starterRecommended)
        print("Main Course :", mainRecommended)
        print("Breads :     ", breadsRecommended)
        print("Rice :       ", riceRecommended)
        print("Drinks :     ", drinksRecommended)
        print("Sweets :     ", sweetsRecommended)
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("\n ")

    conn.row_factory = lambda cursor,row:row[0]
    #SOUP
    
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT NAME FROM MENU where TAG="SOUPS"')
    soup = cursorObj.fetchall()
    #SOUPQ
     


    cursorObj = conn.cursor()
    cursorObj.execute('SELECT QUANTITY FROM MENU where TAG="SOUPS"')
    soupq = cursorObj.fetchall()

    soupRecommendedValue = max(soupq)
    index = soupq.index(soupRecommendedValue)
    soupRecommended = soup[index]
   
    #STARTER
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT NAME FROM MENU where TAG="STARTERS"')
    starter = cursorObj.fetchall()
    #STARTERQ
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT QUANTITY FROM MENU where TAG="STARTERS"')
    starterq = cursorObj.fetchall()

    starterRecommendedValue = max(starterq)
    index = starterq.index(starterRecommendedValue)
    starterRecommended = starter[index]

    #MAINCOURSE
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT NAME FROM MENU where TAG="MAIN COURSE"')
    mainCourse = cursorObj.fetchall()
    #MAINCOURSEQ
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT QUANTITY FROM MENU where TAG="MAIN COURSE"')
    mainCourseq = cursorObj.fetchall()

    mainRecommendedValue = max(mainCourseq)
    index = mainCourseq.index(mainRecommendedValue)
    mainRecommended = mainCourse[index]

    #RICE
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT NAME FROM MENU where TAG="RICE"')
    rice = cursorObj.fetchall()
    #RICEQ
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT QUANTITY FROM MENU where TAG="RICE"')
    riceq = cursorObj.fetchall()


    riceRecommendedValue = max(riceq)
    index = riceq.index(riceRecommendedValue)
    riceRecommended = rice[index]

    #BREADS
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT NAME FROM MENU where TAG="BREADS"')
    breads = cursorObj.fetchall()
    #BREADSQ
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT QUANTITY FROM MENU where TAG="BREADS"')
    breadsq = cursorObj.fetchall()

    breadsRecommendedValue = max(breadsq)
    index = breadsq.index(breadsRecommendedValue)
    breadsRecommended = breads[index]

    #DRINKS
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT NAME FROM MENU where TAG="DRINKS"')
    drinks = cursorObj.fetchall()
    #DRINKSQ
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT QUANTITY FROM MENU where TAG="DRINKS"')
    drinksq = cursorObj.fetchall()

    drinksRecommendedValue = max(drinksq)
    index = drinksq.index(drinksRecommendedValue)
    drinksRecommended = drinks[index]

    #SWEETS
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT NAME FROM MENU where TAG="SWEETS"')
    sweets = cursorObj.fetchall()
    #SWEETSQ
     
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT QUANTITY FROM MENU where TAG="SWEETS"')
    sweetsq = cursorObj.fetchall()

    sweetsRecommendedValue = max(sweetsq)
    index = sweetsq.index(sweetsRecommendedValue)
    sweetsRecommended = sweets[index]

    def Order():
        
        ch=4
        print("\n")
        print("~~~~~~~~~~~~~~~~~~")
        print("\n\n 1. Soups \n 2. Starter \n 3. Main Course \n 4. Breads \n 5. Rice \n 6. Drinks \n 7. Sweets \n 8. Search \n")
        print("~~~~~~~~~~~~~~~~~~")
        print("\n")
        print("**")
        choice = int(input("Please enter your selection = "))
        print("**")

        if(choice == 1):
            for i in range(len(soup)):
                print(i+1,".",soup[i],end='\n')
            print("\n")
            print("--------------")
            ch=int(input("Enter Your Choice = "))
            q1 =  int(input("Enter the quantity = "))
            print("Ordered Successfully !!")
            print("--------------")
            quant.append(q1)
            cursorObj = conn.cursor()
            sql_comm="""SELECT ID FROM MENU WHERE NAME='%s'""" %(soup[ch-1])
            sql_comm1="""UPDATE MENU SET QUANTITY=QUANTITY-%d WHERE NAME='%s'"""%(q1,soup[ch-1])
            cursorObj.execute(sql_comm)
            a=cursorObj.fetchall()
            cursorObj.execute(sql_comm1)
            conn.commit()
            bill.extend(a)
            #print(bill)
            #print(quant)
            
            

        elif(choice == 2):
            for i in range(len(starter)):
                print(i+1,".",starter[i],end='\n')  
            print("--------------")   
            ch=int(input("Enter Your Choice = "))
            q1 =  int(input("Enter the quantity = "))
            print("Ordered Successfully !!")
            print("--------------")
            quant.append(q1)
            cursorObj = conn.cursor()
            sql_comm="""SELECT ID FROM MENU WHERE NAME='%s'""" %(starter[ch-1])
            sql_comm1="""UPDATE MENU SET QUANTITY=QUANTITY-%d WHERE NAME='%s'"""%(q1,starter[ch-1])
            cursorObj.execute(sql_comm)
            a=cursorObj.fetchall()
            cursorObj.execute(sql_comm1)
            conn.commit()
            bill.extend(a)     
            #print(bill)
            #print(quant)

        elif(choice == 3):
            for i in range(len(mainCourse)):
                print(i+1,".",mainCourse[i],end='\n')
            print("--------------")
            ch=int(input("Enter Your Choice = "))
            q1 =  int(input("Enter the quantity = "))
            print("Ordered Successfully !!")
            print("--------------")
            quant.append(q1)
            cursorObj = conn.cursor()
            sql_comm="""SELECT ID FROM MENU WHERE NAME='%s'""" %(mainCourse[ch-1])
            sql_comm1="""UPDATE MENU SET QUANTITY=QUANTITY-%d WHERE NAME='%s'"""%(q1,mainCourse[ch-1])
            cursorObj.execute(sql_comm)
            a=cursorObj.fetchall()
            cursorObj.execute(sql_comm1)
            conn.commit()
            bill.extend(a)
            #print(bill)
            #print(quant)

        elif(choice == 4):
            for i in range(len(breads)):
                print(i+1,".",breads[i],end='\n')
            print("--------------")
            ch=int(input("Enter Your Choice = "))
            q1 =  int(input("Enter the quantity = "))
            print("Ordered Successfully !!")
            print("--------------")
            quant.append(q1)
            cursorObj = conn.cursor()
            sql_comm="""SELECT ID FROM MENU WHERE NAME='%s'""" %(breads[ch-1])
            sql_comm1="""UPDATE MENU SET QUANTITY=QUANTITY-%d WHERE NAME='%s'"""%(q1,breads[ch-1])
            cursorObj.execute(sql_comm)
            a=cursorObj.fetchall()
            cursorObj.execute(sql_comm1)
            conn.commit()
            bill.extend(a)
            #print(bill)
            #print(quant)

        elif(choice == 5):
            for i in range(len(rice)):
                print(i+1,".",rice[i],end='\n')
            print("--------------")
            ch=int(input("Enter Your Choice = "))
            q1 =  int(input("Enter the quantity = "))
            print("Ordered Successfully !!")
            print("--------------")
            quant.append(q1)
            cursorObj = conn.cursor()
            sql_comm="""SELECT ID FROM MENU WHERE NAME='%s'""" %(rice[ch-1])
            sql_comm1="""UPDATE MENU SET QUANTITY=QUANTITY-%d WHERE NAME='%s'"""%(q1,rice[ch-1])
            cursorObj.execute(sql_comm)
            a=cursorObj.fetchall()
            cursorObj.execute(sql_comm1)
            conn.commit()
            bill.extend(a)
            #print(bill)
            #print(quant)

        elif(choice == 6):
            for i in range(len(drinks)):
                print(i+1,".",drinks[i],end='\n')
            print("--------------")
            ch=int(input("Enter Your Choice = "))
            q1 =  int(input("Enter the quantity = "))
            print("Ordered Successfully !!")
            print("--------------")
            quant.append(q1)
            cursorObj = conn.cursor()
            sql_comm="""SELECT ID FROM MENU WHERE NAME='%s'""" %(drinks[ch-1])
            sql_comm1="""UPDATE MENU SET QUANTITY=QUANTITY-%d WHERE NAME='%s'"""%(q1,drinks[ch-1])
            cursorObj.execute(sql_comm)
            a=cursorObj.fetchall()
            cursorObj.execute(sql_comm1)
            conn.commit()
            bill.extend(a)
            #print(bill)
            ##print(quant)

        elif(choice == 7):
            for i in range(len(sweets)):
                print(i+1,".",sweets[i],end='\n')
            print("--------------")
            ch=int(input("Enter Your Choice = "))
            q1 =  int(input("Enter the quantity = "))
            print("Ordered Successfully !!")
            print("--------------")
            quant.append(q1)
            cursorObj = conn.cursor()
            sql_comm="""SELECT ID FROM MENU WHERE NAME='%s'""" %(sweets[ch-1])
            sql_comm1="""UPDATE MENU SET QUANTITY=QUANTITY-%d WHERE NAME='%s'"""%(q1,sweets[ch-1])
            cursorObj.execute(sql_comm)
            a=cursorObj.fetchall()
            cursorObj.execute(sql_comm1)
            conn.commit()
            bill.extend(a)
            #print(bill)
            #print(quant)
        
        elif(choice == 8):
            print("--------------")
            ch=input("Enter your search = ")
            cursorObj = conn.cursor()
            sql_comm="""SELECT NAME FROM MENU WHERE NAME LIKE '%s' OR TAG LIKE '%s'"""%(ch,ch)
            sql_comm1="""SELECT ID FROM MENU WHERE NAME LIKE '%s' OR TAG LIKE '%s'"""%(ch,ch)
            cursorObj.execute(sql_comm)
            a=cursorObj.fetchall()
            cursorObj.execute(sql_comm1)
            b=cursorObj.fetchall()
            print("~~~~~Found~~~~~~")
            print(a)
            print("\n")
            print("**")
            ch1=int(input("Would you like to add this to your order (1 : YES / 2 : NO) = "))
            if (ch1==1):
                bill.extend(b)
                quan=int(input("Enter the quantity = "))
                print("Ordered Successfully !! \n")
                print("\n")
                quant.append(quan)
                sql_comm2="""UPDATE MENU SET QUANTITY=QUANTITY-%d WHERE NAME='%s'"""%(quan,ch)
                cursorObj.execute(sql_comm2)
                conn.commit()

        order_flag = 0 #initial case
        order_flag = int(input("Do you want to add another order?\n1. Yes\n2. No\n"))
        if order_flag == 1:
            Order()   
                 
    def Bill():
        sumn=0
        for i in range(len(bill)):
            cursorObj = conn.cursor()
            sql_comm="""SELECT PRICE FROM MENU WHERE ID=%d""" %(bill[i])
            cursorObj.execute(sql_comm)
            a=cursorObj.fetchall()
            sumn+=sum(a)
        print("\n")
        print("The total price is ",sumn,end="\n")
        print("\n")
    
    def Update():
        for i in range(len(bill)):
            cursorObj = conn.cursor()
            sql_comm="""SELECT NAME FROM MENU WHERE ID=%d""" %(bill[i])
            cursorObj.execute(sql_comm)
            a=cursorObj.fetchall()
            update.extend(a)
        print("~~~~~~~~~~~~~~~~~~~~~")
        for j in range(0,len(bill)):
            print(j+1,".",'{0:<35}'.format(update[j]),end='')
            for k in range(0,len(quant)):
                if(j==k):
                    print(quant[k])
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("\n")
        ch=int(input("Do you want to delete any order \n 1.YES \n 2.NO \n "))
        if(ch==1):
            q=1
            while len(update)>=q:
                print("\n")
                ch1=int(input("Enter the food serial number = "))
                ch2=int(input("Enter the quantity to remove = "))
                print("Deleted Successfully !!")
                quant[ch1-1]=quant[ch1-1]-ch2
                cursorObj = conn.cursor()
                sql_comm="""UPDATE MENU SET QUANTITY=QUANTITY+%d WHERE NAME='%s'""" %(ch2,update[ch1-1])
                cursorObj.execute(sql_comm)
                conn.commit()
                if (quant[ch1-1]<0):
                    print("Enter correct quantity !")
                if(quant[ch1-1]==0):
                    del(bill[ch1-1])
                    del(update[ch1-1])
                    del(quant[ch1-1])
                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~")
                for j in range(0,len(bill)):
                    print(j+1,".",'{0:<35}'.format(update[j]),end='')
                for k in range(0,len(quant)):
                    if(j==k):
                        print(quant[k])
                print("~~~~~~~~~~~~~~~~~~~~~")
                print("\n")
                print("Do you want to delete anything else ? 1:Yes / 2:No ")
                ch3=int(input("Enter choice = "))
                
                if (ch3==2):
                    q=len(update)
                else:
                    break
                break
        
        
    def Feedback():
        print("\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        feed=input("Please enter your feedback : ")
        print("Thank you for your feedback :)")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n")
        

    while True:
        #Recommended1()
        print("\n")
        print("~~~~~~~~~~~~~~~~~~~~~")
        print(" Menu \n 1. Recommended Items \n 2. Order \n 3. Bill \n 4. View/Update \n 5. Contact \n 6.Feedback \n 7. Exit \n")
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("\n")
        choice = int(input("Enter option  =  \n"))
        if(choice == 1):
            Recommended1()

        elif(choice == 2):
            Order()
            #print(o)
        elif(choice == 3):
            Bill()
        
        elif(choice == 4):
            Update()
        
        elif(choice == 5):
            Contact()

        elif(choice==6):
            Feedback()
        
        elif(choice == 7):
            break

        else:
            print("Please enter a valid number \n \n \n")
            sleep(2)

    
    
    

    #print("\n\n Choose category \n 1. Soup \n 2. Starter \n 3. Main Course \n 4. Rice \n 5. Breads \n 6. Drinks \n 7. Sweets \n")
    #choice = int(input("Enter category"))
    #print(choice)


def Contact():
    print("~~~~~~~~~~~~~~~~~~~~~")
    print("\n Our representative will be at your table shortly.  \n ")
    print("~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    main()