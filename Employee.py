from person import Person

class Employee(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position

    def __str__(self):
        return f"Employee {self.name}, ID: {self.employee_id}, Position: {self.position}, {self.age} years old"
