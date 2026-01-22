class EmployeeError(Exception):
    pass

class InvalidSalaryError(EmployeeError):
    pass

class Employee:
    def __init__(self, name, salary):
        if not isinstance(name, str) or not name:
            raise ValueError("Numele trebuie să fie un string nevid.")

        if not isinstance(salary, (int, float)) or salary <= 0:
            raise InvalidSalaryError("Salariul trebuie să fie un număr pozitiv.")

        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)

        if not isinstance(department, str) or not department:
            raise ValueError("Departamentul trebuie să fie un string nevid.")

        self.department = department

    def get_details(self):
        return (
            f"Manager: {self.name}, "
            f"Salary: {self.salary}, "
            f"Department: {self.department}"
        )


try:
    emp = Employee("John", 3000)
    mgr = Manager("Alice", 5000, "IT")

    print(emp.get_details())
    print(mgr.get_details())
except EmployeeError as e:
    print("Eroare angajat:", e)
except ValueError as e:
    print("Eroare date:", e)
