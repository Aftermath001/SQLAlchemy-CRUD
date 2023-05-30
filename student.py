from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



Base = declarative_base()

class Student(Base):
    # Creating a table
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

     # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()

# INserting data into table
    Student1 = Student(name="Albert Einstein",age = 24,grade= 10)

    Student2 = Student(name="Alvin Adams",age = 21,grade= 8)

    Student3 = Student(name="Ephy Orina",age = 18,grade= 7)

    Student4 = Student(name="Joy Waka",age = 16,grade= 6)

    Student5 = Student(name="George Ingabo",age = 12,grade= 5)

    # session.add(Student1)

    session.add_all ([Student1, Student2, Student3, Student4, Student5 ])

# Commiting to the database
    session.commit()

# Get all data for table
    students = session.query(Student)
# Loop through the data
    for student in students:
        print (student.name,student.age,student.grade)


# # Getting data of students in order of student name
#     students = session.query (Student).order_by(Student.name)
#     for student in students:
#         print(student.name)


# Update Data in table
# Select the record to be changed
    student = session.query(Student).filter(Student.name == "Albert Einstein").first()

# change the record
    student.name = "Kim Bonnke"
# Commit to the database
    session.commit()
    # print(student.name)


# Delete data from the table
    # student = session.query(Student).filter(Student.name == "Albert Einstein").first()
    # session.delete(student)
    # session.commit()
