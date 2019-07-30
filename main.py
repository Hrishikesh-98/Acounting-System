import sqlite3
from PyQt5.QtWidgets import (QLineEdit, QLabel, QPushButton, QWidget, QMainWindow, QMessageBox,
                             QApplication, QFrame, QHBoxLayout, QCheckBox, QTableWidget, QTableWidgetItem, QTextEdit)
import sys
import calendar
global connection
global day_name
global Database_name
global table_name
global recname
global indicator


class MainPage(QWidget):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.action = QLabel("What do you want to perform?", self)
        self.action.setFixedSize(400, 50)
        self.action.move(150, 200)
        self.dbname_label = QLabel("Enter Year", self)
        self.enter_dbname = QLineEdit(self)
        self.create_connection = QPushButton("Create Connection", self)
        self.create_table = QPushButton("Create Table", self)
        self.create_table.setFixedSize(150,30)
        self.use_table = QPushButton("Use Table", self)
        self.use_table.setFixedSize(150, 30)
        self.modify_table = QPushButton("Modify Table", self)
        self.modify_table.setFixedSize(150, 30)
        self.quit = QPushButton("Quit", self)
        self.dbname_label.move(150, 150)
        self.enter_dbname.move(300,150)
        self.quit.setFixedSize(150, 30)
        self.create_table.move(150,300)
        self.use_table.move(350, 300)
        self.modify_table.move(250, 400)
        self.quit.move(250, 500)
        self.create_connection.move(450, 150)

    def creating_connection(self):
        if self.enter_dbname.text() is "":
            QMessageBox.about(self, "info", "Enter Year")
        else:
            global connection, Database_name, connection_tab
            Database_name = "'" + self.enter_dbname.text() + ".db'"
            connection = sqlite3.connect(Database_name)
            print('connection created')

class TablenamePage(QWidget):
    def __init__(self, parent= None):
        super(TablenamePage, self).__init__(parent)
        self.table_name_to_use = QLabel("Enter Month", self)
        self.enter_table_name_to_use = QLineEdit(self)
        self.use_button = QPushButton("Use",self)
        self.cancel = QPushButton("Cancel/Back", self)
        self.cancel.move(380, 400)
        self.useframe = QFrame(self)
        self.uselayout = QHBoxLayout()
        self.useframe.setLayout(self.uselayout)
        self.uselayout.addWidget(self.table_name_to_use)
        self.uselayout.addWidget(self.enter_table_name_to_use)
        self.useframe.setGeometry(150, 200, 400, 100)
        self.use_button.move(280,400)



class CreateTablePage(QWidget):
    def __init__(self, parent=None):
        super(CreateTablePage, self).__init__(parent)
        self.new_tablename = QLabel("Enter New Month", self)
        self.enter_new_tablename = QLineEdit(self)
        self.old_tablename = QLabel("Enter Old Month", self)
        self.enter_old_tablename = QLineEdit(self)
        self.create = QPushButton("Create", self)
        self.cancel = QPushButton("Cancel/Back", self)
        self.cancel.move(380, 400)
        self.createframe = QFrame(self)
        self.createlayout = QHBoxLayout()
        self.createframe.setLayout(self.createlayout)
        self.createlayout.addWidget(self.new_tablename)
        self.createlayout.addWidget(self.enter_new_tablename)
        self.createframe.setGeometry(150, 200, 400, 100)

        self.oldframe = QFrame(self)
        self.oldlayout = QHBoxLayout()
        self.oldframe.setLayout(self.oldlayout)
        self.oldlayout.addWidget(self.old_tablename)
        self.oldlayout.addWidget(self.enter_old_tablename)
        self.oldframe.setGeometry(150, 300, 400, 100)

        self.create.move(280, 400)

    def creating_new_table(self):
        try:
            global connection
            new_tablename = self.enter_new_tablename.text()
            old_tablename = self.enter_old_tablename.text()
            query = "CREATE TABLE " + new_tablename + "(name char(100) UNIQUE);"
            connection.execute(query)
            for i in range(1,32):
                query = "ALTER TABLE " + new_tablename + " ADD COLUMN day_" + str(i) + " varchar(100);"
                connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN total varchar(100);"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN payment_due int;"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN phone_no varchar(200);"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN address varchar(300);"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN security int;"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN jar_remaining int;"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN capsule_remaining int;"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN cust_id int;"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN status char(10);"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN balance int;"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN remark varchar(1000);"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + " ADD COLUMN customer varchar(1000);"
            connection.execute(query)

            query = "CREATE TABLE " + new_tablename+ "_paid " + "(for_i int, name char(100) UNIQUE);"
            connection.execute(query)
            for i in range(1,32):
                query = "ALTER TABLE " + new_tablename + "_paid ADD COLUMN day_" + str(i) + " int;"
                connection.execute(query)
            query = "INSERT INTO " + new_tablename+ "_paid" + "(for_i, name) values(1, ' ');"
            connection.execute(query)
            query = "ALTER TABLE " + new_tablename + "_paid ADD COLUMN sum int;"
            connection.execute(query)
            connection.commit()

            if old_tablename is not '':
                query = "SELECT name, phone_no, address, security, cust_id, status, customer FROM " + old_tablename + ";"
                names = connection.execute(query)
                query = "SELECT for_i FROM " + old_tablename + "_paid WHERE name=' '";
                for_i = connection.execute(query)
                for iis in for_i:
                    query = "UPDATE "+ new_tablename + "_paid SET for_i=" + str(iis[0]) + " WHERE name=' ';"
                    connection.execute(query)
                for row in names:
                    query = "INSERT INTO "+ new_tablename + "(name, phone_no, address, security, " \
                                                            "jar_remaining, capsule_remaining, payment" \
                                                            "_due, cust_id, status, balance, remark, customer) values(" \
                                                            "'" + row[0] + "','" + str(row[1]) + "','"\
                                                            + str(row[2]) + "'," + str(row[3]) + ",0,0,0,"\
                            + str(row[4]) + ",'" + str(row[5])+ "',0,' ','" + str(row[6]) + "');"
                    connection.execute(query)
                    query = "INSERT INTO "+ new_tablename + "_paid (name, sum, for_i) values('" + row[0] + "',0," + str(row[4])+ ");"
                    connection.execute(query)
                    for i in range(1,32):
                        query = "UPDATE " + new_tablename + "_paid set day_" + str(i) + "=0 WHERE name='" + str(row[0]) + "';"
                        connection.execute(query)
                    connection.commit()

                    query = "UPDATE " + new_tablename + " SET total='0@0@0' WHERE name='" + str(row[0]) + "';"
                    connection.execute(query)

                    for i in range(1, 32):
                        query = "UPDATE " + new_tablename + " SET day_" + str(
                            i) + "='0a0a0a0a0' WHERE name='" + str(row[0]) + "';"
                        connection.execute(query)

                    connection.commit()

            print("Table Created")

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't create table, either it already exists or there is some other issue")
            '''try:
                query = "Drop Table " + self.enter_new_tablename.text() + ";"
                connection.execute(query)
                query = "Drop Table " + self.enter_new_tablename.text() + "_paid;"
                connection.execute(query)
                connection.commit()
            except sqlite3.OperationalError:
                pass'''

        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")

class AddRemarkPage(QWidget):
    def __init__(self, parent=None):
        super(AddRemarkPage, self).__init__(parent)
        self.add_client_naame = QLabel("Enter Client Name", self)
        self.enter_add_client_name = QLineEdit(self)
        self.add_remark = QLabel("Enter remark", self)
        self.enter_remark = QTextEdit(self)
        self.add_button = QPushButton("Add",self)
        self.cancel = QPushButton("Cancel\Back",self)
        self.add_client_naame.move(100,100)
        self.enter_add_client_name.move(250,100)
        self.add_remark.move(100,200)
        self.enter_remark.setFixedSize(300,200)
        self.enter_remark.move(300,200)
        self.add_button.move(200,500)
        self.cancel.move(350,500)

    def addingremark(self):
        try:
            global connection, table_name
            name = self.enter_add_client_name.text()
            remark = self.enter_remark.toPlainText()
            query = "SELECT remark FROM "+ table_name + " WHERE name='" + name + "';"
            record = connection.execute(query)
            for rec in record:
                prev_remark = str(rec[0])
            remark = prev_remark + ", " + remark
            connection.execute(query)
            query = "UPDATE "+ table_name + " SET remark='" + remark + "' WHERE name='" + name + "';"
            connection.execute(query)
            print("Remark added")
            connection.commit()
        except sqlite3.OperationalError:
            QMessageBox.about(self,"info","couldn't add remark something went in entering values")
        except UnboundLocalError:
            QMessageBox.about(self,"info", "something went wrong try again")
        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")


class UseTablePage(QWidget):
    def __init__(self, parent=None):
        super(UseTablePage, self).__init__(parent)
        self.action = QLabel("What do you want to perform?", self)
        self.action.setFixedSize(400, 50)
        self.action.move(150, 50)
        self.add_entry = QPushButton("Add entry", self)
        self.add_entry.setFixedSize(150,30)
        self.add_regular_entry = QPushButton("Add Regular entries", self)
        self.add_regular_entry.setFixedSize(150,30)
        self.view_record = QPushButton("View Record", self)
        self.view_record.setFixedSize(150, 30)
        self.find_client = QPushButton("Find Client", self)
        self.find_client.setFixedSize(150, 30)
        self.client_closed = QPushButton("Client CLosed", self)
        self.client_closed.setFixedSize(150, 30)
        self.show_closed_clients = QPushButton("Show Closed Clients List", self)
        self.show_closed_clients.setFixedSize(150, 30)
        self.add_remark = QPushButton("Add Remark", self)
        self.add_remark.setFixedSize(150, 30)
        self.cancel = QPushButton("Cancel/Back", self)
        self.cancel.setFixedSize(150, 30)
        self.add_entry.move(150,150)
        self.add_regular_entry.move(350,150)
        self.view_record.move(150, 275)
        self.find_client.move(350, 275)
        self.client_closed.move(150,400)
        self.show_closed_clients.move(350,400)
        self.add_remark.move(150,500)
        self.cancel.move(350, 500)

