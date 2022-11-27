from db import db


print(f"{'-'*120}")
print('''                                           Welcome to indian team selecton for 2024 T20 Wordcup 
                                                          
                                                    Menu:
                                                    1) Add new player
                                                    2) Display player
                                                    3) Update player data
                                                    4) Remove player
                                                    5) Select by specification
'''
)
print(f"{'-'*120}")


 #assigning varible name use while updating and adding

printing=["Jersey_Name","First_Name","Last_Name","Dept","IPL_Team","Age","Run"] 

# ADD

def add_player():

    first_name=(input('Enter first name of player: ').title())
    jersey_name=first_name
    last_name=(input('Enter last name of player: ').title())
    IPL_team=(input('Enter IPL team of player (shortform): ').upper())
    player_departments=(input('Enter department of player (Bat/Bowl/All): ').title())
    player_age=(input('Enter age of player: ').title())
    player_run=(input('Enter run of player: ').title())

    jersey_name={}
    jersey_name['fname']=first_name
    jersey_name['lname']=last_name
    jersey_name['iplteam']=IPL_team
    jersey_name['departments']=player_departments
    jersey_name['age']=player_age
    jersey_name['run']=player_run
    db[first_name]=jersey_name
    db.update({first_name:jersey_name})

    print(f"{'-'*120}")
   

# DISPLAY

def Display_player():

    name_to_display=(input('Name of the player or (db for database) you want to display: ')).title()


    print(f"{'-'*125}")
    print(f'\n{"Jersey_Name"}\t\t{"First_Name"}\t\t{"Last_Name"} \t{"IPL_Team"}\t{"Dept"}\t\t{"Age"}\t\t{"Run"}')
    print(f"{'-'*125}")

    if name_to_display =='Db':                #loop for databases
        for i,j in db.items():
                sr=1
                for k,l in j.items():
                    printing[sr]=l
                    sr+=1           
                print(f'  \n{printing[1]:<10.15}   \t\t{printing[1]:<7.10} \t\t{printing[2]:<7.10} \t{printing[3]:<7.10}\t\t{printing[4]:<7.10}\t\t{printing[5]:<7.10}\t\t{printing[6]:<7.10}')
                print(f"{'-'*125}")

    else:            #loop for individual
        for i,j in db.items():
            if i==name_to_display:
                sr=1
                for k,l in j.items():
                    printing[sr]=l
                    sr+=1
                print(f'  \n{printing[1]:<10.15}   \t\t{printing[1]:<7.10} \t\t{printing[2]:<7.10} \t{printing[3]:<7.10}\t\t{printing[4]:<7.10}\t\t{printing[5]:<7.10}\t\t{printing[6]:<7.10}')
                print(f"{'-'*125}")
    if db=={}:
        print()
        print('Database is emty')
        print()
    print(f"{'-'*125}")



#UPDATE

def Update_player_data():
    jersey_name_to_update=(input('jersey name of the player you want to Update data: ')).title()
    db_keys_to_update=(input('dict keys of the player you want to Update[fname,lname,iplteam,department,age,run]: ')).lower()
    db_values_to_update=(input('dict values of the player you want to Update: '))
    db[jersey_name_to_update][db_keys_to_update]=db_values_to_update
    Display_player()
    
    
# REMOVE

def Remove_player():
    name_to_delete=(input('Name of the player or (db for database) you want to Delete: ')).title()
    if name_to_delete=='Db':
        db.clear()
        print('database deleted')
    else: 
        db.pop(name_to_delete)
        # print(db)
        if db=={}:
            print('All data deleted and database is emty')
    print(f"{'-'*120}")
    Display_player()

#----------------------------------------------------------------------------------------------------------------

    





while True:
    option=eval(input('what you want to do in this process[1:Add, 2:Read/Display, 3:Update 4:Delete 5:By Specification]: '))

    if option==1:
        add_player()
        
    elif option==2:
         Display_player()

    elif option==3:
         
         Update_player_data()
        
    elif option==4:
         
         Remove_player()
    # elif option==5:
         
    #      Specify_player()
    else:
        print('invilide input')

    choice=input('do you want to continue [y/n]: ')
    if choice !='y':
        print('Thank you')
        break

