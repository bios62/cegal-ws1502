# Lab 32 instructions

## Purpose of the lab

The purpose of this lab is to  build machine learning models to predict consumption at different speeds and temperatures, based on the TRIP table.



## Prerequisites

Complete lab 1 and ensure that  `TRIP` table is loaded into the schema.


## Database Actions SQL instructions for the first Machine Learning experiment.

We will use machine learning with default parameters and the default Support Vector Machine (SVM) algorithm with a Linear Kernel.
First we need to create the source - for this we will create a view on top of the TRIP table with the necessary data for machine learning: 

## Step 1

```
create or replace view mlinput (ID,KMH,KWP100)as (
SELECT KMH,KMH,KWP100 FROM trip
where km>35 -- ignore short drives where initial car heating can disturb.
and mm is null -- ignore drives with rain/snow 
and hoh is null -- ignore the steepest driving up and down mountains
);

-- Do a select to confirm that it returns data :

select * from mlinput;
```

## Step 2

Next task is to configure this Machine Learning experiment,  by creating a settings table :

```
drop table mlsettingsSVM   -- if exists;
create table mlsettingsSVM (setting_name varchar2(30), setting_value varchar2(30));
```

We will be using Support Vector Machine (SVM) with default parameters - so that we do not need to add any rows to the table in this experiment.

## Step 3

Next task is to create and train the model:

First we drop the model - if it already exists - if not ignore: 
  
```
begin
dbms_data_mining.drop_model(model_name => 'SVM1');
end;
/

--The new Model :

begin
dbms_data_mining.create_model(
model_name => 'SVM1',
MINING_FUNCTION => dbms_data_mining.regression,
data_table_name => 'MLINPUT',
CASE_ID_COLUMN_NAME => 'ID',
TARGET_COLUMN_NAME => 'KWP100',
SETTINGS_TABLE_NAME => 'MLSETTINGSSVM');
end;
/
```  

## Step 4
We can then do some predictions - some examples :
  
  ```
SELECT prediction (SVM1 using 100 AS kmh,20 AS CELSIUS) FROM DUAL;

SELECT prediction (SVM1 using 130 AS kmh,20 AS CELSIUS) FROM DUAL;

SELECT prediction (SVM1 using 100 AS kmh,10 AS CELSIUS) FROM DUAL;
```  

Does it look ok ?
If not, what is wrong ?

## Step 5

Lets repeat: 
  
```
SELECT prediction (SVM1 using 100 AS kmh,20 AS CELSIUS) FROM DUAL;
SELECT prediction (SVM1 using 100 AS kmh,10 AS CELSIUS) FROM DUAL;
```

It looks like the temperature is ignored!
Let's look at the CREATE VIEW STATEMENT source view:

```
create or replace view mlinput (ID,KMH,KWP100)
as (SELECT KMH,KMH,KWP100 FROM trip
where km>35
and mm is null
and hoh is null
);
```  

It looks like we have not included the temperature in the source data  - let's fix it:
  
```
create or replace view mlinput (ID,KMH,KWP100,CELSIUS)
as (SELECT KMH,KMH,KWP100,CELSIUS FROM trip
where km>35
and mm is null
and hoh is null
);

SELECT prediction (SVM1 using 100 AS kmh,20 AS CELSIUS) FROM DUAL;
SELECT prediction (SVM1 using 100 AS kmh,10 AS CELSIUS) FROM DUAL;
```  

Any better now?
Why not?
Let's go to the next step.

## Step 6

We actually need to train the model - once more, now including the celsius column/attribute/feature.

All you have to do is repeat step 3.

And verify that it works now:
  
```
SELECT prediction (SVM1 using 100 AS kmh,20 AS CELSIUS) FROM DUAL;
SELECT prediction (SVM1 using 100 AS kmh,10 AS CELSIUS) FROM DUAL;
```  

## Step 7

Now that the predictions work better, lets wrap it in a standard PL/SQL function:
  
```
create or replace FUNCTION predict_consumption (kmh number,celsius number) 
    RETURN NUMBER IS
    query_str VARCHAR2(1000);
    consumption NUMBER;
BEGIN
query_str :='SELECT 
prediction (SVM1 using
:kmh AS kmh,:celsius AS CELSIUS
)FROM DUAL';

    EXECUTE IMMEDIATE query_str
     INTO consumption
     using kmh,celsius;
    RETURN consumption;
END;
/

--And test it:

select predict_consumption(100,20) from dual;
```  

## Step 7

It would be useful to have a view with consumptions at different speeds and temperatures:
  
```  
create or replace view consumption (celsius,kmh30,kmh50,kmh80,kmh120,kmh150,kmh200) as
select '-10' Celsius, 
predict_consumption(30,-10) "30 KMH",
predict_consumption(50,-10) "50 KMH",
predict_consumption(80,-10) "80 KMH",
predict_consumption(120,-10) "120 KMH",
predict_consumption(150,-10) "150 KMH",
predict_consumption(200,-10) "200 KMH"
from dual
union
select '0', predict_consumption(30,0),
predict_consumption(50,0) ,
predict_consumption(80,0) ,
predict_consumption(120,0),
predict_consumption(150,0) ,
predict_consumption(200,0) 
from dual
union
select '10', predict_consumption(30,10),
predict_consumption(50,10),
predict_consumption(80,10),
predict_consumption(120,10),
predict_consumption(150,10),
predict_consumption(200,10)
from dual
union
select '20',predict_consumption(30,20),
predict_consumption(50,20),
predict_consumption(80,20),
predict_consumption(120,20),
predict_consumption(150,20),
predict_consumption(200,20)
from dual;
```  

