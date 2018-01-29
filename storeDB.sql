create database store;
use store;


drop table categories;
create table categories(
id int  auto_increment primary key,
name text
);

insert into categories values
(1,"Vegetables"),
(2,"Fruits"),
(3,"Dairy");

drop table products;
create table products(
id int auto_increment primary key,
title text not Null,
description text not Null,
price float not Null,
img_url text not Null,
category int not Null,
favorite boolean,
creation_time datetime default current_timestamp
);

 
insert into products values
(1,"Banana","Banana",1.95,"./images/banana.jpg",2,1,current_timestamp),
(2,"Cherry tomato","Cherry tomato in a 50 gr plastic box",10.56,"./images/cherry_tomate.jpg",1,1,current_timestamp),
(3, "Milk carton 3%","Tnuva 3% fat milk in a carton",11.90,"./images/3%_milk_carton.jpg",3,1,current_timestamp),
(4,"Cottage cheese 5%","Tnuva 5% cottage cheese 250 gr box",5.95,"./images/Cottage_Cheese_5_Tnuva_250G.jpg",3,0,current_timestamp),
(5,"Cucumber","Cucumber",4.34,"./images/Cucumber.jpg",1,0,current_timestamp),
(6,"Green Apple","Granny smith green apple",7.83,"./images/granny_smith_apple.jpg",2,0,current_timestamp);


ALTER TABLE products
ADD constraint FK_products1 FOREIGN KEY (category) REFERENCES categories(id)
on update cascade
on delete restrict;

