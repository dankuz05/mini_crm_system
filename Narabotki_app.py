import tkinter
import DatabaseForm
from tkinter import *
from tkcalendar import DateEntry
import tkinter.messagebox
from tkinter import ttk
import time

root1=Tk()
root1.title('Вход')
root1.geometry('700x300+300+200')
root1.resizable(False,False)
root1.configure(bg="#fff")
Frame1=Frame(root1,width=200,height=200,bg='white')
Frame1.place(x=150,y=70)

lbl = Label(Frame1, font=('font', 12, 'bold'), text="     ВАШЕ ФИО:",  bd=10, bg= "white")
lbl.grid(row=0, column=0)
btn2 = ttk.Combobox(Frame1, font=('font', 12, 'bold'),width=32)
btn2['value'] = DatabaseForm.DataEntry2()
btn2.current()
btn2.grid(row=0, column=1)

lbl2 = Label(Frame1, font=('font', 12, 'bold'), text="ПАРОЛЬ:",  bd=10,bg= "white")
lbl2.grid(row=1, column=0)
btn3 = Entry(Frame1, font=('font', 12, 'bold'), bd=5, width=32, justify='left')
btn3.grid(row=1, column=1)


def zz():
    name=btn2.get()
    passw= btn3.get()
    datetoday= time.strftime("%d.%m.%Y")

    if DatabaseForm.DataEntryLog(name, passw)>0:
        root1.destroy()
        root = Tk()
        root.title("Наработки| Внесение данных")
        root.geometry("1070x705")
        root.configure(background="gainsboro")

        MainFrame = Frame(root, bd=10, width=1300, height=1300, relief=RIDGE,bg='lightblue')
        MainFrame.pack_propagate(0)
        MainFrame.pack(fill='both', side='left', expand='True')
        MainFrame.grid()


        TopFrame1 = Frame(MainFrame, bd=10, width=100, height=200, relief=RIDGE,bg='lightblue')
        TopFrame1.pack_propagate(0)
        TopFrame1.pack(fill='both', side='left',padx=0,pady=0,anchor='w',expand='False')
        TopFrame1.grid()
        TopFrame2 = Frame(MainFrame, bd=10, width=1300, height=50, relief=RIDGE)
        TopFrame2.grid()

        TopFrame6 = Frame(MainFrame, bd=10, width=1300, height=50, relief=RIDGE)
        TopFrame6.grid()

        TopFrame3 = Frame(MainFrame, bd=10, width=1300, height=300, relief=RIDGE)
        TopFrame3.grid()
        TopFrame4= Frame(MainFrame, bd=10, width=1300, height=50, relief=RIDGE)
        TopFrame4.grid()

        innerTopFrame1 = Frame(TopFrame1, bd=5, width=1000, height=190, relief=RIDGE)
        innerTopFrame1.pack_propagate(0)
        innerTopFrame1.pack(fill='both', side='left', expand='True')
        innerTopFrame1.grid()
        innerTopFrame2 = Frame(TopFrame2, bd=5, width=1000, height=48, relief=RIDGE)
        innerTopFrame2.grid()
        innerTopFrame3 = Frame(TopFrame3, bd=5, width=1000, height=280, relief=RIDGE)
        innerTopFrame3.grid()

        lblproveOfID = Label(innerTopFrame1, font=('font', 12, 'bold'), text="Руководитель", bd=10)
        lblproveOfID.grid(row=0, column=0)
        lblproveOfID2 = Label(innerTopFrame1, font=('font', 12, 'bold'), text=name, bd=10)
        lblproveOfID2.grid(row=0, column=1)
        lbltext= Entry(innerTopFrame1, font=('font', 12, 'bold'), bd=5, width=32, justify='left',textvariable=name)

        lblstrdel= Label(TopFrame4, font=('font', 12, 'bold'), text="         Удалить по ID строки:       ", bd=10)
        lblstrdel.grid(row=0,column=0)
        txtstrdel = Entry(TopFrame4, font=('font', 12, 'bold'), bd=5, width=10, justify='left')
        txtstrdel.grid(row=0, column=1)

        lblgetid = Label(TopFrame4, font=('font', 12, 'bold'),text="          Номер строки для автозаполнения:       ",bd=10)
        lblgetid.grid(row=0, column=3)
        txtgetid = Entry(TopFrame4, font=('font', 12, 'bold'), bd=5, width=10, justify='left')
        txtgetid.grid(row=0, column=4)

        lbloperator_f = Label(TopFrame6, font=('font', 10, 'bold'), text="Фильтр-Оператор", bd=10)
        lbloperator_f.grid(row=0, column=0)
        cbooperator_f = ttk.Combobox(TopFrame6, font=('font', 10, 'bold'), width=15)
        cbooperator_f['value'] = DatabaseForm.DataEntry1(name)
        cbooperator_f.current()
        cbooperator_f.grid(row=0, column=1)

        lblRegistrationDate_f = Label(TopFrame6, font=('font', 10, 'bold'), text="                                                                       Оплатит до", bd=10)
        lblRegistrationDate_f.grid(row=0, column=4)
        cboRegistrationDate_f = DateEntry(TopFrame6, locale='RU', width=12, background='lightblue',foreground='white', borderwidth=2, date_pattern='dd.mm.yyyy')
        cboRegistrationDate_f.grid(row=0, column=5)


        lblgroup = Label(innerTopFrame1, font=('font', 12, 'bold'), text="Группа", bd=10)
        lblgroup.grid(row=1, column=0)
        cbogroup = ttk.Combobox(innerTopFrame1, font=('font', 12, 'bold'), width=32)
        cbogroup['value'] = DatabaseForm.DataGroups(name)
        cbogroup.current(0)
        cbogroup.grid(row=1, column=1)

        lbloperator = Label(innerTopFrame1, font=('font', 12, 'bold'), text="Оператор", bd=10)
        lbloperator.grid(row=2, column=0)
        cbooperator = ttk.Combobox(innerTopFrame1, font=('font', 12, 'bold'), width=32)
        cbooperator['value'] = DatabaseForm.DataEntry1(name)
        cbooperator.current()
        cbooperator.grid(row=2, column=1)

        lblReference = Label(innerTopFrame1, font=('font', 12, 'bold'), text="Пин клиента", bd=10)
        lblReference.grid(row=0, column=2)
        txtReference = Text(innerTopFrame1, font=('font', 12, 'bold'), bd=5, width=32, height=1)#, justify='left')
        txtReference.grid(row=0, column=3)

        lblSumofPay = Label(innerTopFrame1, font=('font', 12, 'bold'), text="Сумма или кол-во заказа", bd=10)
        lblSumofPay.grid(row=1, column=2)
        txtSumofPay = Text(innerTopFrame1, font=('font', 12, 'bold'), bd=5, width=32,height=1)#, justify='left')
        txtSumofPay.grid(row=1, column=3)

        lblDate = Label(innerTopFrame1, font=('font', 12, 'bold'), text="Дата внесения", bd=10)
        lblDate.grid(row=2, column=2)
        lblDate = Label(innerTopFrame1, font=('font', 10, 'bold'), text=time.strftime("%d.%m.%Y"),bd=10)  # пОМЕНЯЙ ДАТУ НА ДЭЙТТАЙМ
        lblDate.grid(row=2, column=3)
        lbltextday= Entry(innerTopFrame1, font=('font', 12, 'bold'), bd=5, width=32, justify='left',textvariable=time.strftime("%d.%m.%Y"))



        smthg= Label(innerTopFrame1, font=('font', 12, 'bold'), text=" ", bd=10)
        smthg.grid(row=1, column=7)

        lblRegistrationDate = Label(innerTopFrame1, font=('font', 12, 'bold'), text="Оплатит до", bd=10)
        lblRegistrationDate.grid(row=3, column=0)
        cboRegistrationDate = DateEntry(innerTopFrame1, locale='RU', width=12, background='lightblue',
                                        foreground='white', borderwidth=2, date_pattern='dd.mm.yyyy')
        cboRegistrationDate.grid(row=3, column=1)

        lblstatus = Label(innerTopFrame1, font=('font', 12, 'bold'), text="Статус", bd=10)
        lblstatus.grid(row=3, column=2)
        cbostatus = ttk.Combobox(innerTopFrame1, font=('font', 12, 'bold'), width=32)
        cbostatus['value'] = ('', 'Ожидаем', 'Оплачено', 'Отказ')
        cbostatus.current(0)
        cbostatus.grid(row=3, column=3)

        lblAdress = Label(innerTopFrame1, font=('font', 12, 'bold'), text="Комментарий", bd=10)
        lblAdress.grid(row=4, column=0)
        txtAdress = Text(innerTopFrame1, font=('font', 12, 'bold'), bd=5, width=95,height=1)#, justify='left')
        txtAdress.grid(row=4, column=1, columnspan=3)
        tree=ttk.Treeview(innerTopFrame3,height=10,columns=3)
        dataf= DatabaseForm.sqloutof(name)
        tree["column"]= list(dataf.columns)
        tree["show"]="headings"

        for column in tree["column"]:
            tree.column('' + str(column), width=101, stretch=0)
            tree.heading(column,text=column)
        dataf_rows=dataf.to_numpy().tolist()
        for row in dataf_rows:
            tree.insert("","end",values=row)
        tree.grid(row=4, column=0)


        def Reset():# Кнопка очистк
            cbogroup.delete(0,END)
            cbooperator.delete(0,END)
            txtReference.delete(0.0,END)
            txtSumofPay.delete(0.0,END)
            cboRegistrationDate.delete(0,END)
            cbostatus.delete(0, END)
            txtAdress.delete(0.0, END)
        def iExit(): # Выход из программы
            iExit= tkinter.messagebox.askyesno("Наработки", "Для выхода нажмите <Да>")
            if iExit > 0:
                root.destroy()
                return

        def sqlinput():
            if len (cbostatus.get())!=0:
                tree.delete(*tree.get_children())
                DatabaseForm.sqlinto(name, cbogroup.get(), cbooperator.get(), txtReference.get("1.0", 'end-1c'), txtSumofPay.get("1.0", 'end-1c'), datetoday, cboRegistrationDate.get(), cbostatus.get(), txtAdress.get("1.0", 'end-1c'))
                tree2 = ttk.Treeview(innerTopFrame3, height=10, columns=3)
                dataf2 = DatabaseForm.sqloutof(name)
                tree2["column"] = list(dataf2.columns)
                tree2["show"] = "headings"
                for column2 in tree2["column"]:
                    tree2.column('' + str(column2), width=101, stretch=0)
                    tree2.heading(column2, text=column2)
                dataf_rows2 = dataf2.to_numpy().tolist()
                for row in dataf_rows2:
                    tree2.insert("", "end", values=row)
                tree2.grid(row=4, column=0)
                txtReference.delete(0.0, END)
                txtSumofPay.delete(0.0, END)
                cbostatus.delete(0, END)
                txtAdress.delete(0.0, END)





        def delete_id():
            if DatabaseForm.del_string(txtstrdel.get())==1:
                tree2 = ttk.Treeview(innerTopFrame3, height=10, columns=3)
                dataf2 = DatabaseForm.sqloutof(name)
                tree2["column"] = list(dataf2.columns)
                tree2["show"] = "headings"
                for column2 in tree2["column"]:
                    tree2.column('' + str(column2), width=101, stretch=0)
                    tree2.heading(column2, text=column2)
                dataf_rows2 = dataf2.to_numpy().tolist()
                for row in dataf_rows2:
                    tree2.insert("", "end", values=row)
                tree2.grid(row=4, column=0)
                txtstrdel.delete(0,END)

        def insert_in():
            # Сначала чистим все поля
            cbooperator.delete(0, END)
            txtReference.delete(0.0, END)
            txtSumofPay.delete(0.0, END)
            cboRegistrationDate.delete(0, END)
            cbostatus.delete(0, END)
            txtAdress.delete(0.0, END)

            # Забираем строку из базы по айди записи

            df= DatabaseForm.look_alike(txtgetid.get())

            #Вставляем в табл
            txtSumofPay.insert('1.0',df['Сумма'].values[0])
            cbooperator.insert(INSERT,df['Оператор'].values[0])
            cboRegistrationDate.insert(INSERT,df['Оплатит до'].values[0])
            txtReference.insert(INSERT,df['Пин'].values[0])

        def filter_operator():

            tree2 = ttk.Treeview(innerTopFrame3, height=10, columns=3)
            dataf2 = DatabaseForm.filter(operator=cbooperator_f.get())
            tree2["column"] = list(dataf2.columns)
            tree2["show"] = "headings"
            for column2 in tree2["column"]:
                tree2.column('' + str(column2), width=101, stretch=0)
                tree2.heading(column2, text=column2)
            dataf_rows2 = dataf2.to_numpy().tolist()
            for row in dataf_rows2:
                tree2.insert("", "end", values=row)
            tree2.grid(row=4, column=0)

        def fliter_date():

            tree2 = ttk.Treeview(innerTopFrame3, height=10, columns=3)
            dataf2 = DatabaseForm.filter(date=cboRegistrationDate_f.get(), ruk=name)
            tree2["column"] = list(dataf2.columns)
            tree2["show"] = "headings"
            for column2 in tree2["column"]:
                tree2.column('' + str(column2), width=101, stretch=0)
                tree2.heading(column2, text=column2)
            dataf_rows2 = dataf2.to_numpy().tolist()
            for row in dataf_rows2:
                tree2.insert("", "end", values=row)
            tree2.grid(row=4, column=0)


        def clear_oper_date(): #Возвращает таблицу к исходному состоянию
            tree2 = ttk.Treeview(innerTopFrame3, height=10, columns=3)
            dataf2 = DatabaseForm.sqloutof(name)
            tree2["column"] = list(dataf2.columns)
            tree2["show"] = "headings"
            for column2 in tree2["column"]:
                tree2.column('' + str(column2), width=101, stretch=0)
                tree2.heading(column2, text=column2)
            dataf_rows2 = dataf2.to_numpy().tolist()
            for row in dataf_rows2:
                tree2.insert("", "end", values=row)
            tree2.grid(row=4, column=0)

        btnAddNew = Button(innerTopFrame2, pady=1, bd=4, fg='black', font=('font', 16, 'bold'), width=18, height=1,text="Внести наработку",command=sqlinput).grid(row=0, column=0, padx=3)
        btnAddNew = Button(innerTopFrame2, pady=1, bd=4, fg='darkblue', bg= 'lightblue', font=('font', 16, 'bold'), width=18, height=1, text=f"{round(DatabaseForm.sbivaemost(name) * 100)}%- Сбываемость").grid(row=0, column=1, padx=3)#Тут была команда экзекер
        btnAddNew = Button(innerTopFrame2, pady=1, bd=4, fg='black', font=('font', 16, 'bold'), width=18, height=1,text="Очистить форму",command= Reset).grid(row=0, column=2, padx=3)
        btnAddNew = Button(innerTopFrame2, pady=1, bd=4, fg='black', font=('font', 16, 'bold'), width=18, height=1,text="Выйти",command= iExit).grid(row=0, column=3, padx=3)
        btnAddNew = Button(TopFrame4, pady=1, bd=4,bg= 'lightblue', fg='black',font=('font', 12, 'bold'), width=7, height=1,text="Удалить",command= delete_id).grid(row=0, column=2, padx=3)
        btnAddNew = Button(TopFrame4, pady=1, bd=4, bg= 'lightblue', fg='black', font=('font', 12, 'bold'), width=7, height=1,text="Отразить ", command=insert_in).grid(row=0, column=5, padx=3)
        btnAddNew = Button(TopFrame6, pady=1, bd=4,bg='lightblue', fg='black', font=('font', 10, 'bold'), width=15, height=1,text="Применить", command=filter_operator).grid(row=0, column=3, padx=3)
        btnAddNew = Button(TopFrame6, pady=1, bd=4,bg= 'lightblue', fg='black', font=('font', 10, 'bold'), width=15, height=1,text="Применить", command=fliter_date).grid(row=0, column=6, padx=3)
        btnAddNew = Button(TopFrame6, pady=1, bd=4, bg='grey', fg='black', font=('font', 10, 'bold'), width=15,height=1, text="Сброс",command=clear_oper_date).grid(row=0, column=4, padx=3)
        root.mainloop()


btnAddNew = Button(Frame1,pady=1,bd=4,fg='black',font=('font',16,'bold'),width=15,height=1,text="Войти",command=zz,bg="white").grid(row=3,column=0,padx=3)
Button(Frame1,width=35,pady=77,text="go",bg='White',fg='black',border=0).place(x=35,y=200)




root1.mainloop()