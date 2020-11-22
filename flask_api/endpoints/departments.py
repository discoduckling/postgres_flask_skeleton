from flask import Blueprint, jsonify, request
from db.queries.departments import get_departments

departments = Blueprint("departments", __name__)


@departments.route("/", methods=("GET",))
def get():
    data = request.json
    department_ids = data.get("department_ids")
    include_employees=data.get("include_employees")
    return jsonify(get_departments(department_ids, include_employees))
