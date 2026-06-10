#Activity 1 – Employee Salary System
# Problem Statement: Create a simple Employee Salary System in Python. The system 
# should allow the user to add employees, display employee records, search for an 
# employee, and increase an employee’s salary.

class EmployeeSystem:
    def __init__(self):
        self.__employees = []

    def addEmployee(self, name, position, salary):
        employee = {
            "name":name,
            "position":position,
            "salary":salary
        }

        self.__employees.append(employee)
        print(name, "has been added to the employee database.")

    def display_employees(self):
        if len(self.__employees) == 0:
            print("There are no employees in the database.")
        else:
            print("\nEMPLOYEE DATABASE")
            print("====================")

            for employee in self.__employees:
                print("Name:", employee["name"])
                print("Position:", employee["position"])
                print("Salary:", employee["salary"])
                print("============================")

    def searchEmployee(self, name):
        for employee in self.__employees:
            if employee["name"].lower() == name.lower():
                print("\nEmployee found!")
                print("Name:", employee["name"])
                print("Position:", employee["position"])
                print("Salary:", employee["salary"])
                return
            
        print("Employee not found.")


    def increase_salary(self,name, amount):
        for employee in self.__employees:
            if employee["name"].lower() == name.lower():
                employee["salary"] += amount
                print("Salary increased successfully.")
                print(f"New Salary: ${employee['salary']}")

                return
        
        print("Employee not found.")
            
    def showEmployees(self):
        return len(self.__employees)

employeelist = EmployeeSystem()

number_of_employees = int(input("How many employees do you want to add? Please enter a valid number: "))

for i in range(number_of_employees):
    print("\nEnter Employee", i + 1)

    name = input("Enter Employee name: ")
    position = input("Enter Employee position: ")
    salary = float(input("Enter Employee salary: "))

    employeelist.addEmployee(name, position, salary)


employeelist.display_employees()

searchName = input("\nSearch Employee: ")
employeelist.searchEmployee(searchName)

print("\nTotal Employees:", employeelist.showEmployees())

increase_salary_choice = input("\nDo you want to increase an employee's salary? (yes/no): ").lower()

if increase_salary_choice == "yes":
    employee_name = input("Enter employee name to increase salary: ")
    increase_amount = float(input("Enter salary increase amount: "))

    employeelist.increase_salary(employee_name, increase_amount)

elif increase_salary_choice == "no":
    print("No salary changes made.")

else:
    print("Invalid choice. Please enter 'yes' or 'no'.")

print("\nUpdated Employee Records:")
employeelist.display_employees()
