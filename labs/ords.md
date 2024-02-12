# Lab 3 instructions, Build ORDS REST API


## Build ORDS REST API with script

Copy/paste the script create_ords.sql [](../files/create_ords.sql) into dbactions, and run as script, or do the interactive lab

## Interactive instructions, ORDS creation

Create ORDS module
Navigate to the ORDS screen in dbactions  

![ORDS Screen](../images/ords1.jpg)

Select modules from top menu  

![ORDS Screen](../images/ords2.jpg)
  
Click create module, enter name "workshop", leave the rest, click create  

![ORDS Screen](../images/ords3.jpg)

![ORDS Screen](../images/ords4.jpg)
  
Module created, In the workshop title, select create template

![ORDS Screen](../images/ords5.jpg)

You will now create the tempkmh REST API with POST  
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
  
Repeat the steps for creating the temp REST API with POST  

![ORDS Screen](../images/ords15.jpg)

Click create handler  

![ORDS Screen](../images/ords16.jpg)

Enter the PL/SQL below in the handler:  

`begin insert into logdata (temp) values(:temp); commit; end;` 

![ORDS Screen](../images/ords17.jpg)

![ORDS Screen](../images/ords18.jpg)

![ORDS Screen](../images/ords19.jpg)

The REST API temp is added.  

![ORDS Screen](../images/ords20.jpg)  

Repeat the steps and add REST API kmh, POST. 
Add the following PL/SQL in the POST handler:  
`begin insert into current_speed (kmh) values(:kmh); commit; end;` 

![ORDS Screen](../images/ords21.jpg)

![ORDS Screen](../images/ords22.jpg)

![ORDS Screen](../images/ords23.jpg)

![ORDS Screen](../images/ords24.jpg)

![ORDS Screen](../images/ords25.jpg)

The last REST API, preditct GET deviates a bit.  
This REST API select ad value with a PL/SQL having two input query parameters

Repeat the steps and add REST API predict, GET. 
Add the following PL/SQL in the POST handler:  
`begin :p_result:=predict_consumption(:p_kmh,:p_temp); end;` 

![ORDS Screen](../images/ords30.jpg)

![ORDS Screen](../images/ords31.jpg)

![ORDS Screen](../images/ords32.jpg)

![ORDS Screen](../images/ords33.jpg)

![ORDS Screen](../images/ords34.jpg)

The GET REST API needs to define the return value from the PL/SQL function as a parameter  
Create the parameter:  

![ORDS Screen](../images/ords34.jpg)

![ORDS Screen](../images/ords35.jpg)