Lets test it:
  
```select * from consumption order by celsius;```  

And let's save the result in a table:
  
```
drop table consumptionSVM; -- if exists
  
create table consumptionSVM as select * from consumption;

select * from consumptionSVM order by celsius;
```  
  
## Step 7

Another useful model is the General Linear Model (GLM).
To try this model, we have to repeat the tasks from Step 2 - with some small changes. Let's try the following:
  
```
drop table mlsettingsGLM; -- ignore if table not exists

create table mlsettingsGLM (setting_name varchar2(30), setting_value varchar2(30));

--We will NOT be using Support Vector Machine (SVM) which is the default, but GLM.
--so now, we have to configure the settings:

begin
insert into MLSETTINGSGLM (setting_name, setting_value)  
    values (dbms_data_mining.algo_name, dbms_data_mining.algo_generalized_linear_model);  
end;
/

commit;

--make sure that you have not entered multiple rows with the same parameters:

select * from mlsettingsglm order by setting_name;

--Drop the model if this is not your first attempt:

begin
dbms_data_mining.drop_model(
model_name => 'GLM1');
end;
/

--create the GLM model:

begin
dbms_data_mining.create_model(
model_name => 'GLM1',
MINING_FUNCTION => dbms_data_mining.regression,
data_table_name => 'MLINPUT',
CASE_ID_COLUMN_NAME => 'ID',
TARGET_COLUMN_NAME => 'KWP100',
SETTINGS_TABLE_NAME => 'MLSETTINGSGLM');
end;
/
```  

And test it: 
  
```
SELECT prediction (GLM1 using 100 AS kmh,20 AS CELSIUS) FROM DUAL;
SELECT prediction (GLM1 using 100 AS kmh,10 AS CELSIUS) FROM DUAL;

--And compare it to SVM1

SELECT prediction (SVM1 using 100 AS kmh,20 AS CELSIUS) FROM DUAL;
SELECT prediction (SVM1 using 100 AS kmh,10 AS CELSIUS) FROM DUAL;
```  


## Step 7

Maybe we should switch to using SVM1.  Here is one simple way to switch between the models:
  
```
create or replace FUNCTION predict_consumption_flex (kmh number,celsius number,modelName varchar2) 
    RETURN NUMBER IS
    query_str VARCHAR2(1000);
    consumption NUMBER;
BEGIN
query_str :='SELECT 
prediction ('||modelName||' using
:kmh AS kmh,:celsius AS CELSIUS
)FROM DUAL';

    EXECUTE IMMEDIATE query_str
     INTO consumption
     using kmh,celsius;
    RETURN consumption;
END;
/

select predict_consumption_flex(100,20,'SVM1') from dual;
select predict_consumption_flex(100,20,'GLM1') from dual;
```  

And then we replace to old predict_consumption function with this:
  
```
create or replace FUNCTION predict_consumption (kmh number,celsius number) 
    RETURN NUMBER IS
    query_str VARCHAR2(1000);
    consumption NUMBER;
BEGIN
-- select model by commenting out the not used one:
--RETURN predict_consumption_flex (kmh ,celsius ,'SVM1'); 
RETURN predict_consumption_flex (kmh ,celsius ,'GLM1'); 

END;
/
```
  
A more flexible way could be to have a table with the current selected model - but we will not do that today.
  
Let's query the old view - with the new GLM model : 
  

```
select * from consumption order by celsius;

--and compare it to the old SVM:

select * from consumptionSVM order by celsius;
```  
  
If we have followed the instructions correctly - and those instructions are correctly, we should have two slightly different predictions.
It is interesting that the biggest difference is at the extremes 30 kmh, 150 and 200 kmh.
Since the input data does not contain speeds above 140kmh - we cannot be sure about the quality of these predictions.
  
Finally since sql is fun - lets save also the GLM1 prediction in a table:
  
```
drop table consumptionGLM -- if already existing;

create table consumptionGLM as select * from consumption;
```  
  
## Step 8

In order to make sure that we are on the right track - let's do a few final analysis, by comparing predicted vs. actual consumption:
  
```
select trip.*,predict_consumption(kmh,celsius),
abs(predict_consumption(kmh,celsius)-kwp100) 
from trip
order by dato,kl;
```  

Or if we want to list the predictions, starting with the worst from the top:
  
```
select trip.*,predict_consumption(kmh,celsius),
abs(predict_consumption(kmh,celsius)-kwp100) 
from trip
order by abs(predict_consumption(kmh,celsius)-kwp100) desc;
```  

We can probably study the result for hours - to try to understand the data better.
However there are at least two major flaws in the used methology!
Any suggestions ?

But are SVM or GLM the most accurate?
Lets sum up the discrepancies:
  
```
select 'SVM',sum(abs(predict_consumption_flex(kmh,celsius,'SVM1')-kwp100)) 
from trip
union all
select 'GLM',sum(abs(predict_consumption_flex(kmh,celsius,'GLM1')-kwp100)) 
from trip;
```  
  
This one excludes short trips, rain/snow and mountain trips  ?
  
```
select 'SVM',sum(abs(predict_consumption_flex(kmh,celsius,'SVM1')-kwp100)) 
from trip
where km>35 and mm is null and hoh is null
union all
select 'GLM',sum(abs(predict_consumption_flex(kmh,celsius,'GLM1')-kwp100)) 
from trip
where km>35 and mm is null and hoh is null;
```