class ModifyTablePage(QWidget):
    def __init__(self, parent=None):
        super(ModifyTablePage, self).__init__(parent)
        self.add_client = QPushButton("Add Client", self)
        self.add_client.setFixedSize(150, 30)
        self.delete_client = QPushButton("Delete Client", self)
        self.delete_client.setFixedSize(150, 30)
        self.modify_client = QPushButton("Modify Client", self)
        self.modify_client.setFixedSize(150, 30)
        self.change_serial = QPushButton("Change Sequence", self)
        self.change_serial.setFixedSize(150, 30)
        self.add_client.move(200,200)
        self.modify_client.move(400,200)
        self.delete_client.move(200,300)
        self.change_serial.move(400,300)

        self.cancel = QPushButton("Cancel/Back", self)
        self.cancel.move(300, 500)

class AddEntryPage(QWidget):
    def __init__(self, parent=None):
        super(AddEntryPage, self).__init__(parent)
        self.client_name = QLabel("Enter Client Name", self)
        self.enter_client_name = QLineEdit(self)
        self.date = QLabel("Enter Date", self)
        self.enter_date = QLineEdit(self)
        self.jargiven = QLabel("Enter Jar Supplied", self)
        self.enter_jargiven = QLineEdit(self)
        self.jartaken = QLabel("Enter Jar Returned", self)
        self.enter_jartaken = QLineEdit(self)
        self.capsulegiven = QLabel("Enter Capsule Supplied", self)
        self.enter_capsulegiven = QLineEdit(self)
        self.capsuletaken = QLabel("Enter Capsule Returned", self)
        self.enter_capsuletaken = QLineEdit(self)
        self.one_can = QLabel("Enter amount of one capsule", self)
        self.enter_one_can = QLineEdit(self)
        self.one_jar = QLabel("Enter amount of one jar", self)
        self.enter_one_jar = QLineEdit(self)
        self.paid = QLabel("Enter amount paid", self)
        self.enter_paid = QLineEdit(self)
        self.enter_paid.setText('0')
        self.add = QPushButton("Add", self)
        self.cancel = QPushButton("Cancel/Back", self)
        self.cancel.move(380, 560)
        self.addnameframe = QFrame(self)
        self.addnamelayout = QHBoxLayout()
        self.addnameframe.setLayout(self.addnamelayout)
        self.addnamelayout.addWidget(self.client_name)
        self.addnamelayout.addWidget(self.enter_client_name)
        self.addnameframe.setGeometry(150, 100, 400, 100)

        self.adddateframe = QFrame(self)
        self.adddatelayout = QHBoxLayout()
        self.adddateframe.setLayout(self.adddatelayout)
        self.adddatelayout.addWidget(self.date)
        self.adddatelayout.addWidget(self.enter_date)
        self.adddateframe.setGeometry(150, 150, 400, 100)

        self.addjargivenframe = QFrame(self)
        self.addjargivenlayout = QHBoxLayout()
        self.addjargivenframe.setLayout(self.addjargivenlayout)
        self.addjargivenlayout.addWidget(self.jargiven)
        self.addjargivenlayout.addWidget(self.enter_jargiven)
        self.addjargivenframe.setGeometry(150, 200, 400, 100)

        self.addjartakenframe = QFrame(self)
        self.addjartakenlayout = QHBoxLayout()
        self.addjartakenframe.setLayout(self.addjartakenlayout)
        self.addjartakenlayout.addWidget(self.jartaken)
        self.addjartakenlayout.addWidget(self.enter_jartaken)
        self.addjartakenframe.setGeometry(150, 250, 400, 100)

        self.addcapsulegivenframe = QFrame(self)
        self.addcapsulegivenlayout = QHBoxLayout()
        self.addcapsulegivenframe.setLayout(self.addcapsulegivenlayout)
        self.addcapsulegivenlayout.addWidget(self.capsulegiven)
        self.addcapsulegivenlayout.addWidget(self.enter_capsulegiven)
        self.addcapsulegivenframe.setGeometry(150, 300, 400, 100)

        self.addcapsuletakenframe = QFrame(self)
        self.addcapsuletakenlayout = QHBoxLayout()
        self.addcapsuletakenframe.setLayout(self.addcapsuletakenlayout)
        self.addcapsuletakenlayout.addWidget(self.capsuletaken)
        self.addcapsuletakenlayout.addWidget(self.enter_capsuletaken)
        self.addcapsuletakenframe.setGeometry(150, 350, 400, 100)


        self.addonejarframe = QFrame(self)
        self.addonejarlayout = QHBoxLayout()
        self.addonejarframe.setLayout(self.addonejarlayout)
        self.addonejarlayout.addWidget(self.one_jar)
        self.addonejarlayout.addWidget(self.enter_one_jar)
        self.addonejarframe.setGeometry(350, 400, 200, 100)

        self.addonecanframe = QFrame(self)
        self.addonecanlayout = QHBoxLayout()
        self.addonecanframe.setLayout(self.addonecanlayout)
        self.addonecanlayout.addWidget(self.one_can)
        self.addonecanlayout.addWidget(self.enter_one_can)
        self.addonecanframe.setGeometry(150, 400, 200, 100)

        self.addpaidframe = QFrame(self)
        self.addpaidlayout = QHBoxLayout()
        self.addpaidframe.setLayout(self.addpaidlayout)
        self.addpaidlayout.addWidget(self.paid)
        self.addpaidlayout.addWidget(self.enter_paid)
        self.addpaidframe.setGeometry(150, 450, 400, 100)
        self.add.move(280, 560)

    def adding_entry(self):
        try:
            global connection, table_name, connection_tab
            name = self.enter_client_name.text()
            day = self.enter_date.text()
            query = "SELECT * FROM " + table_name + " WHERE name= '" + name + "';"
            rows = connection.execute(query)
            for row in rows:
                jar_rem = int(str(row[37]))
                can_rem = int(str(row[38]))
                due_prev = int(str(row[33]))
                prev_jar = str(row[int(day)]).split("a",2)[0]
                prev_cap = str(row[int(day)]).split("a",2)[1]
                x2 = 0
                total_jar = 0
                total_can = 0
                for k in range(1, 32):
                    temp = int(str(row[k]).split('a', 4)[0])
                    total_jar = total_jar + temp
                    temp = int(str(row[k]).split('a', 4)[1])
                    total_can = total_can + temp
                total_final = total_jar + total_can
                if int(str(row[int(day)]).split('a',4)[2]) > 0:
                    x = str(row[int(day)]).split('a',4)
                    jar_take = x[3]
                    cap_take = x[4]
                    jar_pay = x[0]
                    cap_pay = x[1]
                    x2 = x[2]
                    if int(self.enter_one_can.text()) > 0:
                        canpay = int(self.enter_one_can.text())
                    else:
                        canpay = 30
                    if int(self.enter_one_jar.text()) > 0:
                        jarpay = int(self.enter_one_jar.text())
                    else:
                        jarpay = 30
                if int(x2) > 0:
                    jar_rem = jar_rem - (int(jar_pay) - int(jar_take))
                    can_rem = can_rem - (int(cap_pay) - int(cap_take))
                    due_prev = due_prev - (int(jar_pay))*jarpay - (int(cap_pay))*canpay
                    total_jar = total_jar - int(prev_jar)
                    total_can = total_can - int(prev_cap)
                else:
                    pass

            jar_given = int(self.enter_jargiven.text())
            can_given = int(self.enter_capsulegiven.text())
            jar_taken = int(self.enter_jartaken.text())
            can_taken = int(self.enter_capsuletaken.text())
            jar_remaining = jar_rem + jar_given - jar_taken
            can_remaining = can_rem + can_given - can_taken
            total = jar_given + can_given
            x = str(self.enter_jargiven.text()) + "a" + self.enter_capsulegiven.text() + \
                "a" + str(total) + "a" + self.enter_jartaken.text() + "a" + self.enter_capsuletaken.text()
            query = "UPDATE " + table_name + " SET day_"+ day + "='" + str(x) + "' WHERE name ='" +name+ "';"
            connection.execute(query)
            query = "UPDATE " + table_name + " SET jar_remaining ="+ str(jar_remaining)+" WHERE name = '"+name+"';"
            connection.execute(query)
            query = "UPDATE " +table_name +" SET capsule_remaining ="+str(can_remaining)+" WHERE name = '"+name+"';"
            connection.execute(query)
            query = "SELECT * FROM " + table_name + " WHERE name = '" + name + "';"
            record = connection.execute(query)
            sum = 0
            for rec in record:
                for i in range(1,32):
                    x = str(rec[i]).split('a',4)
                    if int(x[2]) == 0:
                        sum = sum + 0
                    else:
                        sum = sum + int(x[2])
            total_jar = total_jar+jar_given
            total_can = total_can + can_given
            total_final = total_jar + total_can
            query = "UPDATE " + table_name + " SET total ='" + str(total_jar) + "@"+ str(total_can)\
                    + "@" + str(total_final) + "' WHERE name = '" + name + "';"
            connection.execute(query)
            payment_due = due_prev + jar_given * int(self.enter_one_jar.text()) +\
                          can_given * int(self.enter_one_can.text())
            query = "UPDATE " + table_name + " SET payment_due =" + str(payment_due) + " WHERE name = '" + name + "';"
            connection.execute(query)
            connection.commit()
            query = "UPDATE " + table_name + "_paid SET day_" + str(day)\
                    + "=" + self.enter_paid.text() + " WHERE name='" + self.enter_client_name.text() + "';"
            connection.execute(query)
            query = "SELECT * FROM " + table_name + "_paid WHERE name='" + self.enter_client_name.text() + "';"
            amt = connection.execute(query)
            amtt = 0
            for amounts in amt:
                for i in range(1,32):
                    amtt = amtt + int(str(amounts[i+1]))
            query = "UPDATE " + table_name + "_paid SET sum=" + str(amtt)\
                    + " WHERE name='" + self.enter_client_name.text() + "';"
            connection.execute(query)
            bal = payment_due - amtt
            query = "UPDATE " + table_name + " SET balance=" + str(bal)\
                    + " WHERE name='" + self.enter_client_name.text() + "';"
            connection.execute(query)
            connection.commit()
            print("Entry added")

        except ValueError:
            QMessageBox.about(self, "Info", "Couldn't add entry, something went wrong in entering values")

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't add entry, something went wrong")

        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")

