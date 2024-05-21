from person import Person

class Customer(Person):
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self.customer_id = customer_id

    def __str__(self):
        return f"Customer {self.name}, ID: {self.customer_id}, {self.age} years old"
