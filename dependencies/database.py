import MySQLdb
from . import messages
from .encrypt import xorWord as xor,encrypt
from . import display_info as di
try:
  from .variable import *
except:
  print("Please run configure file first") #preconfiguration not done
  exit()

a=MySQLdb.connect(host,user,pas,databaseName)
b=a.cursor()

def insertStud(roll,name,pwd,mob,sex,city):
 ''' insert data in database 
      if user not exist in database''' 
  b.execute('Select rollno from Students where rollno=%s;'%a.escape(roll))
  if len(roll)==0 or len(name)==0 or len(pwd)==0 or len(mob)==0 or len(sex)==0 or len(city)==0:
    c=messages.button("Some fields are empty")
    c.b_error()
  elif len(b.fetchall())==0:
    b.execute('insert into Students values (%s,%s,%s,%s,%s,%s);'%(a.escape(roll),a.escape(name),a.escape(pwd),a.escape(mob),a.escape(sex),a.escape(city))) #insert data in database
    c=messages.button("You are registered now you can exit")
    c.b_info()
    a.commit()
  else:
    c=messages.button("Student Already Exists")
    c.b_warn()

def logintask(roll,pwd):
 ''' login user if their registration 
	    already exist'''
  b.execute("select * from Students where rollno=%s AND pass=%s;"%(a.escape(xor(roll,"cyberry")),a.escape(encrypt(pwd))))  
  c=b.fetchall()
  if len(c)!=0:
    c=c[0]
    di.info=(xor(c[1],pwd),xor(c[0],"cyberry"),xor(c[3],pwd),xor(c[5],pwd),xor(c[4],pwd))
    di.vp_start_gui() #display user information after login
  else:
    c=messages.button("Incorrect Login Credentials") 
    c.b_error() #display error while login
