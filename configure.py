
#run this before entring main_program to configure

def conf():
 '''initialize hostname, mysql username ,password and database '''
  print("Enter following")
  host=str(input("Host : "))
  user=str(input("Mysql Username : "))
  pas=str(input("Mysql password : "))
  databaseName=str(input("Database name : "))
  f=open("dependencies/variable.py","w")
  f.write("host='%s'\nuser='%s'\npas='%s'\ndatabaseName='%s'"%(host,user,pas,databaseName))
  f.close()
  print("Configured")

conf()

