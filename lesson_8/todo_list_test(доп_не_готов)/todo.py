import requests

host = 'https://todo-app-sky.herokuapp.com/'


# проверить список
def check_todo_list():
    response = requests.get(
        url=host
    )
    return response.json()


# создать задание и получить его номер
def create_todo_task():
    task = {
        'title': 'automate API',
        'completed': False
    }
    requests.post(
        url=host,
        json=task
    )
    for i in range(0, len(check_todo_list())):
        if task['title'] == check_todo_list()[i]['title']:
            id = check_todo_list()[i]['id']
            return id


# обновение задачи
def update_todo_task(id):
    requests.patch(
        url=f'{host}{id}',
        json={
            'title': 'Automate API update'
        }
    )
    return id


# отметка задачи «Выполнена»
def mark_the_task_as_completed(id):
    task = {
        'completed': True
    }
    requests.patch(
        url=f'{host}{id}',
        json=task
    )


# удаление
def delete_task(id):
    requests.delete(
        url=f'{host}{id}'
    )


check_todo_list()  # просмотр списка
create_todo_task()  # создать задачу
update_todo_task(create_todo_task())  # обновить задачу
mark_the_task_as_completed(update_todo_task(create_todo_task()))  # поставить обновленную задачу как V
delete_task(2846)
