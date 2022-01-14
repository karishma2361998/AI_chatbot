import mysql.connector

def DataUpdate(name,email,state,city,dealer_name,model_name,date,time): 
  mydb = mysql.connector.connect( 
      host="localhost", 
      user="root",  
      passwd="",
      database="location3"
      ) 
               
  mycursor = mydb.cursor()
 
  #sql= "CREATE TABLE customers1 (name VARCHAR(255),email VARCHAR(255),state VARCHAR(255),city VARCHAR(255),dealer_name VARCHAR(255),model_name VARCHAR(255),date VARCHAR(255),time VARCHAR(255));"
  sql='INSERT INTO customers1 (name,email,state,city,dealer_name,model_name,date,time) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}");'.format(name,email,state,city,dealer_name,model_name,date,time)
  mycursor.execute(sql) 
  mydb.commit()
  print(mycursor.rowcount,"record inserted")

if __name__=="__main__":
    DataUpdate("Siddhi Jain","siddhijain123@gmail.com","Maharashtra","mumbai","AGENCY HOUSE (A & N ISLANDS) PVT. LTD","VITARA_BREEZZA","20 Dec 2021","3 p.m")