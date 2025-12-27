from db import get_cursor
from datetime import datetime

def expense(event,balance_update):

    mydb,mycursor=get_cursor()

    time_data=('insert into point_transaction(timestamp) values(%s)')
    mycursor.execute(time_data,(datetime.now(),))
    mydb.commit()

    balance=('select sum(balance) from point_transaction')
    mycursor.execute(balance)
    result=mycursor.fetchone()[0]

    current_balance=result[0] if result[0] is not None else 1000
    new_balance=current_balance-balance_update
    if new_balance<0:
        
        return "can't expend more than what you have"
    else:
        updated_balance=('insert into point_transaction(event,withdrawals,balance) values(%s,%s,%s)')
        mycursor.execute(updated_balance,(event,balance_update,new_balance))
        mydb.commit()

        return 'balance updated.'
    

def add_income(income,event):

    mydb,mycursor=get_cursor()

    current_balance=('select balance from point_transaction')
    mycursor.execute(current_balance)
    result=mycursor.fetchone()
    total=result[0] if result and result is not None else 1000
    total+=income

    income_query=('insert into point_transaction(event,deposits,balance) values(%s,%s,%s)')
    mycursor.execute(income_query,(event,income,total))
    mydb.commit()

    return 'Amount successfully deposited'