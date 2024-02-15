--
-- Dummy function that generates prediction
--
create or replace function predict_consumption(kmh integer,temp in integer) return integer is
  kwh number;
  seed integer;
begin
  select ((sysdate - TO_DATE('01-JAN-1970','DD/MM/YYYY'))*24*60*60) into seed from dual;
  dbms_random.seed(seed);
  kwh:=dbms_random.value(1,1000)/10;
  return(kwh);
end;
/