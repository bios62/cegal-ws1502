rem
rem Version: 06.02.204
rem collected_data table
rem
rem historical data used for ML predictions
rem
rem
drop table trip;
CREATE TABLE trip 
   (          "DATO" DATE, 
              "KL" NUMBER(38,0), 
              "KM" NUMBER(38,1), 
              "KMH" NUMBER(38,1), 
              "KWP100" NUMBER(38,1), 
              "KW" NUMBER(38,1), 
              "ECO" NUMBER(38,1), 
              "DCFC" VARCHAR2(26 BYTE) COLLATE "USING_NLS_COMP", 
              "TARGET" VARCHAR2(26 BYTE) COLLATE "USING_NLS_COMP", 
              "COUNTRY" VARCHAR2(2 BYTE) COLLATE "USING_NLS_COMP", 
              "GEO" VARCHAR2(2 BYTE) COLLATE "USING_NLS_COMP", 
              "CELSIUS" NUMBER, 
              "MM" NUMBER, 
              "HOH" NUMBER(*,0), 
              "HDIF" NUMBER
   )
/
rem
rem logdata table
rem
rem collects runtime data from sensor
rem temp current outdoor temp
rem kmh current speed 
rem
drop table logdata;
create table logdata (
  id number GENERATED by default on null as IDENTITY,
  logtime timestamp DEFAULT CURRENT_TIMESTAMP,
  temp number(6,2),
  kmh number(6,1)
)
/

rem current_speed table
rem
rem Used to simlate current_speed registration
rem The device does not collect speed, only temp.
rem Current speed needs to be added manually
rem always pick latest and greates
drop table current_speed;
create table current_speed (
  id number GENERATED by default on null as IDENTITY,
  logtime timestamp DEFAULT CURRENT_TIMESTAMP,
  kmh number(6,1)
);
rem
rem trigger for consuming default value if kmh is not set
rem
create or replace trigger default_speed 
Before insert
    on logdata
    For each row    
declare 
  speed number;
begin
    if :new.kmh is NULL then
       select kmh into speed from current_speed where logtime=(select max(logtime) from current_speed);
        :new.kmh:=speed;
    end if;
end;
/
rem
rem insert dummy speed
rem
insert into current_speed (kmh) values('17.2');
rem
rem insert first vale into logtable
rem
insert into logdata (temp) values ('-0.5');
commit;

