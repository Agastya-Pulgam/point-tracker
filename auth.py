from db import get_cursor
from datetime import datetime

def login(new_use,username,email,password,confirm_password,user_login,password_input):

    mydb,mycursor=get_cursor()

    mycursor.execute('select * from user;')
    mycursor.fetchall()
    mydb.commit()
    
    if new_use=='y':

       
        ch=1
        while ch==1:

            
            if password==confirm_password:
                ch=2
                
                sql=('insert into user(username, email,login_password) values(%s,%s,%s)')
                mycursor.execute(sql,(username,email,password))
                mydb.commit()
                logintime=datetime.now()
                history=('insert into history(login_time,username,email) values(%s,%s,%s)')
                values=(logintime,username,email)      
                mycursor.execute(history,values)
                mydb.commit()
                return 'great!! your ID is now ready to use\n'

            else:
                continue
    else:
       
        login_query=('select * from user where username = %s and login_password = %s and email = %s;')
        mycursor.execute(login_query,(user_login,password_input,email))
        result=mycursor.fetchall()
        if result:

            history=('insert into history(username,email) values(%s,%s)')
            values=(user_login,email)
            mycursor.execute(history,values)
            mydb.commit()

            return 'login successful !!\n\n'
           
             
        else:
            return 'invalid login credentials !!'
        


def logout(choice):

    mydb,mycursor=get_cursor()
    
    if choice=='y':
        
        logout_time=datetime.now()
        mycursor.execute('select max(sr_no) from history')
        last_sr_no=mycursor.fetchone()[0]
        command=('update history set logout_time = %s where sr_no =  %s')
        mycursor.execute(command,(logout_time,last_sr_no))
        mydb.commit()

        return 'logged out successfully'

    else:
        return 'logout attempt failed'