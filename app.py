from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


# Below are the models (e.g. classes) for all of your tables.

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    # Define the relationship to Student via StudentCourses
    students = db.relationship('Student', secondary='student_courses')

    def __str__(self):
        students = "["
        for stud in self.students:
            students = students + stud.name + ','
        students = students + "]"
        string_object = str(self.id) + "|" + str(self.name) +"|" + students
        return string_object

class StudentCourses(db.Model):
    __tablename__ = 'student_courses'
    id = db.Column(db.Integer(), primary_key=True)
    course_id = db.Column(db.Integer(), db.ForeignKey('courses.id', ondelete='CASCADE'))
    student_id = db.Column(db.Integer(), db.ForeignKey('student.id', ondelete='CASCADE'))

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    age = db.Column(db.Integer())
    student_nick_names = db.relationship("StudentNickName", backref='student', cascade='all')

    # Define the relationship to Course via StudentCourses
    courses = db.relationship('Course', secondary='student_courses')

    def __str__(self):
        nick_names = "["
        for nick in self.student_nick_names:
            nick_names = nick_names + nick.nick_name + ','
        nick_names = nick_names + "]"
        courses = "["
        for course in self.courses:
            courses = courses + course.name + ','
        courses = courses + "]"
        string_object = str(self.id) + "|" + str(self.name) +"|" + str(self.email) + "|" + str(self.age) + "|" + nick_names + "|" + courses
        return string_object

class StudentNickName(db.Model):
    __tablename__ = 'student_nick_name'
    id = db.Column(db.Integer(), primary_key=True)
    nick_name = db.Column(db.String(50), unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'))

    def __str__(self):
        string_object = nick_name
        return string_object

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/create_all')
def create_all():
    db.create_all()
    # TODO create the db
    message = "DB Created! (A SQLite DB File Should Appear In Your Project Folder.  " \
              "Also, if changes are made to the model, running this again should " \
              "add these changes to the db."
    return render_template('index.html', message=message)

@app.route('/drop_all')
def drop_all():
    db.drop_all()
    # TODO drop the db
    message = "DB Dropped!!"
    return render_template('index.html', message=message)

@app.route('/add_students')
def add_students():
    joe = Student(name='Joe',email='joe@weber.edu',age=21)
    db.session.add(joe)
    db.session.commit()

    mary = Student(name='Mary',email='mary@weber.edu', age=22)
    nickname_1 = StudentNickName(nick_name='Maria')
    mary.student_nick_names.append(nickname_1)
    db.session.add(mary)
    db.session.commit()

    # TODO add two students to the DB with the following attributes:
    # name='Joe',email="joe@weber.edu",age=21
    # name='Mary', email="mary@weber.edu", age=22 | Mary's nickname: Maria

    message = "Student named Joe and Mary added to DB.  Mary's nickname also added"
    return render_template('index.html', message=message)

@app.route('/add_nicknames_to_student')
def add_nicknames_to_student():
    joe = Student.query.filter(Student.email == 'joe@weber.edu').first()
    print(joe.name)
    jojo = StudentNickName(nick_name='Jojo')
    joey = StudentNickName(nick_name='Joey')
    joe.student_nick_names.append(jojo)
    joe.student_nick_names.append(joey)
    db.session.add(joe)
    db.session.commit()

    # TODO associate the nicknames Jojo and Joey to Joe 
    message = "Two nicknames (Jojo and Joey) added to Joe"
    return render_template('index.html', message=message)

@app.route('/update_student')
def update_student():
    joe = Student.query.filter(Student.email == 'joe@weber.edu').first()
    joe.name = 'Joseph'
    db.session.add(joe)
    db.session.commit()  
    # TODO: change Joe's name to Joseph
    message = "Student Joe Updated"
    return render_template('index.html', message=message)


@app.route('/select_student')
def select_student():
    joe = Student.query.filter(Student.email == 'joe@weber.edu').first()

    
    # TODO: Retrieve the student with the email "joe@weber.edu" and display his name, email and nicknames 
    message = f"Query Results:<br> {joe} "
    return render_template('index.html', message=message)

@app.route('/select_students')
def select_students():
    students = Student.query.all()
    students = Student.query.order_by(Student.email.desc())
    query_results = ''
    for x in students:
        query_results = query_results + str(x) + "<br>"

    # TODO: Retrieve all the students and display their names, nicknames (and later their enrollments) 

    message = "Query Results: <br>" + query_results 
    return render_template('index.html', message=message)

@app.route('/delete_student')
def delete_student():
    joe = Student.query.filter(Student.email == 'joe@weber.edu').first()
    db.session.delete(joe)
    db.session.commit()
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
