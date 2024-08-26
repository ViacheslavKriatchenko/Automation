from sqlalchemy import create_engine, text
import allure


class DbTable():

    def __init__(self, db_connection_path) -> None:
        self.db = create_engine(db_connection_path)

    @allure.step('DB. Получить список всех компаний')
    def get_all_companies(self) -> list:
        query = self.db.execute(
            "select * from company where deleted_at is null"
            )
        allure.attach(str(query.context.cursor.query), 'SQL-запрос', allure.attachment_type.TEXT)
        return query.fetchall()

    @allure.step('DB. Получить компанию с максимальным id')
    def get_max_company_id(self) -> list:
        return self.db.execute('select max(id) from company').fetchall()

    @allure.step('DB. Удалить компанию с id = {cp_id}')
    def delete_company(self, cp_id: int):
        sql = text('delete from company where id= :company_id')
        self.db.execute(sql, company_id=cp_id)

    @allure.step('DB. Получить список всех работников')
    def select_all_emloyee(self) -> list:
        self.db.execute('select * from employee').fetchall()

    @allure.step('DB. Удалить работника с id = {emp_id}')
    def delete_employee(self, emp_id: int):
        sql = text('delete from employee where id= :employee_id')
        self.db.execute(sql, employee_id=emp_id)

    @allure.step('DB. Получить запись в сотруднике с макс id')
    def get_employee_info_max_id(self) -> list:
        return self.db.execute(
            'select * from employee order by id desc limit 1'
            ).fetchall()

    @allure.step('DB. Получить запись в сотруднике с id = {emp_id}')
    def get_employee_info_by_id(self, emp_id: int) -> list:
        sql = text('select * from employee where id= :id')
        return self.db.execute(sql, id=emp_id).fetchall()

    @allure.step('DB. Обновить данные сотрудника с id = {emp_id}')
    def update_employee_data_by_id(
            self, emp_id: int, emp_lname: str, emp_email: str
            ) -> list:
        sql = text(
            'update employee set last_name = :new_lname, email = :email where id= :employee_id'
            )
        self.db.execute(
            sql, employee_id=emp_id, new_lname=emp_lname, email=emp_email
            )
