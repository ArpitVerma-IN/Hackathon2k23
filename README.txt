#hackathon23 @ scriet
A 3 day hackathon organised by SCRIET, CCS University for college students.

Tracks given : Smart India Advancement, Healthcare Advancement and Open(Tech) Advancement

Track chosen : Healthcare Advancement

Problems Identified : Unable to provide quick medical support to trauma victims due to lack of info in such short time.
                      Unable to locate nearby people with relevant qualifications to provide first aid to the people in need.

Solutions Implemented : A quick response system for heatlth personnel which uses a centralised database to access medical records in need of emergencies.
        For future    : A real time NaVic based tracking system which allows victims of sudden health deterioration to locate people of relevant qualifications to provide first aid.

Part works regarding the stated problem : Indian government has tried to work on a similar system regarding a centralised database, ABDM, but it hasn't been implemented yet in the way we are doing as of now.

Source code documentation : 
                            Database software : MySQL v8.0
                            Language : Python 3.9
                            Hosting platform : Github
                            Repository link : https://github.com/SatyamKumarn14/Hackathon2k23
                            
                            Database : mdcl_rcd
                            Tables   : basic_info
                                       med_info

                            Python files : PATIENT.py
                                           database creation.py
                                           TABLE_CREATION.py
                            


                            

Implementation details : A database is created for storing user/patient data(includes unique id, age, gender, blood group, diseases, allergies, genetic info, surgical history, others).
These fields are to be filled by users of patient interface, which can be later used by hospital authorities through victim's biometrics(for now, we are using unique id instead of biometrics due to lack of experience and resources).

Cases of implementation : A person is visiting out of his/her place of residence, but unfortunately met with an accident which resulted in various critical fractures and excessive bleeding.
                          Coming to his/her support, nearby people immediately contacted nearby hospital.
                          Upon reaching the hospital, doctors had to do some basic necessary tests, which were required to start the required medical procedure since the victim was not in any condition to state his/her medical info.
                          The overall delay unfortunately resulted in the victim's demise.
                          This isn't an exception, but a regular scenario, which yearly results in many deaths.
                          The saying goes TIME waits for none.

                          These deaths could've have been prevented, if doctors had access to the complete medical records of the victims as soon as he/she was admitted.

                          This database can also be used in medical research institutions with the permission of the concerned user.