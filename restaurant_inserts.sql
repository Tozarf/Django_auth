INSERT INTO menu_meals (mealtype) VALUES
('Pizza'),
('Tacos'),
('Burger'),
('Boneless'),
('French Fries');

INSERT INTO menu_mealtypes(name, grams, price, mealtype_id) VALUES 
('Pepperoni',841,170,(SELECT id FROM menu_meals WHERE mealtype = 'Pizza')),
('Hawaiana',920,170,(SELECT id FROM menu_meals WHERE mealtype = 'Pizza')),
('Pastor',300,80,(SELECT id FROM menu_meals WHERE mealtype = 'Tacos')),
('Asada',320,80,(SELECT id FROM menu_meals WHERE mealtype = 'Tacos')),
('Sirloin',500,130,(SELECT id FROM menu_meals WHERE mealtype = 'Burger')),
('Cheese',450,100,(SELECT id FROM menu_meals WHERE mealtype = 'Burger')),
('BBQ',300,95,(SELECT id FROM menu_meals WHERE mealtype = 'Boneless')),
('Buffalo',310,95,(SELECT id FROM menu_meals WHERE mealtype = 'Boneless')),
('Classic',200,60,(SELECT id FROM menu_meals WHERE mealtype = 'French Fries')),
('Special',300,90,(SELECT id FROM menu_meals WHERE mealtype = 'French Fries'));



INSERT INTO dish_dish (mealtype,name,price,quantity,subtotal) VALUES
('Pizza', 'Pepperoni',170,4,680),
('Burger', 'Sirloin',130,2,260),
('Boneless', 'Buffalo',95,1,95),
('French Fries', 'Special',90,2,180);

INSERT INTO order_specs_order (order_date, order_table,payment,identification, delivery, total ) VALUES
('25/08/21',1,'NFC','Passport', 'To Go',780),
('26/08/21',1,'Credit/debit card','Drivers License', 'In Place',1233),
('27/08/21',7,'Cash','Passport', 'In Place',772),
('12/08/21',12,'NFC','Passport', 'To Go',400),
('02/08/21',4,'Cash','School Id', 'To Go',130),
('05/08/21',2,'Credit/debit card','School Id', 'To Go',300);



INSERT INTO "RestaurantData_restaurant_type" ("description") VALUES ('Drive Thru'),('In Place');

INSERT INTO "RestaurantData_direction" (city,pc,street,int_num,ext_num,"state","location")VALUES
('Durango','34220','Paramaribo',0,111,'Durango','24.041562814893414, -104.62595201475844'),
('Guadalajara','44240','Independencia',0,3295,'Jalisco','20.7190572040002, -103.3189538019302'),
('Durango','34200','Bvd. De Las Rosas',0,245,'Durango','24.0448646289323, -104.63648595914054'),
('CDMX','06300','Heroes',0,192,'CDMX','19.448708733080405, -99.14530642047794');


INSERT INTO "RestaurantData_restaurant" ("name",opening_hour,closing_hour,direction_id,phone,restaurant_id)VALUES
('Burgers Paseo Durango','11:00 AM','10:00 PM',3,'6183029281',2),
('Burgers Tlaquepaque','11:30 AM','10:30 PM',4,'6183034281',1),
('Burgers Jardines de Durango','10:00 AM','10:00 PM',5,'6183034981',2),
('Burgers Plaza Fundadores','10:00 AM','10:30 PM',6,'6183029926',1);

INSERT INTO "order_order_status" ("description") VALUES ('Preparing'),('Done');


INSERT INTO "order_order" ("time", restaurant_id, status_id, "user_id")VALUES
('11:31',3,2,1);

INSERT INTO "order_product_detail" (quantity,order_id,product_id)VALUES
(3,1,3);

INSERT INTO  products_product ("name",price,"description","image") VALUES
('Hawaiana',120, 'Beef burger with pineapple','https://www.ambitiouskitchen.com/wp-content/uploads/2015/08/Sweet-Spicy-BBQ-Bacon-Hawaiian-Turkey-Burgers-square-480x270.jpg'),
('Salchiburguer',120,'Beef burger with sausage slices','https://d1ralsognjng37.cloudfront.net/84708692-6f32-4a89-a685-8a8f87a3a3b3.jpeg'),
('Regular', 80, 'Beef burger','https://i.pinimg.com/736x/da/51/57/da5157dcc8f20cc8afa749075adc98ce--the-list-fast-foods.jpg'),
('Especial', 95, 'Beef burger with a mushrooms sauce', 'https://www.neo2.com/wp-content/uploads/2020/11/burger-king-selection-angus-trufada-setas-01.jpg');