class ViewRecordPage(QWidget):
    def __init__(self, parent=None):
        super(ViewRecordPage, self).__init__(parent)
        self.view_client_name = QLabel("Enter Client Name", self)
        self.enter_view_client_name = QLineEdit(self)
        self.month = QLabel("Enter Month", self)
        self.enter_month = QLineEdit(self)
        self.view = QPushButton("View", self)
        self.cancel = QPushButton("Cancel/Back", self)
        self.cancel.move(380, 400)
        self.viewnameframe = QFrame(self)
        self.viewnamelayout = QHBoxLayout()
        self.viewnameframe.setLayout(self.viewnamelayout)
        self.viewnamelayout.addWidget(self.view_client_name)
        self.viewnamelayout.addWidget(self.enter_view_client_name)
        self.viewnameframe.setGeometry(150, 200, 400, 100)
        recname = self.enter_view_client_name.text()
        self.entermonthframe = QFrame(self)
        self.entermonthlayout = QHBoxLayout()
        self.entermonthframe.setLayout(self.entermonthlayout)
        self.entermonthlayout.addWidget(self.month)
        self.entermonthlayout.addWidget(self.enter_month)
        self.entermonthframe.setGeometry(150, 300, 400, 100)
        self.view.move(280, 400)


class FindClientPage(QWidget):
    def __init__(self, parent=None):
        super(FindClientPage, self).__init__(parent)
        self.ascending = QCheckBox("Ascending", self)
        #self.showclient = FindingClients()
        self.descending = QCheckBox("Descending", self)
        self.alphabetically = QCheckBox("Alphabetically", self)
        self.acc_to_amount = QCheckBox("According to amount", self)
        self.greater_than_equal_to = QCheckBox("Greater than equal to", self)
        self.less_than_equal_to = QCheckBox("Less than equal to", self)
        self.amount = QLabel("Enter amount", self)
        self.enter_amount = QLineEdit(self)
        self.find_client = QPushButton("Find", self)
        self.cancel = QPushButton("Cancel/Back", self)
        self.ascending.move(100,100)
        self.descending.move(300,100)
        self.alphabetically.move(100,200)
        self.acc_to_amount.move(300,200)
        self.amount.move(100,300)
        self.enter_amount.move(300,300)
        self.greater_than_equal_to.move(100,400)
        self.less_than_equal_to.move(300,400)
        self.find_client.move(180, 500)
        self.cancel.move(280,500)

    def finding_client(self):
        if self.ascending.isChecked():
            if self.alphabetically.isChecked():
                #query = "SELECT name, total, payment_due, phone_no, address FROM "+ table_name + " ORDER BY name ASC;"
                query = "SELECT * FROM "+ table_name + " WHERE status='OPEN' ORDER BY name ASC;"
            elif self.acc_to_amount.isChecked():
                if self.greater_than_equal_to.isChecked():
                    #query = "SELECT name, total, payment_due, phone_no, address FROM "+ table_name +\
                            #" WHERE payment_due >=" + str(self.enter_amount.text()) + " ORDER BY payment_due ASC ;"
                    query = "SELECT * FROM " + table_name + \
                            " WHERE balance >=" + str(self.enter_amount.text()) + " and status='OPEN' ORDER BY balance ASC;"

                elif self.less_than_equal_to.isChecked():
                    #query = "SELECT name, total, payment_due, phone_no, address FROM "+ table_name +\
                            #" WHERE payment_due <=" + str(self.enter_amount.text()) + " ORDER BY payment_due ASC ;"
                    query = "SELECT * FROM "+ table_name +\
                            " WHERE balance <=" + str(self.enter_amount.text()) + " and status='OPEN'ORDER BY balance ASC;"
                else:
                    #query = "SELECT name, total, payment_due, phone_no, address FROM "\
                            #+ table_name + " ORDER BY payment_due ASC;"
                    query = "SELECT * FROM "\
                            + table_name + " WHERE status='OPEN' ORDER BY payment_due ASC;"
            else:
                #query = "SELECT name, total, payment_due, phone_no, address FROM " + table_name + " ORDER BY name ASC;"
                query = "SELECT * FROM " + table_name + " WHERE status='OPEN' ORDER BY name ASC;"

        elif self.descending.isChecked():
            if self.alphabetically.isChecked():
                #query = "SELECT name, total, payment_due, phone_no, address FROM " + table_name + " ORDER BY name DESC;"
                query = "SELECT * FROM " + table_name + " WHERE status='OPEN' ORDER BY name DESC;"

            elif self.acc_to_amount.isChecked():
                if self.greater_than_equal_to.isChecked():
                    #query = "SELECT name, total, payment_due, phone_no, address FROM "+ table_name +\
                            #" WHERE payment_due >=" + str(self.enter_amount.text()) + " ORDER BY payment_due DESC ;"
                    query = "SELECT * FROM "+ table_name +\
                            " WHERE balance >=" + str(self.enter_amount.text()) + " and status='OPEN' ORDER BY balance DESC;"

                elif self.less_than_equal_to.isChecked():
                    #query = "SELECT name, total, payment_due, phone_no, address FROM "+ table_name +\
                            #" WHERE payment_due <=" + str(self.enter_amount.text()) + " ORDER BY payment_due DESC ;"
                    query = "SELECT * FROM "+ table_name +\
                            " WHERE balance <=" + str(self.enter_amount.text()) + " and status='OPEN' ORDER BY balance DESC;"
                else:
                    #query = "SELECT name, total, payment_due, phone_no, address FROM "\
                            #+ table_name + " ORDER BY payment_due DESC;"
                    query = "SELECT * FROM "\
                            + table_name + " WHERE status='OPEN' ORDER BY balance DESC;"
            else:
                #query = "SELECT name, total, payment_due, phone_no, address FROM " + table_name + " ORDER BY name DESC;"
                query = "SELECT * FROM " + table_name + " WHERE status='OPEN' ORDER BY name DESC;"

        elif self.acc_to_amount.isChecked():
            if self.greater_than_equal_to.isChecked():
                #query = "SELECT name, total, payment_due, phone_no, address FROM " + table_name +\
                        #" WHERE payment_due >=" + str(self.enter_amount.text()) + ";"
                query = "SELECT * FROM " + table_name + \
                        " WHERE balance >=" + str(self.enter_amount.text()) + " and status='OPEN';"

            elif self.less_than_equal_to.isChecked():
                #query = "SELECT name, total, payment_due, phone_no, address FROM " + table_name +\
                        #" WHERE payment_due <=" + str(self.enter_amount.text()) + ";"
                query = "SELECT * FROM " + table_name + \
                        " WHERE balance <=" + str(self.enter_amount.text()) + " and status='OPEN';"

        else:
            #query = "SELECT name, total, payment_due, phone_no, address FROM " + table_name + " ORDER BY name ASC;"
            query = "SELECT * FROM " + table_name + " WHERE status='OPEN' ORDER BY cust_id ASC;"

        return query

class ClientClosedPage(QWidget):
    def __init__(self, parent=None):
        super(ClientClosedPage, self).__init__(parent)
        self.add_client_name = QLabel("Enter Client Name",self)
        self.enter_add_client_name = QLineEdit(self)
        self.add_jar_returned = QLabel("Enter no. of jars returned",self)
        self.enter_add_jar_returned = QLineEdit(self)
        self.add_cap_returned = QLabel("Enter no. of capsules returned",self)
        self.enter_add_cap_returned = QLineEdit(self)
        self.add_amount = QLabel("Enter Amount Paid",self)
        self.enter_add_amount = QLineEdit(self)
        self.add_remark = QLabel("Enter Remark",self)
        self.enter_remark = QTextEdit(self)
        self.enter_remark.setFixedSize(300,200)
        self.add_table_name = QLabel("Enter Table Name",self)
        self.enter_add_table_name = QLineEdit(self)
        self.close_button = QPushButton("Close", self)
        self.cancel = QPushButton("Cancel/Back", self)
        self.add_client_name.move(100,50)
        self.enter_add_client_name.move(200,50)
        self.add_jar_returned.move(100,100)
        self.enter_add_jar_returned.move(300,100)
        self.add_cap_returned.move(100,150)
        self.enter_add_cap_returned.move(300,150)
        self.add_remark.move(100,300)
        self.enter_remark.move(200,300)
        self.add_table_name.move(100,200)
        self.enter_add_table_name.move(200,200)
        self.add_amount.move(100,250)
        self.enter_add_amount.move(200,250)
        self.close_button.move(200,650)
        self.cancel.move(350,650)

    def closingclient(self):
        try:
            global connection
            table = self.enter_add_table_name.text()
            name = self.enter_add_client_name.text()
            query = "SELECT jar_remaining , capsule_remaining, balance FROM " + table + " WHERE name='" + name + "';"
            record = connection.execute(query)
            query = "SELECT sum FROM " + table + "_paid WHERE name='" + name + "';"
            record2 = connection.execute(query)
            for rec in record:
                jar_rem = int(str(rec[0]))
                cap_rem = int(str(rec[1]))
                bal = int(str(rec[2]))
            for rec2 in record2:
                paid = int(str(rec[0]))
            jar_rem = jar_rem - int(self.enter_add_jar_returned.text())
            cap_rem = cap_rem - int(self.enter_add_cap_returned.text())
            bal = bal - int(self.enter_add_amount.text())
            paid = paid + int(self.enter_add_amount.text())
            query = "UPDATE " + table + " SET status='CLOSED' WHERE name='" + name + "';"
            connection.execute(query)
            query = "UPDATE " + table + " SET jar_remaining=" + str(jar_rem) + " WHERE name='" + name + "';"
            connection.execute(query)
            query = "UPDATE " + table + " SET capsule_remaining=" + str(cap_rem) + " WHERE name='" + name + "';"
            connection.execute(query)
            query = "UPDATE " + table + " SET balance=" + str(bal) + " WHERE name='" + name + "';"
            connection.execute(query)
            query = "UPDATE " + table + "_paid SET sum=" + str(paid) + " WHERE name='" + name + "';"
            connection.execute(query)
            query = "UPDATE " + table + " SET remark='" + str(self.enter_remark.toPlainText()) + "' WHERE name='" + name + "';"
            connection.execute(query)
            connection.commit()
            print("Client Closed")

        except ValueError:
            QMessageBox.about(self, "Info", "Couldn't close client, something went wrong in entering values")

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't close client, something went wrong")

        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")

