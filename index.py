from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb

from PyQt5.uic import loadUiType

ui,_ = loadUiType('library.ui')


class MainApp (QMainWindow,ui):


  def __init__(self):
    QMainWindow.__init__(self)
    self.setupUi(self) 
    self.handle_ui_changes()
    self.handle_buttons()
    self.show_category()
    self.show_author()
    self.show_publisher()
    self.show_category_combo_box()
    self.show_author_combo_box()
    self.show_publisher_combo_box()
    self.show_all_books()
    self.groupBox_4.setEnabled(False)


  def handle_buttons(self):
    
    self.pushButton.clicked.connect(self.open_day_to_day_tab)
    self.pushButton_2.clicked.connect(self.open_books_tab)
    self.pushButton_3.clicked.connect(self.open_users_tab)
    self.pushButton_4.clicked.connect(self.open_settings_tab)
    self.pushButton_5.clicked.connect(self.show_themes)  
    self.pushButton_21.clicked.connect(self.hiding_themes)
    self.pushButton_7.clicked.connect(self.add_new_book)
    self.pushButton_13.clicked.connect(self.add_category)
    self.pushButton_15.clicked.connect(self.add_author)
    self.pushButton_16.clicked.connect(self.add_publisher)
    self.pushButton_8.clicked.connect(self.search_book)
    self.pushButton_9.clicked.connect(self.edit_book)
    self.pushButton_10.clicked.connect(self.delete_book)
    self.pushButton_11.clicked.connect(self.add_new_user)
    self.pushButton_12.clicked.connect(self.login_user)
    self.pushButton_14.clicked.connect(self.edit_user)
    self.pushButton_37.clicked.connect(self.open_customers_tab)



  def handle_ui_changes(self):
    self.hiding_themes()
    self.tabWidget.tabBar().setVisible(False)
  
  def show_themes(self):
    self.groupBox_3.show()
   
  def hiding_themes(self):
    self.groupBox_3.hide()

  ## Opening Tabs
  def open_day_to_day_tab(self):
    self.tabWidget.setCurrentIndex(0)
  
  def open_books_tab(self):
    self.tabWidget.setCurrentIndex(1)
   
  def open_users_tab(self):
    self.tabWidget.setCurrentIndex(3)

  def open_settings_tab(self):
    self.tabWidget.setCurrentIndex(4)
  
  def open_customers_tab(self):
    self.tabWidget.setCurrentIndex(2)

  #--------------Database

  ## Adding New Books

  def add_new_book(self):
      self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db='library_management')
      self.cursor = self.db.cursor()

      book_title = self.lineEdit_3.text()
      book_code = self.lineEdit_2.text()
      book_category = self.comboBox_3.currentIndex()
      book_author = self.comboBox_4.currentIndex()
      book_publisher = self.comboBox_5.currentIndex()
      book_price = self.lineEdit_4.text()
      book_description = self.textEdit.toPlainText()

      sql_query = """

        INSERT INTO book (book_name,book_description,
        book_code,book_category,book_author,book_publisher,book_price)
        values (%s,%s,%s,%s,%s,%s,%s);
      """

      self.cursor.execute(sql_query,(book_title,book_description,book_code,book_category,book_author,book_publisher,book_price))
      self.db.commit()
      self.statusBar().showMessage('New Book Added')
      self.show_all_books()
      self.lineEdit_3.setText('')
      self.lineEdit_2.setText('')
      self.comboBox_3.setCurrentIndex(0)
      self.comboBox_4.setCurrentIndex(0)
      self.comboBox_5.setCurrentIndex(0)
      self.lineEdit_4.setText('')
      self.textEdit.setPlainText('')

  def search_book(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db='library_management')
    self.cursor = self.db.cursor()


    book_title = self.lineEdit_6.text()
    sql_query = """
    SELECT * FROM book where book_name =%s;
    """
    self.cursor.execute(sql_query,(book_title,))

    print(book_title)

    data = self.cursor.fetchone()
    if data:
      print(data[2])
      self.lineEdit_17.setText(str(data[3]))
      self.lineEdit_7.setText(data[1])
      self.comboBox_6.setCurrentIndex(int(data[4]))
      self.comboBox_8.setCurrentIndex(int(data[5]))
      self.comboBox_7.setCurrentIndex(int(data[6]))
      self.lineEdit_5.setText(data[7])
      self.textEdit_2.setPlainText(data[2])

  def edit_book(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db='library_management')
    self.cursor = self.db.cursor()

    book_title = self.lineEdit_7.text()
    book_code = self.lineEdit_17.text()
    book_category = self.comboBox_6.currentIndex()
    book_author = self.comboBox_6.currentIndex()
    book_publisher = self.comboBox_7.currentIndex()
    book_price = self.lineEdit_5.text()
    book_description = self.textEdit_2.toPlainText()


    sql_query = """
      UPDATE book SET book_name=%s,book_description=%s,book_code=%s,book_price=%s,
      book_category=%s,book_author=%s,book_publisher=%s where book_name=%s;

    """

    self.cursor.execute(sql_query,(book_title,book_description,book_code,book_price,book_category,book_author,book_publisher,book_title))

    self.db.commit()
    self.statusBar().showMessage('Book Details Updated')
    self.show_all_books()

    self.lineEdit_17.setText('')
    self.lineEdit_7.setText('')
    self.comboBox_6.setCurrentIndex(0)
    self.comboBox_8.setCurrentIndex(0)
    self.comboBox_7.setCurrentIndex(0)
    self.lineEdit_5.setText('')
    self.textEdit_2.setPlainText('')

  def delete_book(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()

    book_title = self.lineEdit_7.text()
    
    warning = QMessageBox.warning(self,'Delete Book',"Are you sure you want to delete this book?",QMessageBox.Yes | QMessageBox.No)
    if warning ==QMessageBox.Yes:
      sql_query = """
      DELETE from book where book_name=%s;
      """
      self.cursor.execute(sql_query,(book_title,))
      self.db.commit()
      self.statusBar().showMessage('Book Details Deleted')
      self.lineEdit_17.setText('')
      self.lineEdit_7.setText('')
      self.comboBox_6.setCurrentIndex(0)
      self.comboBox_8.setCurrentIndex(0)
      self.comboBox_7.setCurrentIndex(0)
      self.lineEdit_5.setText('')
      self.textEdit_2.setPlainText('')

  def show_all_books(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()


    sql_query = """
      SELECT * from book;
    """
    self.cursor.execute(sql_query)
    data = self.cursor.fetchall()
    print(data)
    if data:
      self.tableWidget_10.setRowCount(1)
      for row,form in enumerate(data):
        if row==2:
          continue
        row_position = self.tableWidget_10.rowCount()
        self.tableWidget_2.insertRow(row_position)
        for column,item in enumerate(form):
          print(item)
          self.tableWidget_10.setItem(row,column,QTableWidgetItem(str(item)))

  ### Combo Box categories from database

  def show_category_combo_box(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()


    sql_query = """
      SELECT category_name from categories;
    """
    self.cursor.execute(sql_query)
    data = self.cursor.fetchall()

    self.comboBox_3.clear()
    for category in data:
      self.comboBox_3.addItem(category[0])
      self.comboBox_6.addItem(category[0])

  def show_author_combo_box(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()


    sql_query = """
      SELECT author_name from authors;
    """
    self.cursor.execute(sql_query)
    data = self.cursor.fetchall()

    self.comboBox_4.clear()

    for category in data:
      self.comboBox_4.addItem(category[0])
      self.comboBox_8.addItem(category[0])


  def show_publisher_combo_box(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()


    sql_query = """
      SELECT publisher_name from publishers;
    """
    self.cursor.execute(sql_query)
    data = self.cursor.fetchall()

    self.comboBox_5.clear()

    for category in data:
      self.comboBox_5.addItem(category[0])
      self.comboBox_7.addItem(category[0])


  ## Adding New Users

  def add_new_user(self):

    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()

    user_name = self.lineEdit_11.text()
    email =self.lineEdit_8.text()
    password = self.lineEdit_10.text()
    password2 = self.lineEdit_9.text()
    
    print("im here")
    if (user_name and email and password and password2):
      if password==password2:
        sql_query = """
        INSERT INTO users (user_name,email,password) VALUES (%s,%s,%s);

        """
        print(user_name,email,password)
        self.cursor.execute(sql_query,(user_name,email,password))
        self.db.commit()
        self.statusBar().showMessage('New User Added')

      else:
        self.label_32.setText('Both passwords does not match. Please re-enter the passwords')


  def edit_user(self):
    user_name =self.lineEdit_20.text()
    email = self.lineEdit_19.text()
    password = self.lineEdit_21.text()
    password2 = self.lineEdit_18.text()

    first_user_name = self.self.lineEdit_12.text()
    if password:
       if (password==password2):
         self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
         self.cursor = self.db.cursor()
         
         sql_query="""
            UPDATE users SET user_name =%s,email=%s,password=%s WHERE
            user_name = %s;
         """

         self.cursor.execute(sql_query,(user_name,email,password,first_user_name))
         self.db.commit()
         self.statusBar().showMessage('User Data Updated')
         
       else:
         print("Both passwords do not match. Please re-enter")


        



  # def delete_user(self):
  #   pass

  def login_user(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()

    user_name = self.lineEdit_12.text()
    password = self.lineEdit_13.text()


    if user_name and password:

      sql_query= """
        SELECT * from users;
      """

      self.cursor.execute(sql_query)
      data = self.cursor.fetchall()
      
      for item in data:

        if item[1]==user_name and item[3]==password:
          print('user found')
          self.statusBar().showMessage('Valid User')
          self.groupBox_4.setEnabled(True)

          self.lineEdit_20.setText(item[1])
          self.lineEdit_19.setText(item[2])


  ## Settings Tab

  def add_category(self):
    category = self.lineEdit_14.text()
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()

    if len(category)>0:
      sql_insert = """
      INSERT INTO categories (category_name) values (%s);
      """

      self.cursor.execute(sql_insert,(category,))
      self.db.commit()
      self.show_category()
      self.show_category_combo_box()
      
      self.lineEdit_14.setText('')
      print(f"Category {category} added")

  def show_category(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()


    sql_query = """
      SELECT category_name from categories;
    """
    self.cursor.execute(sql_query)
    data = self.cursor.fetchall()
    
    if data:
      self.tableWidget_2.setRowCount(0)
      for row,form in enumerate(data):
        row_position = self.tableWidget_2.rowCount()
        self.tableWidget_2.insertRow(row_position)
        for column,item in enumerate(form):
          self.tableWidget_2.setItem(row,column,QTableWidgetItem(str(item)))


  def add_author(self):
    author = self.lineEdit_15.text()
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()

    if len(author)>0:
      sql_insert = """
      INSERT INTO authors (author_name) values (%s);
      """

      self.cursor.execute(sql_insert,(author,))
      self.db.commit()
      self.lineEdit_15.setText('')
      self.show_author()
      self.show_author_combo_box()
      
      print(f"Author {author} added")

  def show_author(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()


    sql_query = """
      SELECT author_name from authors;
    """
    self.cursor.execute(sql_query)
    data = self.cursor.fetchall()
    
    if data:
      self.tableWidget_3.setRowCount(0)
      for row,form in enumerate(data):
        row_position = self.tableWidget_3.rowCount()
        self.tableWidget_3.insertRow(row_position)
        for column,item in enumerate(form):
          self.tableWidget_3.setItem(row,column,QTableWidgetItem(str(item)))
  
  
  def add_publisher(self):
    publisher = self.lineEdit_16.text()
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()


    if len(publisher)>0:
      sql_insert = """
      INSERT INTO publishers (publisher_name) values (%s);
      """

      self.cursor.execute(sql_insert,(publisher,))
      self.db.commit()
      self.lineEdit_16.setText('')
      self.show_publisher()
      self.show_publisher_combo_box()
      print(f"Publisher {publisher} added")

  def show_publisher(self):
    self.db = MySQLdb.connect(host='localhost',user='temp',passwd='password',db="library_management")
    self.cursor = self.db.cursor()


    sql_query = """
      SELECT publisher_name from publishers;
    """
    self.cursor.execute(sql_query)
    data = self.cursor.fetchall()
    
    if data:
      self.tableWidget_4.setRowCount(0)
      for row,form in enumerate(data):
        row_position = self.tableWidget_4.rowCount()
        self.tableWidget_4.insertRow(row_position)
        for column,item in enumerate(form):
          self.tableWidget_4.setItem(row,column,QTableWidgetItem(str(item)))




### Customers Tab

def add_customer(self):

  pass

def edit_customer(self):
  pass

def search_customer(self):
  pass

def show_all_customers(self):
  pass


def main():
  app = QApplication(sys.argv)
  window = MainApp()
  window.show()
  app.exec_()


if __name__ == '__main__':
  main()
