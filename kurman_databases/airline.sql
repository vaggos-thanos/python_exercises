create table city (
    c_name varchar(15) not null,
    c_state varchar(15),
    country varchar(30),
    primary key(c_name)
);

insert into city (c_name, c_state, country) values ("Louisville", "Kentaki", "USA");
insert into city (c_name, c_state, country) values ("Euosmos", "Thesalonikh", "Greece");
insert into city (c_name, c_state, country) values ("Fort Worth", "Texas", "USA");

select * from city;

create table airport (
    ap_name varchar(100) not null,
    ap_state varchar(15),
    country varchar(30),
    c_name varchar(15),
    primary key(ap_name),
    foreign key(c_name) references city (c_name) on delete cascade
);

insert into airport (ap_name, ap_state, country, c_name) values ("Louisville IA", "Kentaki", "USA", "Louisville");
insert into airport (ap_name, ap_state, country, c_name) values ("SKG", "Thesalonikh", "Greece", "Euosmos");
insert into airport (ap_name, ap_state, country, c_name) values ("Fort Worth IA", "Texas", "USA", "Fort Worth");

select * from airport;

create table airline(
    airline_id varchar(3) not null,
    al_name varchar(50),
    three_digit_code varchar(3),
    primary key(airline_id)
);

insert into airline values ("AA", "America Airlines", "001");
insert into airline values ("AG", "Air Greece", "018");
insert into airline values ("LH", "Lufthansa", "220");

select * from airline;

create table ticket2 (
    dateBooking date not null,
    source varchar(3) not null,
    destination varchar(3) not null,
    class varchar(15) not null,
    price int,
    primary key(dateBooking, source, destination, class)
);

insert into ticket2 values ('11-05-16', "BOM", "DFW", "ECONOMMY", 95000);
insert into ticket2 values ('11-06-16', "JFK", "BOM", "ECONOMMY", 100000);
insert into ticket2 values ('21-09-16', "IAH", "DEL", "BUSINESS", 200000);

select * from ticket2;

update ticket2 set price = 150000 where dateBooking = '11-05-16' and source = "BOM" and destination = "DFW" and class = "ECONOMMY";

select * from ticket2;
