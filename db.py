import mysql.connector as msc

def get_cursor():
    mydb=msc.connect(
        host='localhost',
        user='root',
        password='pulgamagastya29@gmail.com',
        database='d1'
    )
    print('connected !!'if mydb.is_connected() else 'connection failed')
    mycursor=mydb.cursor(buffered=True)

    return mydb, mycursor

