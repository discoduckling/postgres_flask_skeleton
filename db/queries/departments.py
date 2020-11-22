from sqlalchemy.sql import select

from db.base.schema import departments, employees
from db.base.engine import connection


def get_employees_by_department(department_ids):
    """Appends employee info to departments query"""
    s = select([employees]).where(employees.c.department_id.in_(department_ids))
    rp = connection.execute(s)
    rows = rp.fetchall()
    employees_grouped_by_department = {id: [] for id in department_ids}
    for row in rows:
        items = row.items()
        department = row["department_id"]
        employees_grouped_by_department[department].append({
           k: v for k,v in items if k is not "department_id"
        })
    return employees_grouped_by_department


def get_all_departments():
    """Returns all departments"""
    s = select([departments])
    rp = connection.execute(s)
    rows = rp.fetchall()
    return [{k: v for k, v in row.items()} for row in rows]


def get_departments(department_ids=None, include_employees=False):
    """Returns specific departments
    Args:
        department_ids (list): integer ids of select departments
        include_employees (bool): True to include employee info for department

    Returns:
        list of departments
    """
    s = select([departments])
    if department_ids is not None:
        s = s.where(departments.c.id.in_(department_ids))

    rp = connection.execute(s)
    rows = rp.fetchall()

    if include_employees:
        if department_ids is not None:
            employee_info = get_employees_by_department(department_ids=department_ids)
        else:
            all_department_ids = set(r["id"] for r in rows)
            employee_info = get_employees_by_department(department_ids=all_department_ids)
        result = []
        for row in rows:
            row_item = {k: v for k, v in row.items()}
            row_item["employees"] = employee_info[row["id"]]
            result.append(row_item)
        return result

    return [{k: v for k, v in row.items()} for row in rows]


if __name__ == "__main__":
    print(get_departments(department_ids=None, include_employees=True))
    print(get_departments([1], True))