class AddClientPage(QWidget):
    def __init__(self, parent=None):
        super(AddClientPage, self).__init__(parent)
        self.add_client_name = QLabel("Enter Client Name", self)
        self.enter_add_client_name = QLineEdit(self)
        self.add_client_phone = QLabel("Enter Client Phone Number", self)
        self.enter_add_client_phone = QLineEdit(self)
        self.add_client_address = QLabel("Enter Client Address", self)
        self.enter_add_client_address = QLineEdit(self)
        self.add_security = QLabel("Enter Security Amount", self)
        self.enter_add_security = QLineEdit(self)
        self.add_customer = QLabel("Enter Customer Type", self)
        self.enter_add_customer = QLineEdit(self)
        self.table_to_add = QLabel("Enter table name", self)
        self.enter_table_to_add = QLineEdit(self)
        self.add_client = QPushButton("Add", self)
        self.cancel = QPushButton("Cancel/Back", self)
        self.add_client.move(280,600)
        self.cancel.move(380, 600)
        self.addclientframe = QFrame(self)
        self.addclientlayout = QHBoxLayout()
        self.addclientframe.setLayout(self.addclientlayout)
        self.addclientlayout.addWidget(self.add_client_name)
        self.addclientlayout.addWidget(self.enter_add_client_name)
        self.addclientframe.setGeometry(150, 50, 400, 100)

        self.addclientphoneframe = QFrame(self)
        self.addclientphonelayout = QHBoxLayout()
        self.addclientphoneframe.setLayout(self.addclientphonelayout)
        self.addclientphonelayout.addWidget(self.add_client_phone)
        self.addclientphonelayout.addWidget(self.enter_add_client_phone)
        self.addclientphoneframe.setGeometry(150, 100, 400, 100)

        self.addclientaddressframe = QFrame(self)
        self.addclientaddresslayout = QHBoxLayout()
        self.addclientaddressframe.setLayout(self.addclientaddresslayout)
        self.addclientaddresslayout.addWidget(self.add_client_address)
        self.addclientaddresslayout.addWidget(self.enter_add_client_address)
        self.addclientaddressframe.setGeometry(150, 200, 400, 100)

        self.addsecurityframe = QFrame(self)
        self.addsecuritylayout = QHBoxLayout()
        self.addsecurityframe.setLayout(self.addsecuritylayout)
        self.addsecuritylayout.addWidget(self.add_security)
        self.addsecuritylayout.addWidget(self.enter_add_security)
        self.addsecurityframe.setGeometry(150, 300, 400, 100)

        self.addcustomerframe = QFrame(self)
        self.addcustomerlayout = QHBoxLayout()
        self.addcustomerframe.setLayout(self.addcustomerlayout)
        self.addcustomerlayout.addWidget(self.add_customer)
        self.addcustomerlayout.addWidget(self.enter_add_customer)
        self.addcustomerframe.setGeometry(150, 400, 400, 100)

        self.tableaddframe = QFrame(self)
        self.tableaddlayout = QHBoxLayout()
        self.tableaddframe.setLayout(self.tableaddlayout)
        self.tableaddlayout.addWidget(self.table_to_add)
        self.tableaddlayout.addWidget(self.enter_table_to_add)
        self.tableaddframe.setGeometry(150, 500, 400, 100)

    def adding_client(self):
        try:
            global connection
            tname = self.enter_table_to_add.text()
            query = "SELECT for_i FROM " + tname + "_paid WHERE name=' ';"
            for_i = connection.execute(query)
            for iis in for_i:
                o = int(str(iis[0])) + 1
                query = "UPDATE " + tname + "_paid SET for_i=" + str(o) + " WHERE name=' ';"
                connection.execute(query)
                query = "INSERT INTO " + tname + "(name, phone_no, address, security, jar_remaining," \
                                                 " capsule_remaining, payment_due, total, status, cust_id, balance, remark, customer)values('"\
                                                 + self.enter_add_client_name.text() + "','"\
                                                 + self.enter_add_client_phone.text() + "','" \
                                                 + self.enter_add_client_address.text() + "',"\
                                                 + self.enter_add_security.text() + ",0,0,0, '0@0@0', 'OPEN',"\
                        + str(iis[0]) +",0,' ','" + self.enter_add_customer.text()+ "');"
                connection.execute(query)
                query = "INSERT INTO " + tname + "_paid (name, sum, for_i) values('" + self.enter_add_client_name.text() + "',0," + str(iis[0]) + ");"
                connection.execute(query)
            for i in range(1,32):
                query = "UPDATE " + tname + " SET day_" + str(i) + "='0a0a0a0a0' WHERE name='" + self.enter_add_client_name.text() + "';"
                connection.execute(query)
            for i in range(1,32):
                query = "UPDATE " + tname + "_paid SET day_" + str(i) + "='0' WHERE name='" + self.enter_add_client_name.text() + "';"
                connection.execute(query)
            connection.commit()
            print("client added")
        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't Add client, something went wrong")
        except sqlite3.IntegrityError:
            QMessageBox.about(self, "Info", "Client with this name already exists")
        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")


class MiddleModifyPage(QWidget):
    def __init__(self, parent=None):
        super(MiddleModifyPage, self).__init__(parent)
        self.add_client_name_to_modify = QLabel("Enter Client name", self)
        self.enter_add_client_to_modify = QLineEdit(self)
        self.add_table_name_to_modify = QLabel("Enter Table name", self)
        self.enter_add_table_to_modify = QLineEdit(self)
        self.proceed_button = QPushButton('Proceed', self)
        self.cancel = QPushButton('Cancel/back', self)
        self.modframe = QFrame(self)
        self.modlayout = QHBoxLayout()
        self.modlayout.addWidget(self.add_client_name_to_modify)
        self.modlayout.addWidget(self.enter_add_client_to_modify)
        self.modframe.setLayout(self.modlayout)
        self.modframe.setGeometry(100,100, 600, 200)
        self.modtabframe = QFrame(self)
        self.modtablayout = QHBoxLayout()
        self.modtablayout.addWidget(self.add_table_name_to_modify)
        self.modtablayout.addWidget(self.enter_add_table_to_modify)
        self.modtabframe.setLayout(self.modtablayout)
        self.modtabframe.setGeometry(100,200, 600, 200)
        self.proceed_button.move(250,450)
        self.cancel.move(400,450)


class ModifyClientPage(QWidget):
    def __init__(self, parent=None):
        super(ModifyClientPage, self).__init__(parent)
        self.add_client_name = QLabel("Enter Client Name", self)
        self.enter_add_client_name = QLineEdit(self)
        self.add_client_phone = QLabel("Enter Client Phone Number", self)
        self.enter_add_client_phone = QLineEdit(self)
        self.add_client_address = QLabel("Enter Client Address", self)
        self.enter_add_client_address = QLineEdit(self)
        self.add_security = QLabel("Enter Security Amount", self)
        self.enter_add_security = QLineEdit(self)
        self.add_customer = QLabel("Enter Customer Type", self)
        self.enter_add_customer = QLineEdit(self)
        self.table_to_add = QLabel("Enter table name", self)
        self.enter_table_to_add = QLineEdit(self)
        self.modify_client = QPushButton("Modify", self)
        self.cancel = QPushButton("Cancel/Back", self)
        self.modify_client.move(280,600)
        self.cancel.move(380, 600)
        self.addclientframe = QFrame(self)
        self.addclientlayout = QHBoxLayout()
        self.addclientframe.setLayout(self.addclientlayout)
        self.addclientlayout.addWidget(self.add_client_name)
        self.addclientlayout.addWidget(self.enter_add_client_name)
        self.addclientframe.setGeometry(150, 50, 400, 100)

        self.addclientphoneframe = QFrame(self)
        self.addclientphonelayout = QHBoxLayout()
        self.addclientphoneframe.setLayout(self.addclientphonelayout)
        self.addclientphonelayout.addWidget(self.add_client_phone)
        self.addclientphonelayout.addWidget(self.enter_add_client_phone)
        self.addclientphoneframe.setGeometry(150, 130, 400, 100)

        self.addclientaddressframe = QFrame(self)
        self.addclientaddresslayout = QHBoxLayout()
        self.addclientaddressframe.setLayout(self.addclientaddresslayout)
        self.addclientaddresslayout.addWidget(self.add_client_address)
        self.addclientaddresslayout.addWidget(self.enter_add_client_address)
        self.addclientaddressframe.setGeometry(150, 210, 400, 100)

        self.addsecurityframe = QFrame(self)
        self.addsecuritylayout = QHBoxLayout()
        self.addsecurityframe.setLayout(self.addsecuritylayout)
        self.addsecuritylayout.addWidget(self.add_security)
        self.addsecuritylayout.addWidget(self.enter_add_security)
        self.addsecurityframe.setGeometry(150, 290, 400, 100)

        self.addcustomerframe = QFrame(self)
        self.addcustomerlayout = QHBoxLayout()
        self.addcustomerframe.setLayout(self.addcustomerlayout)
        self.addcustomerlayout.addWidget(self.add_customer)
        self.addcustomerlayout.addWidget(self.enter_add_customer)
        self.addcustomerframe.setGeometry(150, 370, 400, 100)

        self.tableaddframe = QFrame(self)
        self.tableaddlayout = QHBoxLayout()
        self.tableaddframe.setLayout(self.tableaddlayout)
        self.tableaddlayout.addWidget(self.table_to_add)
        self.tableaddlayout.addWidget(self.enter_table_to_add)
        self.tableaddframe.setGeometry(150, 450, 400, 100)

    def givingvalues(self, client_name, tablename):
        try:
            global connection
            query = "SELECT * FROM " + tablename + " WHERE name='" + client_name + "';"
            record = connection.execute(query)
            for rec in record:
                self.enter_add_client_name.setText(str(rec[0]))
                self.name = str([rec[0]])
                self.id = str(rec[39])
                self.enter_add_client_phone.setText(str(rec[34]))
                self.enter_add_client_address.setText(str(rec[35]))
                self.enter_add_security.setText(str(rec[36]))
                self.enter_add_customer.setText(str(rec[43]))


        except ValueError:
            QMessageBox.about(self, "Info", "Couldn't modify client, something went wrong in entering values")

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't modify client, something went wrong")

        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")

    def modifyingvalues(self):
        try:
            global connection
            query = "UPDATE " + self.enter_table_to_add.text() + " SET name='" + self.enter_add_client_name.text()\
                    + "' WHERE cust_id=" + self.id + ";"
            connection.execute(query)
            query = "UPDATE " + self.enter_table_to_add.text() + "_paid SET name='" + self.enter_add_client_name.text()\
                    + "' WHERE for_i=" + self.id + ";"
            connection.execute(query)
            query = "UPDATE " + self.enter_table_to_add.text() + " SET phone_no='" + self.enter_add_client_phone.text()\
                    + "' WHERE name='" + self.enter_add_client_name.text() + "';"
            connection.execute(query)
            query = "UPDATE " + self.enter_table_to_add.text() + " SET address='" + self.enter_add_client_address.text()\
                    + "' WHERE name='" + self.enter_add_client_name.text() + "';"
            connection.execute(query)
            query = "UPDATE " + self.enter_table_to_add.text() + " SET security=" + self.enter_add_security.text()\
                    + " WHERE name='" + self.enter_add_client_name.text() + "';"
            connection.execute(query)
            query = "UPDATE " + self.enter_table_to_add.text() + " SET customer='" + self.enter_add_customer.text()\
                    + "' WHERE name='" + self.enter_add_client_name.text() + "';"
            connection.execute(query)
            print("Client Details Modified")
            connection.commit()

        except ValueError:
            QMessageBox.about(self, "Info", "Couldn't modify client details, something went wrong in entering values")

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't modify client details, something went wrong")

        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")


