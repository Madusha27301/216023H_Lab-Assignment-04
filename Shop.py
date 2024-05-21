from customer import Customer
from employee import Employee
from product import Product

class Shop:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.employees = []
        self.products = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_product(self, product):
        self.products.append(product)

    def __str__(self):
        return (f"Shop: {self.name}\n"
                f"Customers: {', '.join(str(c) for c in self.customers)}\n"
                f"Employees: {', '.join(str(e) for e in self.employees)}\n"
                f"Products: {', '.join(str(p) for p in self.products)}")
