import pandas as pd
import re
import mysql.connector
password=input("Enter your root pass: ")
cnx=mysql.connector.connect(host="localhost",
                            user="root",
                            passwd=password,
                            database="DIGIKALA_DB")
my_cursor=cnx.cursor()
data = pd.read_excel("5-awte8wbd.xlsx",encoding='utf-8')
df_1=pd.DataFrame(data,columns=['category_keywords'])
df_2=pd.DataFrame(data,columns=['product_attributes'])
df_3=pd.DataFrame(data,columns=['id'])
df_4=pd.DataFrame(data,columns=['product_title_fa'])
df_5=pd.DataFrame(data,columns=['product_title_en'])
df_6=pd.DataFrame(data,columns=['brand_name_fa'])
df_7=pd.DataFrame(data,columns=['brand_name_en'])
df_8=pd.DataFrame(data,columns=['url_code'])
df_9=pd.DataFrame(data,columns=['title_alt'])                  
ck_array=df_1.get_values()
pa_array=df_2.get_values()
p_array=df_3.get_values()
ptf_array=df_4.get_values()
pte_array=df_5.get_values()
bnf_array=df_6.get_values()
bne_array=df_7.get_values()
url_array=df_8.get_values()
tla_array=df_9.get_values()
S_M=r'Mobile-Phone'
S_L=r'Notebook-Netbook'
S_T='تبلت  Tablet'
S_H='Headphone'
S_S='Speaker'
S_GC='Gaming-Consoles'
key_pattern='Key'
value_pattern='Value'
comma_pattern=','
for i in range(ck_array.size):
    if re.search(S_M,str(ck_array[i][0])):
         SQL_query="INSERT INTO Mobile VALUES"\
                   "(%s,%s,%s,%s,%s,%s)"
         val=(int(p_array[i][0]),str(ptf_array[i][0]),
                     str(pte_array[i][0]),str(bnf_array[i][0]),str(bne_array[i][0]),
                     str(url_array[i][0]))
         my_cursor.execute(SQL_query,val)
         cnx.commit()
         title_string=str(tla_array[i][0])
         title_array=re.split(',|-|،',title_string)
         for S in title_array:
                  SQL_query="INSERT INTO Mobile_title_alt(p_id,title_alt) VALUES(%s,%s)"
                  if S.strip():
                     val=(int(p_array[i][0]),S)
                     my_cursor.execute(SQL_query,val)
                     cnx.commit()                  
    if re.search(S_L,str(ck_array[i][0])):
         SQL_query="INSERT INTO Laptop VALUES(%s,%s,%s,%s,%s,%s)"
         val=(int(p_array[i][0]),str(ptf_array[i][0]),str(pte_array[i][0]),
              str(bnf_array[i][0]),str(bne_array[i][0]),str(url_array[i][0]))
                          
         my_cursor.execute(SQL_query,val)
         cnx.commit()                           
         temp_string=str(pa_array[i][0])
         match_key=re.search(key_pattern,temp_string)
         if match_key:
             SQL_query="INSERT INTO laptop_attributes(p_id) VALUES(%s)"
             val=(int(p_array[i][0]),)
             my_cursor.execute(SQL_query,val)
             temp_array=temp_string.split('}')
             for t in temp_array:
                match_key=re.search(key_pattern,t)
                if match_key:
                    t=t[match_key.end():]
                    match_comma=re.search(comma_pattern,t)
                    if match_comma:
                        key=t[3:match_comma.end()-2]
                        if key == "مشخصات حافظه داخلی":
                           SQL_query="UPDATE laptop_attributes SET characteristics=%s WHERE p_id=%s"
                           value=t[match_comma.end()+9:-1]
                           val=(value,int(p_array[i][0]))
                           my_cursor.execute(SQL_query,val)
                           cnx.commit()
                        if key =="توضیحات پورت شبکه Ethernet" :
                           SQL_query="UPDATE laptop_attributes SET ethernet=%s WHERE p_id=%s"
                           value=t[match_comma.end()+9:-1]
                           val=(value,int(p_array[i][0]))
                           my_cursor.execute(SQL_query,val)
                           cnx.commit()
                        if key == "صفحه نمایش لمسی" :
                           SQL_query="UPDATE laptop_attributes SET touch_screen=%s WHERE p_id=%s"
                           value=t[match_comma.end()+9:-1]
                           val=(value,int(p_array[i][0]))
                           my_cursor.execute(SQL_query,val)
                           cnx.commit()
                        if key == "پورت USB Type-C":
                           SQL_query="UPDATE laptop_attributes SET USB_TYPE_C=%s WHERE p_id=%s"
                           value=t[match_comma.end()+9:-1]
                           val=(value,int(p_array[i][0]))
                           my_cursor.execute(SQL_query,val)
                           cnx.commit()
                        if key =="نوع حافظه RAM" :
                           SQL_query="UPDATE laptop_attributes SET RAM=%s WHERE p_id=%s"
                           value=t[match_comma.end()+9:-1]
                           val=(value,int(p_array[i][0]))
                           my_cursor.execute(SQL_query,val)
                           cnx.commit()                              
         
         title_string=str(tla_array[i][0])
         title_array=re.split(',|-|،',title_string)
         for S in title_array:
                 SQL_query="INSERT INTO Laptop_title_alt(p_id,title_alt) VALUES(%s,%s)"
                 if S.strip():
                     val=(int(p_array[i][0]),S)
                     my_cursor.execute(SQL_query,val)
                     cnx.commit()                  
                 
    if ck_array[i][0] == S_T:
         SQL_query="INSERT INTO Tablet VALUES"\
                   "(%s,%s,%s,%s,%s,%s)"
         val=(int(p_array[i][0]),str(ptf_array[i][0]),
                     str(pte_array[i][0]),str(bnf_array[i][0]),str(bne_array[i][0]),
                     str(url_array[i][0]))
         
         my_cursor.execute(SQL_query,val)                 
         title_string=str(tla_array[i][0])
         title_array=re.split(',|-|،',title_string)
         for S in title_array:
                  SQL_query="INSERT INTO Tablet_title_alt(p_id,title_alt) VALUES(%s,%s)"
                  if S.strip():
                     val=(int(p_array[i][0]),S)
                     my_cursor.execute(SQL_query,val)
                     cnx.commit()                  
    if re.search(S_H,str(ck_array[i][0])):
         SQL_query="INSERT INTO Headphone VALUES(%s,%s,%s,%s,%s,%s)"
         val=(int(p_array[i][0]),str(ptf_array[i][0]),
                     str(pte_array[i][0]),str(bnf_array[i][0]),str(bne_array[i][0]),
                     str(url_array[i][0]))
         
         my_cursor.execute(SQL_query,val)
         cnx.commit()
         temp_string=str(pa_array[i][0])
         match_key=re.search(key_pattern,temp_string)
         if match_key:
             SQL_query="INSERT INTO Headphone_attributes(p_id) VALUES(%s)"
             val=(int(p_array[i][0]),)
             my_cursor.execute(SQL_query,val)
             temp_array=temp_string.split('}')
             for t in temp_array:
                match_key=re.search(key_pattern,t)
                if match_key:
                    t=t[match_key.end():]
                    match_comma=re.search(comma_pattern,t)
                    if match_comma:
                        key=t[3:match_comma.end()-2]
                        if key == "ابعاد":
                           SQL_query="UPDATE Headphone_attributes SET dimensions=%s WHERE p_id=%s"
                           value=t[match_comma.end()+9:-1]
                           val=(value,int(p_array[i][0]))
                           my_cursor.execute(SQL_query,val)
                           cnx.commit()
                        if key =="رابط" :
                           SQL_query="UPDATE Headphone_attributes SET connector=%s WHERE p_id=%s"
                           value=t[match_comma.end()+9:-1]
                           val=(value,int(p_array[i][0]))
                           my_cursor.execute(SQL_query,val)
                           cnx.commit()
                        if key == "وزن" :
                           SQL_query="UPDATE Headphone_attributes SET weight=%s WHERE p_id=%s"
                           value=t[match_comma.end()+9:-1]
                           val=(value,int(p_array[i][0]))
                           my_cursor.execute(SQL_query,val)
                           cnx.commit()
                        if key == "طول کابل":
                           SQL_query="UPDATE Headphone_attributes SET cable_length=%s WHERE p_id=%s"
                           value=t[match_comma.end()+9:-1]
                           val=(value,int(p_array[i][0]))
                           my_cursor.execute(SQL_query,val)
                           cnx.commit()
         title_string=str(tla_array[i][0])
         title_array=re.split(',|-|،',title_string)
         for S in title_array:
                  SQL_query="INSERT INTO Headphone_title_alt(p_id,title_alt) VALUES(%s,%s)"
                  if S.strip():
                     val=(int(p_array[i][0]),S)
                     my_cursor.execute(SQL_query,val)
                     cnx.commit()                  
    if re.search(S_S,str(ck_array[i][0])):
         SQL_query="INSERT INTO Speaker VALUES"\
                   "(%s,%s,%s,%s,%s,%s)"
         val=(int(p_array[i][0]),str(ptf_array[i][0]),
                     str(pte_array[i][0]),str(bnf_array[i][0]),str(bne_array[i][0]),
                     str(url_array[i][0]))
                           
         my_cursor.execute(SQL_query,val)
         cnx.commit()                           
         title_string=str(tla_array[i][0])
         title_array=re.split(r',|-|،|\.',title_string)
         for S in title_array:
                  SQL_query="INSERT INTO Speaker_title_alt(p_id,title_alt) VALUES(%s,%s)"
                  if S.strip():
                     val=(int(p_array[i][0]),S)
                     my_cursor.execute(SQL_query,val)
                     cnx.commit()                  

    if re.search(S_GC,str(ck_array[i][0])):
         SQL_query="INSERT INTO Gaming_Console VALUES"\
                   "(%s,%s,%s,%s,%s,%s)"
         val=(int(p_array[i][0]),str(ptf_array[i][0]),
                     str(pte_array[i][0]),str(bnf_array[i][0]),str(bne_array[i][0]),
                     str(url_array[i][0]))
                           
         my_cursor.execute(SQL_query,val)
         cnx.commit()                           
         title_string=str(tla_array[i][0])
         title_array=re.split(r',|-|،|\.',title_string)
         for S in title_array:
                  SQL_query="INSERT INTO Gaming_Console_title_alt(p_id,title_alt) VALUES(%s,%s)"
                  if S.strip():
                     val=(int(p_array[i][0]),S)
                     my_cursor.execute(SQL_query,val)
                     cnx.commit()                  
my_cursor.close()
cnx.close()                                    


 

            
