import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='MDCL_RCD')
cursor=mycon.cursor()

print("SIGNUP(S)\nLOGIN(L)")
def sign_pg():
    import random
    rnd_no=random.randint(100000,999999)
    print("Please Enter the Following Details")
    MD_ID=rnd_no
    pwrd=input("Enter a six digit numeric password")
    name=input("Name of Patient: ")
    age=input("Age: ")
    sex=input("Sex(M/F/O): ")
    bdgrp=input("Blood Group")
    cursor.execute("INSERT INTO basic_info (MD_ID,PASSWORD,Name,Age,Sex,Blood_Group) VALUES (" + str(MD_ID) + "," + str(pwrd) + ",'" + name + "'," + str(age) + ",'" + sex + "','" + str(bdgrp) + "')")
    cursor.execute("INSERT INTO med_info(MD_ID) VALUES("+str(MD_ID)+")")
    fetch="select * from basic_info where MD_ID="+str(rnd_no)+";"
    cursor.execute(fetch)
    data=cursor.fetchall()
    print("#"*99)
    for row in data:
        print("\nYour Unique Medical ID: ",row[0],"\nYour Entered Password: ",row[1],"\nYour Name: ",row[2],"\nAge: ",row[3],"\nSex: ",row[4],"\nBlood Group",row[5])
    mycon.commit()    

def entry(mid):
    choice=input("Please enter in which field do you want to submit record\nDiseases(D)\nAllergies(A)\nFamily History(F)\nSurgical History(S)\nAny Special Notes(O)\n>>>")
    if choice.lower()=="d":
        dses=input("Enter patient's diagnosed diseases patient is suffering from:")
        cursor.execute("UPDATE mdcl_rcd.med_info SET DISEASES='"+str(dses)+"' WHERE MD_ID="+mid+";")
        mycon.commit()
        
    
    if choice.lower()=="a":
            ALL=input("Enter patient's known Allergies: ")
            cursor.execute("UPDATE mdcl_rcd.med_info SET ALLERGIES='"+str(ALL)+"' WHERE MD_ID="+mid+";")
            mycon.commit()
        
    if choice.lower()=="f":
            Fdses=input("Enter patient's FATHER/MOTHER diagnoses diseases: ")
            cursor.execute("UPDATE mdcl_rcd.med_info SET GENETIC_INFO='"+str(Fdses)+"' WHERE MD_ID="+mid+";")
            mycon.commit()

    if choice.lower()=="s":
            shist=input("Enter patient's Surgical History: ")
            cursor.execute("UPDATE mdcl_rcd.med_info SET SURGICAL_HISTORY='"+str(shist)+"' WHERE MD_ID="+mid+";")
            mycon.commit()


    if choice.lower()=="o":
            other=input("Any Special Note for Patient: ")
            cursor.execute("UPDATE mdcl_rcd.med_info SET OTHER='"+str(other)+"' WHERE MD_ID="+mid+";")
            mycon.commit()  

def login_pg():
    mid=input("Enter Your Unique Medical ID: ")
    cursor.execute("select * from basic_info where MD_ID="+str(mid)+";")
    detail=cursor.fetchall()
    if detail == []:
        print("Make sure you have entered correct Id or you have registered")
    else:
        pwd=input("Enter Password: ")
        for i in detail:
            if str(i[1])==pwd:
                print("Login Successful")
                fetch="select * from basic_info where MD_ID="+str(mid)+";"
                cursor.execute(fetch)
                data=cursor.fetchall()
                for row in data:
                    print("\nYour Unique Medical ID: ",row[0],"\nYour Name: ",row[2],"\nAge: ",row[3],"\nSex: ",row[4],"\nBlood Group",row[5])
                    entry(mid)
            else:
                print("Wrong Password")






choice=input("Enter Your Choice")
if choice.lower()=="s":
    sign_pg()
elif choice.lower()=="l":
    login_pg()
else:
    print("Make a valid selection")
