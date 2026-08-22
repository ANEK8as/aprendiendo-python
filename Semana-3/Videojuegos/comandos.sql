select * from estudiantes
update estudiantes set edad=23 where nombre = 'Juanjose'
delete from estudiantes where nombre = 'Jhael';
select * from estudiantes
create table videojuegos(
Id serial primary key,
Nombre VARCHAR(100),
Ano INTEGER,
Genero VARCHAR(100)
)
select * from videojuegos;
insert into videojuegos (nombre, ano, genero)
Values ('Ark survival evolved', 2017,'supervivencia')
insert into videojuegos (nombre, ano, genero)
Values ('minecraft', 2009,'supervivencia')
insert into videojuegos (nombre, ano, genero)
Values ('halo', 2001,'fps')
insert into videojuegos (nombre, ano, genero)
Values ('doom', 1993,'fps')
insert into videojuegos (nombre, ano, genero)
Values ('Dead Space', 2008,'Tps')
select * from videojuegos
select * from videojuegos where genero = 'fps';
select nombre from videojuegos
select * from videojuegos order by ano desc;
select * from videojuegos where ano > 2005;




