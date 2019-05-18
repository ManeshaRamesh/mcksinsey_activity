import time
import sys

# Macros
PROFILE_ID = 0
PROFILE_NAME = 1
PROFILE_TYPE = 2
PROFILE_REGISTERED_TIME = 3
NM_DISCOUNT = 5


# Parent class for calucalting discounts and benefits
class Customer:
	def __init__(self, cust_id, cust_name, PurchaseObj):

		self._name = cust_name
		self._id = cust_id
		self._discount = NM_DISCOUNT
		self._BuyItems = PurchaseObj
		self._discount_threshold = 100
	def calculate_payment(self):
		# print(self.BuyItems.item)
		total_amount = 0
		for product in self._BuyItems.item:
			# if (product[2]== "gorceries"):
			# 	total += float(product[3])
			total_amount += float(product[3])
		return(total_amount - self._discount*int(total_amount/self._discount_threshold))
		
#Child class calculates discounts and benefits for an Employee
class Employee(Customer):
	def __init__(self, cust_id, cust_name, PurchaseObj):
		Customer.__init__(self, cust_id, cust_name, PurchaseObj)
		self._discount = 30

	def calculate_payment(self):
		total_amount = 0
		for product in self._BuyItems.item:
			if (product[2]== "grocery"):
				print(product[0] + " " + product[1] + " " + product[3])
				total_amount += float(product[3])
			else:
				print(product[0] + " " + product[1] + " " + product[3])
				total_amount = float(self._discount)/100*float(product[3])
		return total_amount

#Child class calculates discounts and benefits for an Affiliate
class Affiliate(Customer):
	def __init__(self, cust_id, cust_name, PurchaseObj):
		Customer.__init__(self, cust_id, cust_name, PurchaseObj)
		self._discount = 10

	def calculate_payment(self):
		total_amount = 0
		for product in self._BuyItems.item:
			if (product[2]== "grocery"):
				print(product[0] + " " + product[1] + " " + product[3])
				total_amount += float(product[3])
			else:
				print(product[0] + " " + product[1] + " " + product[3])
				total_amount = float(self._discount)/100*float(product[3])
		return total_amount
#Child class calculates discounts and benefits for a Loyal Customer
class LoyalCustomer(Customer):
	def __init__(self, cust_id, cust_name, PurchaseObj):
		Customer.__init__(self, cust_id, cust_name, PurchaseObj)
		self._discount = 5

	def calculate_payment(self):
		total_amount = 0
		for product in self._BuyItems.item:
			if (product[2]== "grocery"):
				print(product[0] + " " + product[1] + " " + product[3])
				total_amount += float(product[3])
			else:
				print(product[0] + " " + product[1] + " " + product[3])
				total_amount = float(self._discount)/100*float(product[3])
		return total_amount
# Purchcase class contains all the items fora given customer
class Purchase:
	item = []	
	def load_items(self):
		item_list = open("database/items.csv", "r")
		for line in item_list: 
			product = line.rstrip().split(",")
			self.item.append(product)
		item_list.close()
		return 
	

# looks up a customer's information	
def lookup_CustomerID(id):
	database = open("database/customer_database.csv", "r")
	for line in database: 
		profile = line.rstrip().split(",")
		if (int(id) == int(profile[PROFILE_ID])):		
			# print(profile)
			break
	
	database.close() 
	return(profile[PROFILE_NAME],profile[PROFILE_TYPE], profile[PROFILE_REGISTERED_TIME])
	
# Associates a customer to the appropriate Customer class 
def CreateCustomerObject(id, name, userType, registration_time,  PurchaseObj):
	if userType == "Other":
		epoch_year = 31557600
		year_threshold = 2
		current_time = time.time()
		if (current_time - float(registration_time) > (epoch_year*year_threshold)): 
			print("Category: Normal Customer")
			obj = Customer(id,name, PurchaseObj)
		else: 
			print("Category: Loyal Customer")
			obj = LoyalCustomer(id,name, PurchaseObj)
		return(obj)
	if userType == "Employee":
		print("Category: Employee")
		obj = Employee(id, name, PurchaseObj)
		return (obj)
	if userType == "Affiliate":
		print("Category: Affiliate")
		obj = Affiliate(id,name, PurchaseObj)
		return(obj)

def main(): 
	if len(sys.argv) < 2: 
		print ("Specify file name - Should be one of the following: Bill1.txt, Bill2.txt, Bill3.txt, BillCustom.txt")
		return
	
	filename = sys.argv[1]

	#get bill
	bill = open(filename, "r")
	#get name and customer id from Bill
	# name = bill.readline().rstrip()
	id = bill.readline().rstrip()
	#lookup information on the customer - registration time and customer Type
	name, userType,reg_time = lookup_CustomerID(id)
	print("Name: " + name)
	#extract items in the bill and store then in dictionary
	#convert the following to dictionary
	TheItems = Purchase();
	ItemNum= bill.readline().rstrip().split(",")[0]
	TheItems.load_items()
	# pass in the items to get a discount for each customer
	CustomerObj = CreateCustomerObject(id,name, userType,reg_time,TheItems)
	print ("Total Sum: " + str(CustomerObj.calculate_payment()))


	bill.close()

main()
