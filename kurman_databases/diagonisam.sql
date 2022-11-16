CREATE TABLE KATHIGITES (
    kathigites_id integer primary key,
    onoma text not null,
    eidikotiat text not null,
    orario integer not null,
    school text not null,
    polh text not null
);

insert into KATHIGITES values(0001, "Kurmanidhs", "PE86", 18, "2EPAL", "EVOSMOU");
insert into KATHIGITES values(0002, "aegaeg", "PE886", 108, "2EPAL", "EVOSMOU");
insert into KATHIGITES values(0003, "trhjhtj", "PE986", 180, "2EPAL", "EVOSMOU");
insert into KATHIGITES values(0004, "Kurmanitjryerghedhs", "PE866", 181, "2EPAL", "EVOSMOU");
insert into KATHIGITES values(0005, "tsrykyu", "PE856", 108, "2EPAL", "EVOSMOU");
insert into KATHIGITES values(0006, "uyk,k ", "PE846", 018, "2EPAL", "EVOSMOU");
insert into KATHIGITES values(0007, "ryk ryk r", "PE186", 18, "2EPAL", "EVOSMOU");
insert into KATHIGITES values(0008, "rykjryk", "PE836", 108, "2EPAL", "EVOSMOU");
insert into KATHIGITES values(0009, "rykjryweewk", "PE286", 180, "2EPAL", "EVOSMOU");
insert into KATHIGITES values(0010, "rykrws", "PE8846", 108, "2EPAL", "EVOSMOU");

select onoma, eidikotiat from KATHIGITES;
select onoma from KATHIGITES where eidikotiat = "PE8846";

select * from KATHIGITES GROUP BY orario;