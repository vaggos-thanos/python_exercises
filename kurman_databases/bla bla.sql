create table manufactures (
    manufacturer_id int unsigned not null auto_increment,
    manufacturer varchar(50) not null,
    create_date timestamp not null default current_timestamp,
    last_uptade timestamp not null default current_timestamp on update current_timestamp,
    primary key(manufacturer_id)
)
engine = InnoDB auto_increment = 1001;

insert into manufactures (manufacturer) values ('Beagle Aircraft Limited');

select manufacturer_id from manufactures where manufacturer = 'Beagle Aircraft Limited';

create table airplanes (
    plane_id int unsigned not null auto_increment,
    plane varchar(50) not null,
    manufacturer_id int unsigned not null,
    engine_type varchar(50) not null,
    engine_count tinyint not null,
    max_weight mediumint unsigned not null,
    wingspan decimal(5 , 2) not null,
    plane_length decimal(5 , 2) not null,
    parking_area int generated always as (wingspan * plane_length) stored,
    icao_code char(4) not null,
    create_date timestamp not null default current_timestamp,
    last_uptade timestamp not null default current_timestamp on update current_timestamp,
    primary key (plane_id)
)
engine = InnoDB auto_increment = 101;

insert into airplanes (plane, manufacturer_id, engine_type, engine_count, wingspan, plane_length, max_weight, icao_code)
values
('A.61 Terrier', 1008, 'piston', 1, 36, 23.25, 2400, 'AUS6'),
('B.121 Pup', 1008, 'piston', 1, 31, 23.17, 1600, 'PUP'),
('B.206', 1008, 'piston', 2, 55, 33.67, 7500, 'BASS'),
('D.4-108', 1008, 'piston', 1, 36, 23.33, 1900, 'D4'),
('D.5-108 Husky', 1008, 'piston', 1, 36, 23.17, 2400, 'D5');

select * from airplanes
