import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='MDCL_RCD')
cursor=mycon.cursor()

print("ABC GROUUP OF HOSPITALS, MEERUT")
mid=input("Patient's Biometrics       : ")
cursor.execute("select * from med_info where MD_ID="+str(mid)+";")
detail=cursor.fetchall()
if detail==[]:
    print("Sorry! Patient is not registered with SANJEEVANI")
else:
    for row in detail:
        print("\nUnique Medical ID          : ",row[0],
              "\nKnown Diseases             : ",row[1],
              "\nKnown Allergies            : ",row[2],
              "\nFamily History             : ",row[3],
              "\nPrevious surgeries         : ",row[4],
              "\nDoctor's Notes             : ",row[5])