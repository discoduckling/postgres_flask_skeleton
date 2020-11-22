from flask import Blueprint, request, jsonify
from db.queries.employees import get_employees

employees = Blueprint("employees", __name__)


@employees.route("/")
def get():
    data = request.json
    employee_ids = data.get("employee_ids")
    department_ids = data.get("department_ids")
    return jsonify(get_employees(employee_ids, department_ids))


