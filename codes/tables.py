import mysql.connector
password=input("Enter your root pass: ")
cnx=mysql.connector.connect(host="localhost",
                              user="root",
                              passwd=password)
my_cursor=cnx.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS DIGIKALA_DB")
my_cursor.execute("USE DIGIKALA_DB")

my_cursor.execute("CREATE TABLE IF NOT EXISTS Mobile"\
                  "(product_id INT,"\
                  "product_title_fa VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "product_title_en VARCHAR(255),"\
                  "brand_name_fa VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "brand_name_en VARCHAR(20),"\
                  "url_code VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci ,"\
                  "PRIMARY KEY(product_id))")

                  
my_cursor.execute("CREATE TABLE IF NOT EXISTS Mobile_title_alt"\
                  "(title_id INT AUTO_INCREMENT,"\
                  "p_id INT,"\
                  "title_alt VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "PRIMARY KEY(title_id),"\
                  "FOREIGN KEY (p_id) REFERENCES Mobile(product_id))")
                                   
my_cursor.execute("CREATE TABLE IF NOT EXISTS Laptop"\
                  "(product_id INT,"\
                  "product_title_fa VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "product_title_en VARCHAR(255),"\
                  "brand_name_fa VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "brand_name_en VARCHAR(20),"\
                  "url_code VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci ,"\
                  "PRIMARY KEY(product_id))")

my_cursor.execute("CREATE TABLE IF NOT EXISTS Laptop_attributes"\
                  "(L_attribute_id INT AUTO_INCREMENT,"\
                  "p_id INT,"\
                  "characteristics VARCHAR(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL ,"\
                  "ethernet CHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL ,"\
                  "touch_screen CHAR(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL ,"\
                  "USB_TYPE_C CHAR(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,"\
                  "RAM CHAR(10) DEFAULT NULL,"\
                  "FOREIGN KEY (p_id) REFERENCES Laptop(product_id),"\
                  "PRIMARY KEY(L_attribute_id))")
                 
my_cursor.execute("CREATE TABLE IF NOT EXISTS Laptop_title_alt"\
                  "(title_id INT AUTO_INCREMENT,"\
                  "p_id INT,"\
                  "title_alt VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "PRIMARY KEY(title_id),"\
                  "FOREIGN KEY (p_id) REFERENCES Laptop(product_id))")

my_cursor.execute("CREATE TABLE IF NOT EXISTS Tablet"\
                  "(product_id INT,"\
                  "product_title_fa VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "product_title_en VARCHAR(255),"\
                  "brand_name_fa VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "brand_name_en VARCHAR(20),"\
                  "url_code VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "PRIMARY KEY(product_id))")

                  
my_cursor.execute("CREATE TABLE IF NOT EXISTS Tablet_title_alt"\
                  "(title_id INT AUTO_INCREMENT,"\
                  "p_id INT,"\
                  "title_alt VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "PRIMARY KEY(title_id),"\
                  "FOREIGN KEY (p_id) REFERENCES Tablet(product_id))")

my_cursor.execute("CREATE TABLE IF NOT EXISTS Headphone"\
                  "(product_id INT,"\
                  "product_title_fa VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "product_title_en VARCHAR(255),"\
                  "brand_name_fa VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "brand_name_en VARCHAR(20),"\
                  "url_code VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "PRIMARY KEY(product_id))")

my_cursor.execute("CREATE TABLE IF NOT EXISTS Headphone_attributes"\
                  "(H_attribute_id INT AUTO_INCREMENT,"\
                  "p_id INT,"\
                  "dimensions CHAR(20) DEFAULT NULL ,"\
                  "Connector VARCHAR(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,"\
                  "weight CHAR(6) DEFAULT NULL,"\
                  "cable_length CHAR(3) DEFAULT NULL ,"\
                  "FOREIGN KEY (p_id) REFERENCES Headphone(product_id),"\
                  "PRIMARY KEY(H_attribute_id))")

my_cursor.execute("CREATE TABLE IF NOT EXISTS Headphone_title_alt"\
                  "(title_id INT AUTO_INCREMENT,"\
                  "p_id INT,"\
                  "title_alt VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "PRIMARY KEY(title_id),"\
                  "FOREIGN KEY (p_id) REFERENCES Headphone(product_id))")

my_cursor.execute("CREATE TABLE IF NOT EXISTS Speaker"\
                  "(product_id INT,"\
                  "product_title_fa VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "product_title_en VARCHAR(255),"\
                  "brand_name_fa VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "brand_name_en VARCHAR(20),"\
                  "url_code VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "PRIMARY KEY(product_id))")


my_cursor.execute("CREATE TABLE IF NOT EXISTS Speaker_title_alt"\
                  "(title_id INT AUTO_INCREMENT,"\
                  "p_id INT,"\
                  "title_alt VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "PRIMARY KEY(title_id),"\
                  "FOREIGN KEY (p_id) REFERENCES Speaker(product_id))")

my_cursor.execute("CREATE TABLE IF NOT EXISTS Gaming_Console"\
                  "(product_id INT,"\
                  "product_title_fa VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "product_title_en VARCHAR(255),"\
                  "brand_name_fa VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "brand_name_en VARCHAR(20),"\
                  "url_code VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "PRIMARY KEY(product_id))")

my_cursor.execute("CREATE TABLE IF NOT EXISTS Gaming_Console_title_alt"\
                  "(title_id INT AUTO_INCREMENT,"\
                  "p_id INT,"\
                  "title_alt VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci,"\
                  "PRIMARY KEY(title_id),"\
                  "FOREIGN KEY (p_id) REFERENCES Gaming_Console(product_id))")

my_cursor.close()
cnx.close()
