# Form Normalization of Products Relation of Digikala's Database up to Fifth Normal Form (5NF)
In this project, I used database concepts to normalize the form of the products table of Digikala's database. There were more relations in the dataset provided to us, but the primary key of the products table does not match the foreign keys of the others! So, I just worked with the products table with the following attributes:
* `id`
* `product_title_fa`
* `product_title_en`
* `url_code`
* `title_alt`
* `category_title_fa`
* `category_keywords`
* `brand_name_fa`
* `brand_name_en`
* `product_attributes`
  
`title_alt` is multi-valued, so I created a new table to store its content like `(prod_tilte_id, product_id, title_alt)`. The `product_attributes` which contains lists of KEY-VALUE dictionaries were stored in a new table with KEYs as the columns (attributes) and VALUEs as the entries to make the database 3NF. All of the tables have one primary key and are 3NF. Therefore, they are 5NF.

# Reqiurements
1. Install Pandas. 
2. Install xlrd.
3. Place "5-awte8wbd.xlsx" in the root of the "codes" directory.
4. Make sure there is no database named "digikala_db" in your databases.
5. Run "tables.py" to create the tables and then run "script.py" to load the data.
6. Enter your MySQL root password when the scripts run.
