# mcksinsey_activity

### How to run the Program

The program can be run by running the following on the terminal:
>>python mckinsey.py Bill<1,2,3,Custom>.txt

### Assumptions: 

##### In this activity I am making the followng assumptions
1. All the users are registered in the database (which in this case a simple csv file). Even new customers are regsitered before there bill is processed in this system

2. Two of the same items will be stored as separate entries in the bill. 

3. Only One bill is processed at one time

4. Item IDs and customer IDs are unique


##### Unit Tests: 

Due to time constraints and lack of knowledge on the subject, I was unable to perform Unit Tests. However, in my program I would test the following cases: 
Test Case 1:

	a) Does the program work across all Customer types: Affiliate, Employee, Customer and Loyal Customer
	b) How does the respond if the file (containing the bill) is corrupted
	c) What if the Database vocabulary for certain Fields (Customer Type), item IDs and Customer IDs are not ordered. 
	d) Does the CreateCustomerObject() work for different types pf customers and does the default setting work
	e) Does the program run calculations accordingly for grocery items and other items
