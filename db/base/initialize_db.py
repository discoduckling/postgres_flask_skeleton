from schema import Department, Employee
from engine import session


engineering = Department(name="Engineering")
session.add(engineering)
session.commit()
sales = Department(name="Sales")
session.add(sales)
session.commit()

morgan = Employee(name="Morgan", department=sales)
alex = Employee(name="Alex", department=engineering)
mario = Employee(name="Mario", department=sales)
luigi = Employee(name="Luigi", department=engineering)
session.add(morgan)
session.add(alex)
session.add(luigi)
session.add(mario)
session.commit()