class SerialChangePage(QWidget):
    def __init__(self, parent=None):
        super(SerialChangePage, self).__init__(parent)
        self.add_client_to_change = QLabel("Enter client name whose serial you want to change", self)
        self.enter_add_client_to_change = QLineEdit(self)
        self.add_client_to_change_with = QLabel("Enter client name with whom you want to change serial", self)
        self.enter_add_client_to_change_with = QLineEdit(self)
        self.add_client_to_change_in = QLabel("Enter Tablename", self)
        self.enter_add_client_to_change_in = QLineEdit(self)
        self.chamge = QPushButton("Change", self)
        self.cancel = QPushButton("Cancel/back", self)
        self.add_client_to_change.move(100,100)
        self.enter_add_client_to_change.move(100,150)
        self.add_client_to_change_with.move(100,250)
        self.enter_add_client_to_change_with.move(100,300)
        self.add_client_to_change_in.move(100,450)
        self.enter_add_client_to_change_in.move(200, 450)
        self.chamge.move(150,550)
        self.cancel.move(300,550)

    def changingserial(self):
        try:
            global connection
            table = self.enter_add_client_to_change_in.text()
            name_with = self.enter_add_client_to_change_with.text()
            name_to = self.enter_add_client_to_change.text()
            query = "SELECT for_i FROM " + table + "_paid WHERE name=' ';"
            for_i = connection.execute(query)
            query = "SELECT cust_id FROM " + table + " WHERE name='" + name_with + "';"
            cust_ids = connection.execute(query)
            for cust_id in cust_ids:
                id_with = int(str(cust_id[0]))
            query = "SELECT cust_id FROM " + table + " WHERE name='" + name_to + "';"
            cust_ids = connection.execute(query)
            for cust_id in cust_ids:
                id_to = int(str(cust_id[0]))
            for iis in for_i:
                start = int(str(iis[0]))
            temp = start
            query = "UPDATE " + table + " SET cust_id=" + str(start) + " WHERE cust_id=" + str(id_to) + ";"
            connection.execute(query)
            query = "UPDATE " + table + "_paid SET for_i=" + str(start) + " WHERE for_i=" + str(id_to) + ";"
            connection.execute(query)
            while(id_to>id_with):
                temp2 = id_to -1
                query = "UPDATE " + table + " SET cust_id=" + str(id_to) + " WHERE cust_id=" + str(temp2) + ";"
                connection.execute(query)
                query = "UPDATE " + table + "_paid SET for_i=" + str(id_to) + " WHERE for_i=" + str(temp2) + ";"
                connection.execute(query)
                id_to = id_to-1;
            query = "UPDATE " + table + " SET cust_id=" + str(id_with) + " WHERE cust_id=" + str(temp) + ";"
            connection.execute(query)
            query = "UPDATE " + table + "_paid SET for_i=" + str(id_with) + " WHERE for_i=" + str(temp) + ";"
            connection.execute(query)
            connection.commit()
            print("Sequence Changed")

        except ValueError:
            QMessageBox.about(self, "Info", "Couldn't change sequence, something went wrong in entering values")

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't change sequence, something went wrong")

        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")


class DeleteClientPage(QWidget):
    def __init__(self, parent=None):
        super(DeleteClientPage, self).__init__(parent)
        self.delete_client_name = QLabel("Enter Client Name", self)
        self.enter_delete_client_name = QLineEdit(self)
        self.delete_client = QPushButton("DELETE", self)
        self.table_to_delete = QLabel("Enter table name", self)
        self.enter_table_to_delete = QLineEdit(self)
        self.cancel = QPushButton("Cancel/Back", self)
        self.delete_client.move(280,400)
        self.cancel.move(380, 400)
        self.deleteclientframe = QFrame(self)
        self.deleteclientlayout = QHBoxLayout()
        self.deleteclientframe.setLayout(self.deleteclientlayout)
        self.deleteclientlayout.addWidget(self.delete_client_name)
        self.deleteclientlayout.addWidget(self.enter_delete_client_name)
        self.deleteclientframe.setGeometry(150, 200, 400, 100)
        self.tabledeleteframe = QFrame(self)
        self.tabledeletelayout = QHBoxLayout()
        self.tabledeleteframe.setLayout(self.tabledeletelayout)
        self.tabledeletelayout.addWidget(self.table_to_delete)
        self.tabledeletelayout.addWidget(self.enter_table_to_delete)
        self.tabledeleteframe.setGeometry(150, 300, 400, 100)

    def deleting_client(self):
        try:
            global connection
            query = "DELETE FROM "+ self.enter_table_to_delete.text() +\
                    " WHERE name= '" + self.enter_delete_client_name.text() + "';"
            connection.execute(query)
            query = "DELETE FROM "+ self.enter_table_to_delete.text() +\
                    "_paid WHERE name= '" + self.enter_delete_client_name.text() + "';"
            connection.execute(query)
            connection.commit()
            print("client deleted")

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't delete client, something went wrong")
        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")

