from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


# TODO Define the data-models
# Create models (e.g. classes) for all of your tables.
# Start with creating the Student and StudentNickName Models
# Later, you can add the Course and StudentCourses Models 

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/create_all')
def create_all():
    # TODO create the db
    message = "DB Created! (A SQLite DB File Should Appear In Your Project Folder.  " \
              "Also, if changes are made to the model, running this again should " \
              "add these changes to the db."
    return render_template('index.html', message=message)

@app.route('/drop_all')
def drop_all():
    # TODO drop the db
    message = "DB Dropped!!"
    return render_template('index.html', message=message)

@app.route('/add_students')
def add_students():
    # TODO add two students to the DB with the following attributes:
    # name='Joe',email="joe@weber.edu",age=21
    # name='Mary', email="mary@weber.edu", age=22 | Mary's nickname: Maria

    message = "Student named Joe and Mary added to DB.  Mary's nickname also added"
    return render_template('index.html', message=message)

@app.route('/add_nicknames_to_student')
def add_nicknames_to_student():
    # TODO associate the nicknames Jojo and Joey to Joe 
    message = "Two nicknames (Joe and Joey) added to Joe"
    return render_template('index.html', message=message)

@app.route('/update_student')
def update_student():
    # TODO: change Joe's name to Joseph
    message = "Student Joe Updated"
    return render_template('index.html', message=message)


@app.route('/select_student')
def select_student():
    # TODO: Retrieve the student with the email "joe@weber.edu" and display his name, email and nicknames 
    message = "Query Results:<br> " 
    return render_template('index.html', message=message)

@app.route('/select_students')
def select_students():
    # TODO: Retrieve all the students and display their names, nicknames (and later their enrollments) 

    message = "Query Results: <br>" 
    return render_template('index.html', message=message)

@app.route('/delete_student')
def delete_student():
    # TODO: Delete Joe and his associated info from the DB
    message = "Joe deleted from DB"
    return render_template('index.html', message=message)

@app.route('/add_courses')
def add_courses():
    # TODO: Add a course named Anthro 1000 and another named English 1100 to the DB
    db.session.commit()
    message = "Two courses added to DB"
    return render_template('index.html', message=message)

@app.route('/enroll_students')
def enroll_students():
    # TODO: Enroll Joe in Anthro and English.  Enroll Mary in Anthro.

    message = "Joe Enrolled in Anthro and English.  Mary enrolled in Anthro"
    return render_template('index.html', message=message)


@app.route('/show_course_enrollments')
def show_course_enrollments():
    # TODO: Show the enrollments for Anthro and English

    message = "Course Enrollments:<br>" + str(anthro) + "<br>" + str(english)
    return render_template('index.html', message=message)

@app.route('/show_student_enrollments')
def show_student_enrollments():
    # TODO: Show Joe's enrollments
    message = "Joe is enrolled in:<br> " 
    return render_template('index.html', message=message)
