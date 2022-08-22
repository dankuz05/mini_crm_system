import pyodbc
import pandas as pd
#rukovoditeli_guppi - это процедкра в базе
#Здесь вывожу список Рг



def DataEntry1(name):
    '''Выдает список подчиненных по руквоводителю, (по тому, что ввыодим при входе в программу)'''
    server = ""
    database = ""
    username = ""
    password = ""
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()


    query = f"""

      SELECT * FROM
      table 
      
       where ChefName='{name}'
      order by Operator_Name"""


    df= pd.read_sql(query,cnxn)
    df=df['Operator_Name'].to_list()
    return  df


#Этот блок выдает список людей для блока логина в блоке входа в программу
# Возвращает список сотрудников указанной должности, ФИО будет логином.
def DataEntry2():
    '''Возвращает список сотрудников, которые могут пользоваться программой, более подробно смотри в DataBaseForm'''
    server = "" # Сервер
    database = "" #База данных
    username = "" #Логин для входа в бд
    password = "" # Пароль пользователя  для входа в бд
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    # В бд должна быть подготовлена таблица, в которой тянется список сотрудников, которые будут пользоваться программой
    # В моем случае у меня процедура которая обновляется ежедневно, которая вытягивает сотрудников по выбранной должности
    # Далее внизу, в самом запросе, перобразоввываем таблицу с сотрудниками в список

    query = f"""
    SELECT s.* FROM 
      (Select * from 
       table
       )s order by s.ChefName"""


    df= pd.read_sql(query,cnxn)
    df=df['ChefName'].to_list()
    return df
#В этой функции идет запрос к таблице содлержащей имена сотрудников

#print(DataEntry2.__doc__)
def DataEntryLog(name,log):

    '''Ищет в таблице строку с выбранным ФИО и паролем, при существовании такой строки возвращает
    число больше 0, в противном случае (Неправильный пароль или Фио) возвращает 0. Более подробно смотри в DataBaseForm
    Принимает параметры имя и пароль.
    '''


    server = "mssql-analytics.crm.prod.aservices.tech"
    database = ""
    username = ""
    password = ""
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    query = f"""
    SELECT count(g.Chefname) as czet from (Select * from table 

    where ChefName ='{name}' and [password] = '{log}')g
    """


    df= pd.read_sql(query,cnxn)
    df=df['czet'].to_list()
    return sum(df)




def DataGroups (name):

    '''Возвращает список подразделений, которыми руководит выбранный пользователь.
    Один параметр - имя руководителя.'''

    server = ""
    database = ""
    username = ""
    password = ""
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    query = f"""
    select ChefName,BusinessUnit_Name, COUNT(ChefDir_Name) as cnt 
    from table 
    where ChefName= '{name}' GROUP BY ChefName,BusinessUnit_Name
    """


    df= pd.read_sql(query,cnxn)
    df=df['BusinessUnit_Name'].to_list()
    return df


def sqlinto(ruk,grp,oper,pin,suma,date1,date2,stat,komm):

    '''Заносит в таблицу, все внесенные данные в ячейки, принимаемые параметры смотри в DataBaseForm'''
    server = ""
    database = ""
    username = ""
    password = ""
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    query = f"""
      insert into table  (Руководитель,Группа,Оператор,Пин,Сумма,[Дата внесения],[Оплатит до],Статус,Комментарий)
      values('{ruk}','{grp}','{oper}',{pin},{suma},'{date1}','{date2}','{stat}','{komm}')
      """
    cursor.execute(query)
    cursor.commit()


def sqloutof(ruk):
    '''Делает запрос для обновления таблички в innerTopFrame3 в тривью'''
    server = ""
    database = ""
    username = ""
    password = ""
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    query= f"""select * from table where Руководитель='{ruk}' order by ID desc"""
    df = pd.read_sql(query, cnxn)
    #df.to_string
    return df


#print(sqloutof('Антонова Ирина Викторовна'))

def del_string (ruk):
    '''Удаляет строку по ее номеру. В табличке предусмотрен параметр, который при добавлении строки, присваевает ей индивидуальный номер, параметр один - номер строки'''

    server = "mssql-analytics.crm.prod.aservices.tech"
    database = ""
    username = ""
    password = ""
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    query = f"""delete from table where ID='{ruk}'"""
    cursor.execute(query)
    cursor.commit()


# pyinstaller --hidden-import babel.numbers Narabotki_app.py

def execer():
    '''Это обновлятор процедуры, которая агрегирует внесенные данные нужным для нас образом'''
    server = "mssql-analytics.crm.prod.aservices.tech"
    database = "PressAP"
    username = "AP_read"
    password = "rM6i37Q7"
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    query = f"""
      exec procedure 
      """
    cursor.execute(query)
    cursor.commit()
execer()