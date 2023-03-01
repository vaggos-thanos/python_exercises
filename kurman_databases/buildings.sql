create table buildings (
    building_no int primary key auto_increment,
    building_name varchar(255) not null,
    building_address varchar(255) not null
);

create table rooms (
    room_no int primary key auto_increment,
    room_name varchar(255) not null,
    building_no int not null,
    foreign key (building_no) references buildings(building_no) on delete cascade
);

insert into buildings (building_name, building_address) values
('Building 1', 'Address 1'),
('Building 2', 'Address 2'),
('Building 3', 'Address 3');

select * from buildings;

insert into rooms (room_name, building_no) values
('Room 1', 1),
('Room 2', 1),
('Room 3', 2),
('Room 4', 2),
('Room 5', 3),
('Room 6', 3);

select * from rooms;

delete from buildings where building_no = 2;

select * from rooms;

create table vehicles (
    vechicleId int,
    year int not null,
    make varchar(100) not null,
    primary key (vechicleId)    
);

insert into vehicles (vechicleId, year, make) values
(1, 2010, 'Toyota'),
(2, 2011, 'Honda'),
(3, 2012, 'Ford'),
(4, 2013, 'Chevy'),
(5, 2014, 'Nissan');

alter table vehicles add column model varchar(100) not null;

select * from vehicles;

alter table vehicles add column color varchar(100), add column note varchar(255);

select * from vehicles;

create table carts (
    cartId int not null auto_increment,
    cartId_product int not null,
    cartPrice decimal(10,2) not null default "0.00",
    cartQuantity int not null default "1",
    cart_datetime datetime not null,
    cart_ip varchar(100) not null collate "utf8_general_ci",
    primary key (cartId) using btree
)
collate = "utf8_general_ci" engine = InnoDB auto_increment = 6;

insert into carts values
(20, 1, 12.1, 3, NOW(), "SomeWhere");

select * from carts;

update carts set cartQuantity = case when cartQuantity >= 2 then cartQuantity - 1 else 1 end where cartId = 20 and cart_ip = "SomeWhere";