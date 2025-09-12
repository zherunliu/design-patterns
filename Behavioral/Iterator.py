from typing import List


# iterator
class Student:
    def __init__(self, name: str, id: str) -> None:
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


# iterator collection
class StudentCollection:
    def __init__(self) -> None:
        self.students: List[Student] = []

    def add_student(self, student: Student):
        self.students.append(student)

    def __iter__(self):
        # iter 返回迭代器，实现了 __iter__() 的类，其实例可以被迭代
        return iter(self.students)


"""
迭代器：实现 __iter__() 和 __next__()
可迭代对象：实现 __iter__()
__iter__(): 返回迭代器
__next__(): 返回迭代的下一个元素
"""

if __name__ == "__main__":
    n = int(input())
    student_collection = StudentCollection()

    for _ in range(n):
        stu_name, stu_id = input().split()
        student = Student(stu_name, stu_id)
        student_collection.add_student(student)

    for student in student_collection:
        print(student.get_name(), student.get_id())
