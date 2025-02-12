# employee_management/app.py

from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "hello_laptop1234"  # Secret key for session management


# Define the Employee class
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary


# Simulated database for employees (using a dictionary)
employees = {}


# Route to display all employees
@app.route('/')
def index():
    return render_template('index.html', employees=employees.values())


# Route to add a new employee
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        name = request.form['name']
        department = request.form['department']
        salary = request.form['salary']

        if emp_id in employees:
            flash("Employee with this ID already exists!", "error")
        else:
            employees[emp_id] = Employee(emp_id, name, department, salary)
            flash("Employee added successfully!", "success")

        return redirect(url_for('index'))

    return render_template('add_employee.html')


# Route to update employee information
@app.route('/update/<emp_id>', methods=['GET', 'POST'])
def update_employee(emp_id):
    employee = employees.get(emp_id)

    if request.method == 'POST':
        employee.name = request.form['name']
        employee.department = request.form['department']
        employee.salary = request.form['salary']

        flash("Employee updated successfully!", "success")
        return redirect(url_for('index'))

    return render_template('update_employee.html', employee=employee)


# Route to delete an employee
@app.route('/delete/<emp_id>')
def delete_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        flash("Employee deleted successfully!", "success")
    else:
        flash("Employee not found!", "error")

    return redirect(url_for('index'))


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
