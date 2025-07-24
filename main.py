from auth import login,logout
from db import get_cursor
from finance import add_income 
from finance import expense

def main():
    
    mydb,mycursor=get_cursor()

    print('welcome to point transaction 2.0')

    new_use=input('are you a new user? : ').lower()

    if new_use=='y':

        username=input('enter username : ')
        email=input('enter email ID : ')
        
        ch=1
        while ch==1:

            password=input('enter password : ')
            confirm_password=input('re-enter password : ')
            if password==confirm_password:
                ch=2

                result=login(
                    new_use='y',
                    username=username,
                    email=email,
                    password=password,
                    confirm_password=confirm_password,
                    user_login=None,
                    password_input=None
                )
                print(result)

                if 'great!! your ID is now ready to use\n' in result:

                    while True:

                        print('1. Deposit points to balance\n2. Withdraw points from balance\n')
                        print('3. Logout\n')

                        choice=int(input('\n--> '))

                        if choice == 1:

                            try:
                                income=int(input('enter amount to deposit : '))
                            except ValueError:
                                print('please enter only integer values !!')

                            event=input('enter source : ').strip()

                            if not event:
                                print('No source provided. Operation aborted')
                            else:
                                print('proceeding......')
                                print(add_income(income,event))
                        
                        elif choice == 2:

                            event=input('enter cause of expense : ').strip()
                            
                            if not event:
                                print('No cause provided. Operation aborted')
                            else:
                                balance_update=int(input('enter amount spent : '))

                                print(expense(event,balance_update))

                        elif choice == 3:
                            
                            choice = input('Do you want to logout ? [y or n] : ')

                            print(logout(choice))
                    

    
    else:

        user_login=input('Enter username : ')
        email=input('enter email : ')
        password_input=input('enter password : ')

        result=login(
            new_use='n',
            username=None,
            email=email,
            password=None,
            confirm_password=None,
            user_login=user_login,
            password_input=password_input
        )
        print(result)

        if 'login successful !!' in result:

            while True:

                print('1. Deposit points to balance\n2. Withdraw points from balance\n')
                print('3. Logout\n')

                choice=int(input('\n--> '))

                if choice == 1:

                    try:
                        income=int(input('enter amount to deposit : '))
                    except ValueError:
                        print('please enter only integer values !!')

                    event=input('enter source : ').strip()

                    if not event:
                        print('No source provided. Operation aborted')
                    else:
                        print('proceeding......')
                        print(add_income(income,event))
                
                elif choice == 2:

                    event=input('enter cause of expense : ').strip()
                    
                    if not event:
                        print('No cause provided. Operation aborted')
                    else:
                        balance_update=int(input('enter amount spent : '))

                        print(expense(event,balance_update))

                elif choice == 3:
                    
                    choice = input('Do you want to logout ? [y or n] : ')

                    print(logout(choice))
                    break
                    


main()