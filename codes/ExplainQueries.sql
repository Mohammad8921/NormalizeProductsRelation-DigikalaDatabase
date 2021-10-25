CREATE INDEX M_index ON mobile(brand_name_en);
-- query1
EXPLAIN SELECT * FROM mobile;
-- query2
EXPLAIN SELECT m.product_id,mta.title_alt FROM mobile m 
INNER JOIN mobile_title_alt mta ON m.product_id=mta.p_id WHERE brand_name_en='BlackBerry';
-- query3
EXPLAIN SELECT product_title_fa FROM mobile ORDER BY product_id;
-- query4
EXPLAIN SELECT m.product_id,mta.title_alt FROM mobile m 
INNER JOIN mobile_title_alt mta ON m.product_id=mta.p_id WHERE product_id=818774;
-- query5
EXPLAIN SELECT url_code FROM mobile WHERE brand_name_en='Blu' OR product_id=818952;
