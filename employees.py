import sqlite3

class EmployeeApplication:
    def __init__(self):
        self.conn = sqlite3.connect('employees.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                phone TEXT,
                                email TEXT,
                                salary REAL
                            )''')
        self.conn.commit()

    def add_employee(self, name, phone, email, salary):
        self.cursor.execute("INSERT INTO employees (name, phone, email, salary) VALUES (?, ?, ?, ?)", (name, phone, email, salary))
        self.conn.commit()

    def update_employee(self, id, name, phone, email, salary):
        self.cursor.execute("UPDATE employees SET name=?, phone=?, email=?, salary=? WHERE id=?", (name, phone, email, salary, id))
        self.conn.commit()

    def delete_employee(self, id):
        self.cursor.execute("DELETE FROM employees WHERE id=?", (id,))
        self.conn.commit()

    def search_employee(self, name):
        self.cursor.execute("SELECT * FROM employees WHERE name=?", (name,))
        result = self.cursor.fetchall()
        return result

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    app = EmployeeApplication()
    app.add_employee("Иванов Иван", "1234567890", "ivanov@example.com", 50000)
    app.update_employee(1, "Петров Пётр", "9876543210", "petrov@example.com", 600000)
    app.delete_employee(1)
    search_result = app.search_employee("Петров Пётр")
    print(search_result)
    app.close_connection()
