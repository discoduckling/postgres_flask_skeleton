from flask import Flask

from flask_api.endpoints.departments import departments
from flask_api.endpoints.employees import employees

app = Flask(__name__)
app.register_blueprint(departments, url_prefix='/departments')
app.register_blueprint(employees, url_prefix='/employees')

if __name__ == "__main__":
    app.run(debug=True)
