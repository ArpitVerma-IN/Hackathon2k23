'''def table_creation_NAME_PWD():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='mdcl_rcd')
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create table IF NOT EXISTS md_id(MD_ID int(6),Name varchar(20),PASSWORD int(4))"
    cursor.execute(s1)
table_creation_NAME_PWD()'''


def table_creation_BASIC_INFO():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='mdcl_rcd')
    cursor=mycon.cursor()
    mycon.autocommit=True
    s2="create table IF NOT EXISTS basic_info(MD_ID int(6),PASSWORD int(4),Name varchar(20),Age int(3),Sex varchar(1), Blood_Group varchar(3))"
    cursor.execute(s2)
table_creation_BASIC_INFO()


def table_creation_MED_INFO():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='mdcl_rcd')
    cursor=mycon.cursor()
    mycon.autocommit=True
    s3="create table IF NOT EXISTS MED_INFO(DISEASES varchar(100), ALLERGIES varchar(100), GENETIC_INFO varchar(100),SURGICAL_HISTORY varchar(100),OTHER varchar(100))"
    cursor.execute(s3)
table_creation_MED_INFO()
