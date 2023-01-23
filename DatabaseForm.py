import pyodbc
import pandas as pd
import numpy as np
import passwords as pw

server = pw.server
database = pw.database
username = pw.username
password = pw.password

def DataEntry1(name):

    '''Возвращает список менеджеров, находящихся в подчинении у руководителя
    Указанного в параметрах из таблицы - st.rukovoditeli_guppi'''

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    query = f"""
      SELECT * FROM
      st.rukovoditeli_guppi where ChefName='{name}'
      order by Operator_Name"""
    df= pd.read_sql(query,cnxn)
    df=df['Operator_Name'].to_list()
    return  df


def DataEntry2():

    '''Для окна входа
    - Возвращает список руководителей групп для входа в программу табл- st.narabotki_names_of_rg'''

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    query = f"""
    SELECT s.* FROM 
      (Select * from st.narabotki_names_of_rg )s order by s.ChefName"""
    df= pd.read_sql(query,cnxn)
    df=df['ChefName'].to_list()
    return df

def DataEntryLog(name,log):

    '''Условие для входа:
    Проверяет на наличие в таблице строк с выбранным руководителем группы и паролем, должен возвращать 1 и 0
    (кол-во строк с выбранным именем и паролем).
    Используется для того, чтобы открылось основное окно после нажатия кнопки войти
    Запрс к табл- st.narabotki_names_of_rg
    '''

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    query = f"""
    SELECT count(g.Chefname) as czet from (Select * from st.narabotki_names_of_rg
    where ChefName ='{name}' and [password] = '{log}')g
    """
    df= pd.read_sql(query,cnxn)
    df=df['czet'].to_list()
    return sum(df)


def DataGroups (name):

    '''Возвращает список групп, которые находятся в подчинении руководителя группы, имя которого передается в параметрах
    Запрос к табл - st.rukovoditeli_guppi '''

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    query = f"""
    select ChefName,BusinessUnit_Name, COUNT(ChefDir_Name) as cnt 
    from st.rukovoditeli_guppi 
    where ChefName= '{name}' GROUP BY ChefName,BusinessUnit_Name
    """
    df= pd.read_sql(query,cnxn)
    df=df['BusinessUnit_Name'].to_list()
    return df


def sqlinto(ruk,grp,oper,pin,suma,date1,date2,stat,komm):

    '''Функция внесения в базу данных значений из заполненых окошек
    В параметрах указываем значения внутри столбцов по порядку, как в таблице - dbo.narabotki_data'''

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    query = f"""
      insert into dbo.narabotki_data (Руководитель,Группа,Оператор,Пин,Сумма,[Дата внесения],[Оплатит до],Статус,Комментарий)
      values('{ruk}','{grp}','{oper}',{pin},{suma},'{date1}','{date2}','{stat}','{komm}')
      """
    cursor.execute(query)
    cursor.commit()


def sqloutof(ruk):
    '''Для кнопки фильтра, покажет все записи из тблаицы, где руководитель = параметру ф-ции'''

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    query= f"""select * from dbo.narabotki_data where Руководитель='{ruk}' order by ID desc"""
    df = pd.read_sql(query, cnxn)
    return df


def del_string (ruk):
    '''Удаление строчек из основной таблицы
    ruk- параметр имени руковдителя
    Прописано условие на возмонжость удаления строки только в день внесения строчки
    При выполнении условия дня вернет 1'''

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    query2 = f"""select convert(varchar,[Дата внесения],4) dat from dbo.narabotki_data where ID= {ruk}"""
    df = pd.read_sql(query2, cnxn)
    df['dat'] = pd.to_datetime(df['dat'])
    df['today'] = pd.to_datetime('today').normalize()
    df['is_it'] = np.where(df['dat'] == df['today'],1,0)
    x=df.iloc[0]['is_it']
    if x>0:
        query = f"""delete from dbo.narabotki_data where ID={ruk}"""
        cursor.execute(query)
        cursor.commit()
        return 1
    else:
        print('Удаление возможно только в день внесения')

def look_alike(ruk):

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

    cursor = cnxn.cursor()
    query= f"""select * from dbo.narabotki_data where ID= {ruk} """
    df=pd.read_sql(query,cnxn)
    return df


# pyinstaller --noconsole  --onefile --hidden-import babel.numbers Narabotki_app.py
# pyinstaller   --onefile  exec_whats.py

def filter (operator=0,date=0,ruk=0):

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

    cursor = cnxn.cursor()
    if operator !=0:
        query = f"""select * from dbo.narabotki_data nolock where Оператор = '{operator}' order by ID desc """
        df= pd.read_sql(query,cnxn)
        return df
    if date !=0:
        query1 = f"""select * from dbo.narabotki_data nolock where [Оплатит до] = '{date}' and Руководитель = '{ruk}' order by ID desc """
        df2= pd.read_sql(query1,cnxn)
        return df2
    else:
        print('Ничего')

def sbivaemost (name):

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

    query = f"""select AVG(Вероятность) Вероятность from st.narabotki_main_table where Руководитель= '{name}' """
    df= pd.read_sql(query,cnxn)
    x = df.iloc[0]['Вероятность']
    if x== None:
        return 0
    else:
        return x

