Project ©Sanjeevani by <sankat.mochax>

#hackathon23 @ scriet
A 3 day hackathon organised by SCRIET, CCS University for college students.

Tracks given : Smart India Advancement, Healthcare Advancement and Open(Tech) Advancement

Track chosen : Healthcare Advancement

Problems Identified : Unable to provide quick medical support to trauma victims due to lack of info in such short time.
                      Unable to locate nearby people with relevant qualifications to provide first aid to the people in need.

Solutions Implemented : A quick response system for heatlth personnel which uses a centralised database to access medical records in need of emergencies.
           For future : A real time NaVic based tracking system which allows victims of sudden health deterioration to locate people of relevant qualifications to provide first aid.

Part works regarding the stated problem : Indian government has tried to work on a similar system regarding a centralised database, ABDM, but it hasn't been implemented yet in the way we are doing as of now.

Source code documentation : 
                        Database software : MySQL v8.0
                        Language : Python 3.9
                        Hosting platform : Github
                        Repository link : https://github.com/SatyamKumarn14/Hackathon2k23
                            
                        Folder/Repo : Hackathon2k23
                        Database : mdcl_rcd
                        Tables   : basic_info
                                   med_info
                        Python files :  PATIENT.py
                                        database creation.py
                                        TABLE_CREATION.py
                                        DOCTOR.py
                        
                        mdcl_rcd description :
                                        No. of tables : 4
                                        Host : localhost
                                        Table description : 
                                                        Table 1 : basic_info :
                                                                        This table contains field to store basic info of patients during signup.
                                                                        These field are : 
                                                                                        Name :
                                                                                                field info : name
                                                                                        Age : 
                                                                                                field info : age
                                                                                        Gender :
                                                                                                field info : sex
                                                                                        Blood Group :
                                                                                                field info : bdrrp
                                                        Table 2 : med_info : 
                                                                        This table contains fields to store detailed medical info provided by the users.
                                                                        These fields are :
                                                                                        Diseases :
                                                                                                field info : dses : includes presence of any diagnosed illness.
                                                                                        Allergies : 
                                                                                                field info : ALL : includes any allergic conditions.
                                                                                        Genetic Info :
                                                                                                field info : Fdese : includes any presence of illness in patient's parents.
                                                                                        Surgical Hisorty :
                                                                                                field info : shist : includes recent surgical history.
                                                                                        Others : other : includes doctor's notes.
                        Table_creation.py : source code for various table creation.
                                Libraries used : mysql.connector
                                Function used  : table_creation_BASIC_INFO() : creates the table for basic info.
                                                 table_creation_MED_INFO() : creates the table for nedical info.
                                                 autocommit() : returns true/false state to sql.
                                Variables used : mycon : object used to establish cinnection between MySQL and Python.
                                                         cursor : object used in Python to execute SQL queries.
                                                         s2, s3 : used to store SQL queries in string format.

                        database creation.py : source code for database creation.
                                Libraries used : mysql.connector
                                Functions used : execute() : executes sql queries.
                                Variables used : s1 : stores SQL query.

                        PATIENT.py : source code for user end interface.
                                Libraries used : random : creates random numbers for 6 digit for MD_ID
                                                 mysql.connector
                                Functoins used : sign_pg() : allots new row for a new user to store data in the basic_info table.
                                                 entry()   : takes MD_ID as argument and stores various fields of basic_info table.
                                                 login_pg(): takes password as argument and displays all fields of a particular user.
                                                 input()   : python function to get data from the user.  
                                Variables used : MD_ID : stores unique medical id of the user, generated using random() function in python.
                                                 rnd_number : stores random number for MD_ID.
                                                 pwrd : stores user password.
                                                 name : stores name of the user.
                                                 age : stores age
                                                 bdgrp : stores blood group.
                                                 fetch : sql query to print data from the table.
                                                 data : stores fetched data from MySQL.
                                                 row : loop control variable
                                                 mid : argument variable that stores MD_ID.
                                                 detail : stores data fetched from MySQL.
                                                 pwd : stores password to authenticate the user.
                                                 i : loop control variable.
                                                 choice : decision variable that asks user to login or signup.

                        DOCTOR.py : source code for hospital end interface.
                                Libraries used : mysql.connector
                                Functions used : no new functions used.
                                Variables used : no new variables used.



Interface details : Our project currently uses CLI to implement this project which is to be upgaraded to app based GUI.

Implementation details : A database is created for storing user/patient data(includes unique id, age, gender, blood group, diseases, allergies, genetic info, surgical history, others).
These fields are to be filled by users of patient interface, which can be later accessed by hospital authorities through victim's biometrics(for now, we are using unique id instead of biometrics due to lack of experience and resources).

Cases of implementation : A person is visiting out of his/her place of residence, but unfortunately met with an accident which resulted in various critical fractures and excessive bleeding.
                          Coming to his/her support, nearby people immediately contacted nearby hospital.
                          Upon reaching the hospital, doctors had to do some basic necessary tests, which were required to start the required medical procedure since the victim was not in any condition to state his/her medical info.
                          The overall delay unfortunately resulted in the victim's demise.
                          This isn't an exception, but a regular scenario, which yearly results in many deaths.
                          The saying goes TIME waits for none.

                          These deaths could've have been prevented, if doctors had access to the complete medical records of the victims as soon as he/she was admitted.

                          This database can also be used in medical research institutions with the permission of the concerned user.

Project Name : Sanjeevani
License : MIT License
Starting Date : 23-11-2023
Team : <sankat.mochax>
Member details :
        Project Planner : Ankit Kumar, Ist Year
        PPT Designer and Presenter : Ananya Tyagi, Ist Year
        Code Developer : Satyam Kumar, Ist Year
        Team Leader : Arpit Kumar Verma, Ist Year