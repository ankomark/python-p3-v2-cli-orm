from models.department import Department
from models.employee import Employee
def list_employees():
    employees = Employee.get_all()  # Assuming you have a method to get all employees
    for employee in employees:
        print(employee)

def exit_program():
    print("Goodbye!")
    exit()

def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')

def find_department_by_id():
    try:
        id_ = int(input("Enter the department's id: "))
        department = Department.find_by_id(id_)
        print(department) if department else print(f'Department {id_} not found')
    except ValueError:
        print("Invalid ID. Please enter a valid integer.")

def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        if not name or not isinstance(name, str):
            raise ValueError("Name cannot be empty and must be a string")
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)
def find_employee_by_id(employee_id):
    employee = Employee.query.get(employee_id)  # Adjust this query based on your ORM
    if employee:
        return employee
    else:
        print(f"Employee with ID {employee_id} not found.")
        return None
def find_employee_by_id(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        return employee
    else:
        print(f"Employee with ID {employee_id} not found.")
        return None



def update_department():
    try:
        id_ = int(input("Enter the department's id: "))
        department = Department.find_by_id(id_)
        if department:
            name = input("Enter the department's new name: ")
            location = input("Enter the department's new location: ")

            if not name or not isinstance(name, str):
                raise ValueError("Name cannot be empty and must be a string")

            department.name = name
            department.location = location
            department.update()
            print(f'Success: {department}')
        else:
            print(f'Department {id_} not found')
    except ValueError as exc:
        print(f"Invalid input: {exc}")
    except Exception as exc:
        print(f"Error updating department: {exc}")

def delete_department():
    try:
        id_ = int(input("Enter the department's id: "))
        if department := Department.find_by_id(id_):
            department.delete()
            print(f'Department {id_} deleted')
        else:
            print(f'Department {id_} not found')
    except ValueError:
        print("Invalid ID. Please enter a valid integer.")
