import sqlite3

conn = sqlite3.connect('Menu.db')
crsr = conn.cursor()
print ("Opened database successfully")
#conn.execute("""CREATE TABLE MENU (ID INT PRIMARY KEY,NAME TEXT NOT NULL,TAG TEXT NOT NULL,QUANTITY INT NOT NULL,PRICE INT NOT NULL);""")

sql="""INSERT INTO MENU VALUES(1,'Manchow Soup','SOUPS',20,70);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(2,'Tomato Soup','SOUPS',22,70);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(3,'Sweet Corn Soup','SOUPS',19,70);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(4,'Gobi 65','STARTERS',25,170);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(5,'Veg. Spring Roll(6 Pcs)','STARTERS',22,175);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(6,'Paneer 65','STARTERS',20,190);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(7,'Chilly Baby Corn Fry','STARTERS',18,220);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(8,'Kadai Paneer','MAIN COURSE',24,240);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(9,'Paneer Butter Masala','MAIN COURSE',22,250 );"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(10,'Chilly Paneer Dry','MAIN COURSE',20,255);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(11,'Dal Fry','MAIN COURSE',30,180);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(12,'Gobi Manchurian Dry','MAIN COURSE',24,200);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(13,'Dum Aloo','MAIN COURSE',25,190);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(14,'Paratha','BREADS',40,50);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(15,'Plain Roti','BREADS',50,60);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(16,'Plain Naan','BREADS',50,55);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(17,'Butter Naan','BREADS',55,75);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(18,'Curd Rice','RICE',30,75);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(19,'Steam Rice','RICE',33,65);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(20,'Lemon Rice','RICE',27,75);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(21,'Sambhar Rice','RICE',38,75);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(22,'Parappu Rice','RICE',32,75);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(23,'Lemon Juice','DRINKS',50,30);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(24,'Lemon Soda','DRINKS',45,35);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(25,'Cold Drinks','DRINKS',70,30);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(26,'Fresh Orange Juice','DRINKS',60,50);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(27,'Mango-Seasonal','DRINKS',80,60);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(28,'Basundhi','SWEETS',40,70);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(29,'Gulab Jamun','SWEETS',50,60);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(30,'Sweet Pongal','SWEETS',60,50);"""
crsr.execute(sql)
sql="""INSERT INTO MENU VALUES(31,'Rasamalai','SWEETS',70,70);"""
print("Recorded")
conn.close()