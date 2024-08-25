from sqlalchemy import create_engine, text


class DbTable():

    def __init__(self, db_connection_path) -> None:
        self.db = create_engine(db_connection_path)

    def get_all_companies(self):
        return self.db.execute(
            "select * from company where deleted_at is null"
            ).fetchall()

    def get_max_company_id(self):
        return self.db.execute('select max(id) from company').fetchall()

    def delete_company(self, cp_id):
        sql = text('delete from company where id= :company_id')
        self.db.execute(sql, company_id=cp_id)

    def select_all_emloyee(self):
        self.db.execute('select * from employee').fetchall()

    def delete_employee(self, emp_id):
        sql = text('delete from employee where id= :employee_id')
        self.db.execute(sql, employee_id=emp_id)

    def get_employee_info_max_id(self):
        return self.db.execute(
            'select * from employee order by id desc limit 1'
            ).fetchall()

    def get_employee_info_by_id(self, emp_id):
        sql = text('select * from employee where id= :id')
        return self.db.execute(sql, id=emp_id).fetchall()

    def update_employee_data_by_id(self, emp_id, emp_lname, emp_email):
        sql = text('update employee set last_name = :new_lname, email = :email where id= :employee_id')
        self.db.execute(sql, employee_id=emp_id, new_lname=emp_lname, email=emp_email)
