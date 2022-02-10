from application import app, db
from application.models import Todo

@app.route('/add/<task>')
def add():
    new_task = Todo(task="New test task")
    db.session.add(new_task)
    db.session.commit()
    return "Added new test task to the database"

# @app.route('/update/<task>')
# def update(task):
#     first_task = Todo.query.first()
#     first_task.task = task
#     db.session.commit()

#     return (f"Your task : {first_task.task}. is added to the database")

# @app.route('/')
@app.route('/view')
def read():
    all_tasks = Todo.query.all()
    tasks_string = ""
    for i in all_tasks:
        tasks_string += "<br>"+ i.task
    return tasks_string

@app.route('/delete')
def delete():
    first_task = Todo.query.first()
    db.session.delete(first_task)
    db.session.commit()
    return "You have deleted the first Task on the"
