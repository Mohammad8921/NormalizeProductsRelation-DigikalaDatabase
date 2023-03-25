# Normalize Products Relation of Digikala Database up to Fifth Normal Form 
In this project, I used database concepts to normalize the form of products table of Digikala. There was more relations in the dataset provided to us, but the Primary Key i.e. the key of products table does not match to the Forign Keys of the others !!. So I just worked with the products table with the following attributes:
* 'product_title_fa'
* product_title_en
* url_code
* title_alt
* category_title_fa
* category_keywords
* brand_name_fa
* brand_name_en
* product_attributes

# Reqiurements
1. Install Pandas. 
2. Install xlrd.
3. Place "5-awte8wbd.xlsx" in the root of "codes" directory.
4. Make sure there is no database named "digikala_db" in your databases.
5. Run "tables.py" to create tables and then run "script.py" to load data.
6. Enter your mysql root password when the scripts run.
