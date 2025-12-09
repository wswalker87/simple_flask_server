from flask import Flask, jsonify

# We create a Flask application by initializing the `app` object.
app = Flask(__name__)

# Sample student data
students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

if __name__ == '__main__':
    app.run(debug=False, port=5000) 

# We define a route `/students` that responds to GET requests.
@app.route('/')
def get_students():
    return jsonify(students)

# /old_students/ :Returns an array of student objects where the students are older than 20 years old.
@app.route('/old_students/', methods=['GET'])
def get_old_students():
    older_students = []
    for student in students:
        if student['age'] >= 20:
            older_students.append(student)
    return jsonify(older_students)
    # return older_students

# print(get_old_students(students))

# /young_students/: Returns an array of student objects where the students are younger than 21 years old.
@app.route('/young_students/')
def get_young_students():
    younger_students = []
    for student in students:
        if student['age'] <= 21:
            younger_students.append(student)
    
    return jsonify(younger_students)

# /advance_students/: Returns an array of student objects where the students are younger than 21 and have a letter grade of "A."
@app.route('/advance_students/')
def get_advance_students():
    advanced_students = []
    for student in students:
        if student['age'] <= 21 and student['grade'] == 'A':
            advanced_students.append(student)
            # print(advanced_students)
    return jsonify(advanced_students)

# print(get_advance_students())

# /student_names/: Returns an array of student objects holding only the keys of 'first_name' and 'last_name' along with their corresponding values.
@app.route('/student_names/')
def get_student_names():
    student_names = []
    for student in students:
        name_dict = {
            'first_name': student[ 'first_name'],
            'last_name': student['last_name']
        }
        student_names.append(name_dict)
    return jsonify(student_names)
# print(get_student_names(students))

# /student_ages/: Returns an array of student objects holding the keys 'student_name' with the value of first and last name, and 'age' with the value of that student's age.
@app.route('/student_ages/')
def get_student_ages():
    student_ages = []
    for student in students:
        name_dict = {
            'first_name': student['first_name'],
            'last_name': student['last_name'], 
            'age': student['age']
        }
        student_ages.append(name_dict)
    # return student_ages
    return jsonify(student_ages)