class ShowingRecordPage(QWidget):
    def __init__(self, parent= None):
        super(ShowingRecordPage, self).__init__(parent)
        self.show_name = QLabel(self)
        self.show_phone = QLabel(self)
        self.show_address = QLabel(self)
        self.show_security = QLabel(self)
        self.show_cust_id = QLabel(self)
        self.show_jar_remaining = QLabel(self)
        self.show_can_remaining = QLabel(self)
        self.remark = QLabel("Remark", self)
        self.add_remark = QTextEdit(self)
        self.add_remark.setFixedSize(300,150)
        self.tablewidget = QTableWidget(self)
        self.tablewidget.setGeometry(50, 100, 850, 350)
        self.tablewidget.move(50, 200)
        self.tablewidget.setRowCount(11)
        self.tablewidget.setColumnCount(8)
        self.cancel = QPushButton("Cancel/Back", self)
        self.cancel.move(300, 600)
        self.show_name.setFixedSize(250,50)
        self.show_phone.setFixedSize(200, 50)
        self.show_security.setFixedSize(100, 50)
        self.show_jar_remaining.setFixedSize(100, 50)
        self.show_can_remaining.setFixedSize(150, 50)
        self.show_address.setFixedSize(600, 50)
        self.show_cust_id.move(20, 50)
        self.show_name.move(20, 80)
        self.show_phone.move(300, 80)
        self.show_address.move(300, 120)
        self.show_security.move(20,120)
        self.remark.move(450,50)
        self.add_remark.move(450,70)
        self.show_jar_remaining.move(20,150)
        self.show_can_remaining.move(300,150)

    def showing_record(self, name, tblname):
        try:
            global table_name, connection
            global Database_name
            connectiontab = sqlite3.connect(Database_name)
            self.name = name
            self.show_name.setText("Name: " + self.name)
            query = "SELECT * FROM " + tblname + " WHERE name ='" + self.name + "';"
            record = connection.execute(query)
            query = "SELECT * FROM " + tblname + "_paid WHERE name='" + self.name + "';"
            record2 = connectiontab.execute(query)
            for i in range(0, 12):
                x = "day " + str(i + 1)
                self.tablewidget.setItem(i, 0, QTableWidgetItem(x))
            for i in range(2, 13):
                x = "day " + str(i + 10)
                self.tablewidget.setItem(i - 2, 2, QTableWidgetItem(x))
            for i in range(3, 12):
                x = "day " + str(i + 20)
                self.tablewidget.setItem(i - 3, 4, QTableWidgetItem(x))
            for rec in record:
                self.add_remark.setText(str(rec[42]))
                for rec2 in record2:
                    for i in range(0, 12):
                        if int(str(rec2[i+2])) > 0:
                            pay = str(rec2[i+2])
                        else:
                            pay = ' '
                        x = str(rec[i+1]).split('a',4)
                        self.tablewidget.setItem(i, 1, QTableWidgetItem(x[0] + "+" + x[1] + "=" + x[2] + ", Rs: "+ str(pay)))
                    for i in range(2, 13):
                        if int(str(rec2[i+11])) > 0:
                            pay = str(rec2[i+11])
                        else:
                            pay = ' '
                        x = str(rec[i+10]).split('a',4)
                        self.tablewidget.setItem(i - 2, 3, QTableWidgetItem(x[0] + "+" + x[1] + "=" + x[2]+ ", Rs: "+  str(pay)))
                    for i in range(3, 12):

                        if int(str(rec2[i+21])) > 0:
                            pay = str(rec2[i+21])
                        else:
                            pay = ' '
                        x = str(rec[i+20]).split('a',4)
                        self.tablewidget.setItem(i - 3, 5, QTableWidgetItem(x[0] + "+" + x[1] + "=" + x[2]+ ", Rs: "+  str(pay)))
                self.tablewidget.setItem(0, 6, QTableWidgetItem("Total:"))

                total_jar = 0
                total_can = 0
                for k in range(1, 32):
                    temp = int(str(rec[k]).split('a', 4)[0])
                    total_jar = total_jar + temp
                    temp = int(str(rec[k]).split('a', 4)[1])
                    total_can = total_can + temp
                total_final = total_jar + total_can
                #y = str(rec[32]).split("@", 2)
                self.tablewidget.setItem(1, 6, QTableWidgetItem("Due:"))
                self.tablewidget.setItem(2, 6, QTableWidgetItem("Total Paid:"))
                self.tablewidget.setItem(3, 6, QTableWidgetItem("Balance:"))
                #print(y)
                #self.tablewidget.setItem(0, 7, QTableWidgetItem(y[0] + "+" + y[1] + "= "+ y[2]))
                self.tablewidget.setItem(0, 7, QTableWidgetItem(str(total_jar) + "+" + str(total_can) + "= " + str(total_final)))
                self.tablewidget.setItem(1, 7, QTableWidgetItem(str(rec[33])))
                self.tablewidget.setItem(2, 7, QTableWidgetItem(str(rec2[33])))
                bal = int(str(rec[33])) - int(str(rec2[33]))
                self.tablewidget.setItem(3, 7, QTableWidgetItem(str(bal)))
                self.show_phone.setText("Phone no: " + str(rec[34]))
                self.show_address.setText("Address: " + str(rec[35]))
                self.show_security.setText("Security: " + str(rec[36]))
                self.show_jar_remaining.setText("Jar Remaining: " + str(rec[37]))
                self.show_can_remaining.setText("Capsule Remaining: " + str(rec[38]))
            self.tablewidget.setColumnWidth(1, 100)

        except ValueError:
            QMessageBox.about(self, "Info", "Couldn't show records, something went wrong in entering values")

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't show records, something went wrong")

        #except NameError:
            #QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")


class ShowingRecordFromTablePage(QWidget):
    def __init__(self, parent= None):
        super(ShowingRecordFromTablePage, self).__init__(parent)
        self.show_name = QLabel(self)
        self.show_phone = QLabel(self)
        self.show_address = QLabel(self)
        self.show_security = QLabel(self)
        self.show_cust_id = QLabel(self)
        self.show_jar_remaining = QLabel(self)
        self.show_can_remaining = QLabel(self)
        self.remark = QLabel("Remark", self)
        self.add_remark = QTextEdit(self)
        self.add_remark.setFixedSize(300,150)
        self.tablewidget = QTableWidget(self)
        self.tablewidget.setGeometry(50, 100, 850, 350)
        self.tablewidget.move(50, 200)
        self.tablewidget.setRowCount(11)
        self.tablewidget.setColumnCount(8)
        self.cancel = QPushButton("Cancel/Back", self)
        self.cancel.move(300, 600)
        self.show_name.setFixedSize(250,50)
        self.show_phone.setFixedSize(200, 50)
        self.show_security.setFixedSize(100, 50)
        self.show_jar_remaining.setFixedSize(100, 50)
        self.show_can_remaining.setFixedSize(150, 50)
        self.show_address.setFixedSize(600, 50)
        self.show_cust_id.move(20, 50)
        self.show_name.move(20, 80)
        self.show_phone.move(300, 80)
        self.show_address.move(300, 120)
        self.show_security.move(20,120)
        self.remark.move(450,50)
        self.add_remark.move(450,70)
        self.show_jar_remaining.move(20,150)
        self.show_can_remaining.move(300,150)

    def showing_record(self, name, tblname):
        try:
            global table_name, connection
            global Database_name
            connectiontab = sqlite3.connect(Database_name)
            self.name = name
            self.show_name.setText("Name: " + self.name)
            query = "SELECT * FROM " + tblname + " WHERE name ='" + self.name + "';"
            record = connection.execute(query)
            query = "SELECT * FROM " + tblname + "_paid WHERE name='" + self.name + "';"
            record2 = connectiontab.execute(query)
            for i in range(0, 12):
                x = "day " + str(i + 1)
                self.tablewidget.setItem(i, 0, QTableWidgetItem(x))
            for i in range(2, 13):
                x = "day " + str(i + 10)
                self.tablewidget.setItem(i - 2, 2, QTableWidgetItem(x))
            for i in range(3, 12):
                x = "day " + str(i + 20)
                self.tablewidget.setItem(i - 3, 4, QTableWidgetItem(x))
            for rec in record:
                self.add_remark.setText(str(rec[42]))
                for rec2 in record2:
                    for i in range(0, 12):
                        if int(str(rec2[i+2])) > 0:
                            pay = str(rec2[i+2])
                        else:
                            pay = ' '
                        x = str(rec[i+1]).split('a',4)
                        self.tablewidget.setItem(i, 1, QTableWidgetItem(x[0] + "+" + x[1] + "=" + x[2] + ", Rs: "+ str(pay)))
                    for i in range(2, 13):
                        if int(str(rec2[i+11])) > 0:
                            pay = str(rec2[i+11])
                        else:
                            pay = ' '
                        x = str(rec[i+10]).split('a',4)
                        self.tablewidget.setItem(i - 2, 3, QTableWidgetItem(x[0] + "+" + x[1] + "=" + x[2]+ ", Rs: "+  str(pay)))
                    for i in range(3, 12):

                        if int(str(rec2[i+21])) > 0:
                            pay = str(rec2[i+21])
                        else:
                            pay = ' '
                        x = str(rec[i+20]).split('a',4)
                        self.tablewidget.setItem(i - 3, 5, QTableWidgetItem(x[0] + "+" + x[1] + "=" + x[2]+ ", Rs: "+  str(pay)))
                self.tablewidget.setItem(0, 6, QTableWidgetItem("Total:"))

                total_jar = 0
                total_can = 0
                for k in range(1, 32):
                    temp = int(str(rec[k]).split('a', 4)[0])
                    total_jar = total_jar + temp
                    temp = int(str(rec[k]).split('a', 4)[1])
                    total_can = total_can + temp
                total_final = total_jar + total_can
                #y = str(rec[32]).split("@", 2)
                self.tablewidget.setItem(1, 6, QTableWidgetItem("Due:"))
                self.tablewidget.setItem(2, 6, QTableWidgetItem("Total Paid:"))
                self.tablewidget.setItem(3, 6, QTableWidgetItem("Balance:"))
                #print(y)
                #self.tablewidget.setItem(0, 7, QTableWidgetItem(y[0] + "+" + y[1] + "= "+ y[2]))
                self.tablewidget.setItem(0, 7, QTableWidgetItem(str(total_jar) + "+" + str(total_can) + "= " + str(total_final)))
                self.tablewidget.setItem(1, 7, QTableWidgetItem(str(rec[33])))
                self.tablewidget.setItem(2, 7, QTableWidgetItem(str(rec2[33])))
                bal = int(str(rec[33])) - int(str(rec2[33]))
                self.tablewidget.setItem(3, 7, QTableWidgetItem(str(bal)))
                self.show_phone.setText("Phone no: " + str(rec[34]))
                self.show_address.setText("Address: " + str(rec[35]))
                self.show_security.setText("Security: " + str(rec[36]))
                self.show_jar_remaining.setText("Jar Remaining: " + str(rec[37]))
                self.show_can_remaining.setText("Capsule Remaining: " + str(rec[38]))
            self.tablewidget.setColumnWidth(1, 100)

        except ValueError:
            QMessageBox.about(self, "Info", "Couldn't show records, something went wrong in entering values")

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't show records, something went wrong")

        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")


