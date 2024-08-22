from sqlalchemy import create_engine, text

db_connection_path = ("postgresql://x_clients_user:"
                      "95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@"
                      "dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/"
                      "x_clients_db_fxd0")


def test_db_connection():
    db = create_engine(db_connection_path)
    names = db.table_names()
    assert names[0] == 'app_users'


def test_select():
    db = create_engine(db_connection_path)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]

    assert row1['id'] == 3497
    assert row1['name'] == 'Эльдорадо'


def test_select_1_row():
    db = create_engine(db_connection_path)
    sql_statement = text("select * from company where id = :company_id")

    rows = db.execute(sql_statement, company_id=3497).fetchall()

    assert len(rows) == 1
    assert rows[0]['name'] == 'Эльдорадо'


def test_select_rows_with_filters():
    db = create_engine(db_connection_path)
    sql_statement = text(
        "select * from company where id > :company_id and is_active = :isActive"
        )

    rows = db.execute(sql_statement, company_id=3700, isActive=True).fetchall()

    assert len(rows) == 20
    assert rows[0]['name'] == 'Chairs&Co'


def test_select_rows_with_params():
    db = create_engine(db_connection_path)
    sql_statement = text(
        "select * from company where id > :company_id and is_active = :isActive"
        )

    my_params = {
        'company_id': 3700,
        'isActive': True
    }

    rows = db.execute(sql_statement, my_params).fetchall()

    assert len(rows) == 20
    assert rows[0]['name'] == 'Chairs&Co'


def test_insert():
    db = create_engine(db_connection_path)
    sql = text(
        'insert into company("name") values (:company_name)'
    )
    db.execute(sql, company_name='DeadLand')


def test_update():
    db = create_engine(db_connection_path)
    sql = text(
        "update company set description = :descr where id = :company_id"
    )
    db.execute(sql, descr='Eat me', company_id=3724)


def test_delete():
    db = create_engine(db_connection_path)
    sql = text(
        "delete from company where id = :company_id"
    )
    db.execute(sql, company_id=3724)
