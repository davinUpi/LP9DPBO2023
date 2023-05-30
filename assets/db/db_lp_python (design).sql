/**
* revamped db_tp_php
* added 'series' table since both figure and figure_info
* display teh same table in tkinter
*/

create table manufacturers(
    man_id int primary key auto_increment,
    man_name varchar(25) unique,
    man_figures int default 0
);

create table figure_types(
    type_id int primary key auto_increment,
    type_name varchar(20) unique,
    type_figures int default 0
);

create table series(
    series_id int primary key auto_increment,
    series_name varchar(50) unique,
    series_figures int default 0
);

create table figures(
    fig_id bigint primary key auto_increment,
    fig_name varchar(50) unique,
    fig_img varchar(255) unique,
    type_id int,
    man_id int,
    series_id int,

    foreign key(type_id) references figure_types(type_id) on delete cascade,
    foreign key(man_id) references manufacturers(man_id) on delete cascade,
    foreign key(series_id) references series(series_id) on delete cascade

);

/**
* triggers for the number of figures
*/

delimiter $$
create trigger num_fig_adder
AFTER INSERT ON figures
for each row
begin
    update manufacturers as A
    set A.man_figures =  A.man_figures + 1
    where A.man_id = NEW.man_id;

    update figure_types as B
    set B.type_figures = B.type_figures + 1
    where B.type_id = NEW.type_id;

    update series as C 
    set C.series_figures = C.series_figures + 1
    where C.series_id = NEW.series_id;
end$$
delimiter ;

delimiter $$
create trigger num_fig_subtractor
after delete on figures
for each row
begin
    update manufacturers as A
    set A.man_figures = A.man_figures - 1
    where A.man_id = OLD.man_id;

    update figure_types as B
    set B.type_figures = B.type_figures - 1
    where B.type_id = OLD.type_id;

    update series as C 
    set C.series_figures = C.series_figures - 1
    where C.series_id = OLD.series_id;
end$$
delimiter ;

/**
* view tables
*/

create view figure_info as
select fig_id as id, fig_name as name, fig_img as img, 
       A.type_name as type, B.man_name as manufacturer, 
       C.series_name as series from figures
       join figure_types as A on figures.type_id = A.type_id
       join manufacturers as B on figures.man_id = B.man_id
       join series as C on figures.series_id = C.series_id; 