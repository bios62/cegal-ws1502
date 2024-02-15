# Lab 3 instructions, Build ORDS REST API


## Interactive instructions, ORDS creation

When creating APIs with ORDS there are 3 basic steps:
- Create the module, which is a collection of APIs
- Create a template, which is the name of the API
- create  ahandler, one handler for each HTTP verb, GET, POST, PATCH, DELETE
  
By defalt the URI will be: /ords/dbschema/module/template

Create ORDS module wsapi

The ORDS module will be the first part of the API path, and act as a placeholder for a set of APIs.  

Navigate to the ORDS screen in dbactions  

![ORDS Screen](../images/ords1.jpg)

Select modules from top menu  

![ORDS Screen](../images/ords2.jpg)
  
Click create module, enter name "wsapi", leave the rest, click create  

![ORDS Screen](../images/ords3.jpg)

![ORDS Screen](../images/ords4.jpg)
  
Module created.  

Next step is to create the 3 POST REST APIs for updating tge logdata table or current_speed table.
Firs API is tempkmh for inserting a new record into the logdata table with both temp and kmh from the payload.  

In the workshop title, select create template

![ORDS Screen](../images/ords5.jpg)  
  
Creating the tempkmh REST API with POST  
Click on "create template"  
Enter Template name "tempkmh", click create  

![ORDS Screen](../images/ords6.jpg)
  
Template created, note the Create Handler
Click create handler 

![ORDS Screen](../images/ords7.jpg)

Select POST and add PL/SQL statement: 

`begin insert into logdata (temp,kmh) values(:temp,:kmh); commit; end;`  

![ORDS Screen](../images/ords8.jpg)

![ORDS Screen](../images/ords9.jpg)

Navigate to MIMEs allowed and select application/json and click add  
  
![ORDS Screen](../images/ords10.jpg)

![ORDS Screen](../images/ords11.jpg)

![ORDS Screen](../images/ords12.jpg)

The first REST API handlers is complete

![ORDS Screen](../images/ords13.jpg)

Well done, first API created, navigate back to "workshop"    
  
![ORDS Screen 14](../images/ords14.jpg)
  
Creating the temp REST API with POST  
The temp API updates the logdata with temp from the payload and the speed from the current_speed table.  
Repeat the steps for creating the temp REST API with POST,but do not add MIMEs allowed.  


![ORDS Screen](../images/ords15.jpg)

Click create handler  

![ORDS Screen](../images/ords16.jpg)

Enter the PL/SQL below in the handler:  

`begin insert into logdata (temp) values(:temp); commit; end;` 

![ORDS Screen](../images/ords17.jpg)  

The micropython implementation does not support setting header variables like "Content Type", and the REST API need
to discard lack of MIME type. Skip setting of MIMEs allowed for this API


The REST API temp is added. 

![ORDS Screen](../images/ords19.jpg)

Creating the kmh REST API with POST 
the kmh API ipdates the current_speed table, not the logdata table  
 Repeat the steps and add REST API KMH, click create template

![ORDS Screen](../images/ords20.jpg)  

Create template kmh  

![ORDS Screen](../images/ords21.jpg)

Create the POST handler for kmh

![ORDS Screen](../images/ords22.jpg)

Add the following PL/SQL in the POST handler:  
`begin insert into current_speed (kmh) values(:kmh); commit; end;` 

![ORDS Screen](../images/ords23.jpg)

![ORDS Screen](../images/ords24.jpg)

The REST API kmh is complete  

![ORDS Screen](../images/ords25.jpg)

Finally lets create two GET APIs one for making a prediction and one for fetching the latest 25 rows form the logdata table

Predict GET deviates a bit.  
This REST API select ad value with a PL/SQL having two input query parameters  


Create template predict  
  
![ORDS Screen](../images/ords30.jpg)

Add the handler for GET  

![ORDS Screen](../images/ords31.jpg)
  
Select Source type PL/SQL and add the following PL/SQL in the GET handler:  
   
`begin :p_result:=predict_consumption(:p_kmh,:p_temp); end;` 

![ORDS Screen](../images/ords32.jpg)

Add MIMEs Allowed  

![ORDS Screen](../images/ords33.jpg)

For PL/SQL type GET we need to define the result data that will be in the JSON response.
We define a response value name "response" as a OUT parameter with the PL/SQL variable p_result as bind variable  
Clict create parameter  

![ORDS Screen](../images/ords34.jpg)

The GET REST API needs to define the return value from the PL/SQL function as a parameter  
Create the parameter:  

![ORDS Screen](../images/ords34.jpg)

And the REST API GET predict is complete

![ORDS Screen](../images/ords35.jpg)


As the last API lets create the tempkmh GET api fro retrieving the 25 newest records from the logdata table.
Note that the API URL is the same as the POST above, but the handler is a GET handler, in reality a new API.
Navigate back to the tempkmh template.  

Create template tempkmh GET API 
  
![ORDS Screen](../images/ords40.jpg)

  
Select Source type  ords.source_type_collection_feed and add the following SQL in the GET handler:  
   
`select logtime,temp,kmh from logdata order by logtime desc`

![ORDS Screen](../images/ords41.jpg)

Add MIMEs Allowed  

![ORDS Screen](../images/ords42.jpg)

The creation of tempkmh API complete.

This completse the creation of the REST API.

A simple test, add the URL to the last GET API in your browser:

`https://<your ATP URL>/ords/<your username>/wsapi/`

and observe the result.