class FindingClients(QWidget):
    def __init__(self, parent=None):
        super(FindingClients, self).__init__(parent)
        self.tblwidget = QTableWidget(self)
        self.tblwidget.setGeometry(50, 50, 1000, 500)
        self.tblwidget.move(50, 50)
        self.tblwidget.setRowCount(500)
        self.tblwidget.setColumnCount(41)
        self.all_name = list()
        self.cancel = QPushButton("Cancel/Back", self)
        self.cancel.move(200,600)

    def finding_client(self, query):
        try:
            global table_name, day_name
            z= 0
            b = 0
            day_no = list()
            for mnth in calendar.month_name:
                if table_name[:-4] == mnth.lower():
                    z = b
                else:
                    b = b+1
            b = int(table_name[-4:])
            c = calendar.TextCalendar(calendar.SUNDAY)
            no = 0
            for a in c.itermonthdays2(b,z):
                if int(a[0]) > 0:
                    no = no+1
                    day_no.append(int(a[1]))
            self.query = query
            record = connection.execute(self.query)
            i=2
            self.all_name.clear()
            self.tblwidget.setItem(0, 0, QTableWidgetItem("Security"))
            self.tblwidget.setItem(0, 1, QTableWidgetItem("Name"))
            self.tblwidget.setItem(0, 2, QTableWidgetItem("Phone no."))
            self.tblwidget.setItem(0, 3, QTableWidgetItem("Address"))
            self.tblwidget.setItem(0, 4, QTableWidgetItem("Total"))
            self.tblwidget.setItem(0, 5, QTableWidgetItem("Payment Due"))
            self.tblwidget.setItem(0, 6, QTableWidgetItem("Dates"))
            for j in range(1,32):
                self.tblwidget.setItem(0, j+6, QTableWidgetItem("Day" + str(j)))
            for j in range(1, no+1):
                self.tblwidget.setItem(1,j+6, QTableWidgetItem(str(day_name[int(day_no[j-1])])))
            self.tblwidget.setItem(0, 38, QTableWidgetItem("Jar Remaining"))
            self.tblwidget.setItem(0, 39, QTableWidgetItem("Capsule Remaining"))
            self.tblwidget.setItem(0, 40, QTableWidgetItem("Remark"))
            for j in range(2,500):
                for k in range(0,41):
                    self.tblwidget.setItem(j, k, QTableWidgetItem(" "))
            for rec in record:
                x = " "
                for l in range(1,32):
                    try:
                        if int(str(rec[l]).split('a',4)[2]) > 0:
                            x = str(x) + str(l) + ","
                        else:
                            pass

                    except ValueError:
                        pass
                y = str(rec[32]).split("@",2)
                self.tblwidget.setItem(i, 0, QTableWidgetItem(str(rec[36])))
                self.all_name.append(str(rec[0]))
                self.tblwidget.setItem(i, 1, QTableWidgetItem(str(rec[0])))
                print(str(rec[0]))
                self.tblwidget.setItem(i, 2, QTableWidgetItem(str(rec[34])))
                self.tblwidget.setItem(i, 3, QTableWidgetItem(str(rec[35])))
                self.tblwidget.setItem(i, 4, QTableWidgetItem(y[0] + "+" + y[1] + "= "+ y[2]))
                self.tblwidget.setItem(i, 5, QTableWidgetItem(str(rec[41])))
                self.tblwidget.setItem(i, 6, QTableWidgetItem(x))
                for j in range(1,32):
                    x = str(rec[j]).split('a',4)
                    self.tblwidget.setItem(i, j+6, QTableWidgetItem(x[0] + "+" + x[1] + "=" + x[2]))
                self.tblwidget.setItem(i, 38, QTableWidgetItem(str(rec[37])))
                self.tblwidget.setItem(i, 39, QTableWidgetItem(str(rec[38])))
                self.tblwidget.setItem(i, 40, QTableWidgetItem(str(rec[42])))
                i = i+1

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't view record , something went wrong")
        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")

        except ValueError:
            QMessageBox.about(self, "Info", "Couldn't view record, something went wrong in entering values")



