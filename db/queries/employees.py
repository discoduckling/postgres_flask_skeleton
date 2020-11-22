# import sys
# sys.path.append('..')

from sqlalchemy import select

from db.base.engine import connection
from db.base.schema import employees


def get_employees(employee_ids=None, department_ids=None):
    s = select([employees])
    if employee_ids:
        s = s.where(employees.c.id.in_(employee_ids))
    if department_ids:
        s = s.where(employees.c.department_id.in_(department_ids))

    rp = connection.execute(s)
    rows = rp.fetchall()
    return [{k: v for k, v in row.items()} for row in rows]


if __name__ == "__main__":
    print(get_employees())
    print(get_employees([1]))
    print(get_employees(None, [2]))
