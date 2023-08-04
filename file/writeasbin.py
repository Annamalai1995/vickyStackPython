from pickle import *
name=open("mydata.txt","wb")
studentdata=[501,"Annamalai","KCE","cbe"]

collegedata={"Name":"kumar","College":"KCE","Rollno":5001}

Myfrndsname=("Sathish","Venkat")

dump(studentdata,name)
dump(collegedata,name)
dump(Myfrndsname,name)
name.close()