class FindingRegularClients(QWidget):
    def __init__(self, parent=None):
        super(FindingRegularClients, self).__init__(parent)
        self.tblwidget = QTableWidget(self)
        self.tblwidget.setGeometry(50, 50, 1000, 500)
        self.tblwidget.move(50, 50)
        self.tblwidget.setRowCount(500)
        self.tblwidget.setColumnCount(41)
        self.cancel = QPushButton("Cancel/Back", self)
        self.cancel.move(200,600)
        self.edits = list()
        self.all_name = list()

    def finding_client(self, query1,query2, tablename):
        try:
            global table_name, day_name
            z = 0
            b = 0
            day_no = list()
            for mnth in calendar.month_name:
                if table_name[:-4] == mnth.lower():
                    z = b
                else:
                    b = b + 1
            b = int(table_name[-4:])
            c = calendar.TextCalendar(calendar.SUNDAY)
            no = 0
            for a in c.itermonthdays2(b, z):
                if int(a[0]) > 0:
                    no = no + 1
                    day_no.append(int(a[1]))
            global connection
            self.query = query1
            self.record = connection.execute(self.query)
            num = connection.execute(query2)
            self.all_name.clear()
            #names = connection.execute(query3)
            for number in num:
                self.m = int(str(number[0]))
            for i in range(1,500):
                self.tblwidget.removeCellWidget(i,1)
            for n in range(0,self.m):
                self.edits.append(list())
                for k in range(0,32):
                    self.edits[n].append(QLineEdit(self))
            i=2
            g = 0
            self.tblwidget.setItem(0, 0, QTableWidgetItem("Security"))
            self.tblwidget.setItem(0, 1, QTableWidgetItem("Name"))
            self.tblwidget.setItem(0, 2, QTableWidgetItem("Phone no."))
            self.tblwidget.setItem(0, 3, QTableWidgetItem("Address"))
            self.tblwidget.setItem(0, 4, QTableWidgetItem("Total"))
            self.tblwidget.setItem(0, 5, QTableWidgetItem("Payment Due"))
            self.tblwidget.setItem(0, 6, QTableWidgetItem("Dates"))
            for j in range(1,32):
                self.tblwidget.setItem(0, j+6, QTableWidgetItem("Day" + str(j)))
            for j in range(1, no+1):
                self.tblwidget.setItem(1,j+6, QTableWidgetItem(str(day_name[int(day_no[j-1])])))
            self.tblwidget.setItem(0, 38, QTableWidgetItem("Jar Remaining"))
            self.tblwidget.setItem(0, 39, QTableWidgetItem("Capsule Remaining"))
            self.tblwidget.setItem(0, 40, QTableWidgetItem("Remark"))
            for j in range(2,500):
                for k in range(0,41):
                    self.tblwidget.setItem(j, k, QTableWidgetItem(" "))
            for rec in self.record:
                x = " "
                for l in range(1,32):
                    try:
                        if int(str(rec[l]).split('a',4)[2]) > 0:
                            x = str(x) + str(l) + ","
                        else:
                            pass

                    except ValueError:
                        pass
                y = str(rec[32]).split("@",2)
                self.tblwidget.setItem(i, 0, QTableWidgetItem(str(rec[36])))
                self.tblwidget.setItem(i, 1, QTableWidgetItem(str(rec[0])))
                self.all_name.append(str(rec[0]))
                self.tblwidget.setItem(i, 2, QTableWidgetItem(str(rec[34])))
                self.tblwidget.setItem(i, 3, QTableWidgetItem(str(rec[35])))
                self.tblwidget.setItem(i, 4, QTableWidgetItem(y[0] + "+" + y[1] + "= "+ y[2]))
                self.tblwidget.setItem(i, 5, QTableWidgetItem(str(rec[41])))
                self.tblwidget.setItem(i, 6, QTableWidgetItem(x))
                for j in range(0,31):
                    self.tblwidget.setCellWidget(g+2,j+7, self.edits[g][j])
                    x = str(rec[j+1]).split('a', 4)
                    self.edits[g][j].setText(str(x[0]))

                self.tblwidget.setItem(i, 38, QTableWidgetItem(str(rec[37])))
                self.tblwidget.setItem(i, 39, QTableWidgetItem(str(rec[38])))
                self.tblwidget.setItem(i, 40, QTableWidgetItem(str(rec[42])))
                i = i+1
                g = g+1

        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't view record , something went wrong")
        #except NameError:
            #QMessageBox.about(self, "info", "You did not create a connection")

    def going_back(self):
        try:
            global table_name, connection
            i = 0
            query = "SELECT * FROM " + table_name + " WHERE status='OPEN' and customer='regular';"
            record = connection.execute(query)
            for rec in record:
                sum = 0
                for j in range(1,32):
                    if self.edits[i][j-1].text() == '':
                        x = '0a0a0a0a0'
                    else:
                        x = self.edits[i][j-1].text() + "a0a" + self.edits[i][j-1].text() + "a" + self.edits[i][j-1].text() + "a0"
                        sum = sum + int(self.edits[i][j-1].text())
                    query = "UPDATE " + table_name + " SET day_" + str(j) + "='" + x + "' WHERE name='" + str(rec[0]) + "';"
                    connection.execute(query)
                query = "UPDATE " + table_name + " SET total='" + str(sum) + "@0@" + str(sum) + "' WHERE name='" + str(rec[0]) + "';"
                connection.execute(query)
                connection.commit()
                i = i+1
        except sqlite3.OperationalError:
            QMessageBox.about(self, "Info", "Couldn't add entries , something went wrong")
        except NameError:
            QMessageBox.about(self, "info", "Either You did not create a connection, or you entered something incorrect")

        #except ValueError:
            #QMessageBox.about(self, "Info", "Couldn't add entries, something went wrong in entering values")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        global day_name
        day_name = list()
        for z in calendar.day_name:
            day_name.append(z[0:3])
        self.tablename = ' '
        self.name = ' '
        self.setWindowTitle("Pure Sip Accounting System")
        self.setBaseSize(700,800)
        self.mainPage = MainPage(self)
        self.mainPage.show()
        self.createtable = CreateTablePage(self)
        self.createtable.hide()
        self.usetable = UseTablePage(self)
        self.usetable.hide()
        self.tabletouse = TablenamePage(self)
        self.tabletouse.hide()
        self.modifytable = ModifyTablePage(self)
        self.modifytable.hide()
        self.addentry = AddEntryPage(self)
        self.addentry.hide()
        self.viewrecord = ViewRecordPage(self)
        self.viewrecord.hide()
        self.addclient = AddClientPage(self)
        self.addclient.hide()
        self.deleteclient = DeleteClientPage(self)
        self.deleteclient.hide()
        self.findclient = FindClientPage(self)
        self.findclient.hide()
        self.findingclients = FindingClients(self)
        self.findingclients.hide()
        self.showrecord = ShowingRecordPage(self)
        self.showrecord.hide()
        self.middlemodify = MiddleModifyPage(self)
        self.middlemodify.hide()
        self.modifyclient = ModifyClientPage(self)
        self.modifyclient.hide()
        self.serialchange = SerialChangePage(self)
        self.serialchange.hide()
        self.closeclient = ClientClosedPage(self)
        self.closeclient.hide()
        self.addremark = AddRemarkPage(self)
        self.addremark.hide()
        self.showrecordfromtable = ShowingRecordFromTablePage(self)
        self.showrecordfromtable.hide()
        self.findregularclients = FindingRegularClients(self)
        self.findregularclients.hide()
        self.mainPage.create_connection.clicked.connect(self.mainPage.creating_connection)
        self.mainPage.enter_dbname.returnPressed.connect(self.mainPage.creating_connection)
        self.mainPage.create_table.clicked.connect(self.createTable)
        self.mainPage.use_table.clicked.connect(self.tableToUse)
        self.mainPage.modify_table.clicked.connect(self.modifyTable)
        self.mainPage.quit.clicked.connect(self.close)
        self.createtable.create.clicked.connect(self.createtable.creating_new_table)
        self.createtable.cancel.clicked.connect(self.backToMainPage)
        self.tabletouse.use_button.clicked.connect(self.useTable)
        self.tabletouse.cancel.clicked.connect(self.backToMainPage)
        self.usetable.add_entry.clicked.connect(self.addEntry)
        self.usetable.view_record.clicked.connect(self.viewRecord)
        self.usetable.find_client.clicked.connect(self.findClient)
        self.usetable.client_closed.clicked.connect(self.closeClient)
        self.usetable.cancel.clicked.connect(self.backToMainPage)
        self.usetable.add_remark.clicked.connect(self.addRemark)
        self.usetable.add_regular_entry.clicked.connect(self.findRegular)
        self.usetable.show_closed_clients.clicked.connect(self.showclosedClients)
        self.closeclient.close_button.clicked.connect(self.closeclient.closingclient)
        self.closeclient.cancel.clicked.connect(self.backToUseTable)
        self.addentry.add.clicked.connect(self.addentry.adding_entry)
        self.addentry.cancel.clicked.connect(self.backToUseTable)
        self.viewrecord.view.clicked.connect(self.showRecord)
        self.viewrecord.cancel.clicked.connect(self.backToUseTable)
        self.showrecord.cancel.clicked.connect(self.backToViewRecord)
        self.showrecordfromtable.cancel.clicked.connect(self.backToFindingClients)
        self.addremark.add_button.clicked.connect(self.addremark.addingremark)
        self.addremark.cancel.clicked.connect(self.backToUseTable)
        self.modifytable.cancel.clicked.connect(self.backToMainPage)
        self.modifytable.add_client.clicked.connect(self.addClient)
        self.modifytable.modify_client.clicked.connect(self.middleModify)
        self.modifytable.delete_client.clicked.connect(self.deleteClient)
        self.modifytable.change_serial.clicked.connect(self.changeSerial)
        self.addclient.add_client.clicked.connect(self.addclient.adding_client)
        self.addclient.cancel.clicked.connect(self.backToModifyTable)
        self.middlemodify.proceed_button.clicked.connect(self.modifyPage)
        self.middlemodify.cancel.clicked.connect(self.backToModifyTable)
        self.modifyclient.modify_client.clicked.connect(self.modifyclient.modifyingvalues)
        self.modifyclient.cancel.clicked.connect(self.backToMainPage)
        self.serialchange.chamge.clicked.connect(self.serialchange.changingserial)
        self.serialchange.cancel.clicked.connect(self.backToModifyTable)
        self.deleteclient.delete_client.clicked.connect(self.deleteclient.deleting_client)
        self.deleteclient.cancel.clicked.connect(self.backToModifyTable)
        self.findclient.find_client.clicked.connect(self.showClients)
        self.findingclients.tblwidget.itemDoubleClicked.connect(self.showRecordTable)
        self.findregularclients.tblwidget.itemDoubleClicked.connect(self.showRecordTable)
        self.findclient.cancel.clicked.connect(self.backToUseTable)
        self.findregularclients.cancel.clicked.connect(self.backToUse)
        self.findingclients.cancel.clicked.connect(self.backToUseTable)
        self.show()

    def createTable(self):
        if self.mainPage.enter_dbname.text() is "":
            QMessageBox.about(self, "info", "enter database name")
        else:
            self.mainPage.hide()
            self.createtable.show()

    def useTable(self):
        try:
            if self.tabletouse.enter_table_name_to_use.text() is "":
                QMessageBox.about(self, "info", "Enter table name")
            else:
                self.mainPage.hide()
                self.tabletouse.hide()
                global table_name
                table_name = self.tabletouse.enter_table_name_to_use.text()
                self.usetable.show()
        except NameError:
            QMessageBox.about(self, "info", "You did not create a connection")

    def modifyTable(self):
        if self.mainPage.enter_dbname.text() is "":
            QMessageBox.about(self, "info", "enter database name")
        else:
            self.mainPage.hide()
            self.modifytable.show()

    def middleModify(self):
        self.modifytable.hide()
        self.middlemodify.show()

    def changeSerial(self):
        self.modifytable.hide()
        self.serialchange.show()

    def addRemark(self):
        self.usetable.hide()
        self.addremark.show()

    def tableToUse(self):
        if self.mainPage.enter_dbname.text() is "":
            QMessageBox.about(self, "info", "enter database name")
        else:
            self.mainPage.hide()
            self.tabletouse.show()

    def findClient(self):
        self.usetable.hide()
        self.findclient.show()

    def addEntry(self):
        self.usetable.hide()
        self.addentry.show()
        self.addentry.enter_one_can.setText('0')
        self.addentry.enter_one_jar.setText('0')
        self.addentry.enter_capsuletaken.setText('0')
        self.addentry.enter_jartaken.setText('0')
        self.addentry.enter_capsulegiven.setText('0')
        self.addentry.enter_jargiven.setText('0')
        self.addentry.enter_paid.setText('0')

    def viewRecord(self):
        self.usetable.hide()
        self.viewrecord.show()

    def closeClient(self):
        self.usetable.hide()
        self.closeclient.show()
        self.closeclient.enter_remark.setText(' ')
        self.closeclient.enter_add_cap_returned.setText('0')
        self.closeclient.enter_add_jar_returned.setText('0')

    def modifyPage(self):
        self.middlemodify.hide()
        self.modifyclient.show()
        self.modifyclient.givingvalues(self.middlemodify.enter_add_client_to_modify.text(), self.middlemodify.enter_add_table_to_modify.text())

    def showClients(self):
        global table_name, indicator
        indicator = 0
        self.setGeometry(100,100,1200,800)
        self.findclient.hide()
        self.findingclients.show()
        x = self.findclient.finding_client()
        self.findingclients.finding_client(x)

    def findRegular(self):
        global table_name, indicator
        indicator = 2
        self.usetable.hide()
        self.findregularclients.show()
        query1 = "SELECT * FROM " + table_name + " WHERE status='OPEN' and customer='regular';"
        query2 = "SELECT COUNT(name) FROM " + table_name + " WHERE status='OPEN' and customer='regular';"
        self.findregularclients.finding_client(query1, query2, table_name)

    def showclosedClients(self):
        global table_name, indicator
        indicator = 1
        self.setGeometry(100,100,1200,800)
        self.usetable.hide()
        self.findingclients.show()
        query1 = "SELECT * FROM " + table_name + " WHERE status='CLOSED';"
        self.findingclients.finding_client(query1)

    def showRecord(self):
        global table_name
        self.viewrecord.hide()
        self.showrecord.show()
        self.name = self.viewrecord.enter_view_client_name.text()
        if self.viewrecord.enter_month:
            self.showrecord.showing_record(self.viewrecord.enter_view_client_name.text(), self.viewrecord.enter_month.text())
            self.tablename = self.viewrecord.enter_month.text()
        else:
            self.showrecord.showing_record(self.viewrecord.enter_view_client_name.text(), table_name)
            self.tablename = table_name

    def showRecordTable(self):
        global table_name
        self.findingclients.hide()
        self.findregularclients.hide()
        self.showrecordfromtable.show()
        if indicator < 2:
            i = self.findingclients.tblwidget.currentRow()
            self.name2 = self.findingclients.all_name[i-2]
        else:
            i = self.findregularclients.tblwidget.currentRow()
            self.name2 = self.findregularclients.all_name[i-2]
        self.showrecordfromtable.showing_record(self.name2, table_name)

    def addClient(self):
        self.modifytable.hide()
        self.addclient.show()

    def deleteClient(self):
        self.modifytable.hide()
        self.deleteclient.show()

    def backToMainPage(self):
        self.addentry.hide()
        self.modifyclient.hide()
        self.tabletouse.hide()
        self.viewrecord.hide()
        self.createtable.hide()
        self.usetable.hide()
        self.modifytable.hide()
        self.addclient.hide()
        self.deleteclient.hide()
        self.mainPage.show()

    def backToUseTable(self):
        self.setBaseSize(700, 800)
        self.addentry.hide()
        self.closeclient.hide()
        self.viewrecord.hide()
        self.findclient.hide()
        self.addremark.hide()
        self.findingclients.hide()
        self.usetable.show()

    def backToUse(self):
        self.findregularclients.going_back()
        self.findregularclients.hide()
        self.usetable.show()

    def backToViewRecord(self):
        self.showrecord.hide()
        self.viewrecord.show()
        try:
            global connection
            query = "UPDATE " + self.tablename + " SET remark='" + self.showrecord.add_remark.toPlainText() + "' WHERE name='"\
            + self.name + "';"
            connection.execute(query)
            connection.commit()
        except sqlite3.OperationalError:
            pass
        except NameError:
            pass
        except ValueError:
            pass
        self.viewrecord.enter_month.setText('')
        self.viewrecord.enter_view_client_name.setText('')

    def backToModifyTable(self):
        self.addclient.hide()
        self.deleteclient.hide()
        self.serialchange.hide()
        self.middlemodify.hide()
        self.modifytable.show()

    def backToFindingClients(self):
        global indicator
        self.showrecordfromtable.hide()
        if indicator < 2:
            self.findingclients.show()
        else:
            self.findregularclients.show()
        global connection, table_name
        query = "UPDATE " + table_name + " SET remark='" + self.showrecordfromtable.add_remark.toPlainText() + "' WHERE name='"\
        + self.name2 + "';"
        connection.execute(query)
        connection.commit()
        self.viewrecord.enter_month.setText('')
        self.viewrecord.enter_view_client_name.setText('')
        if indicator == 0:
            self.showClients()
        elif indicator ==1:
            self.showclosedClients()
        elif indicator == 2:
            self.findRegular()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())