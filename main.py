import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Tests,Test_Results,Students,Classes
from random import randint

classes = ['class' + chr(i) for i in range(65,75)]
students = ['student' + chr(i) for i in range(65,75)]
test_names = ['物理','英語','国語']
inserted_tests=[]
# テストテープルに科目を入れる
for test_name in test_names:
    test = Tests(
        name = test_name
    )
    test.save()
    inserted_tests.append(test)


# クラステープルにデータを入れる
for class_name in classes:
    insert_class = Classes(
        name = class_name
    )
    insert_class.save()
    
    # 学生テープルにデータを入れる
    for student_name in students:
        name = class_name + " " + student_name,
        student = Students(
            name = name,
            class_fk = insert_class,
            grade = 1,
            )
        student.save()
        # テストテープルにデータを入れる
        for inserted_test in inserted_tests:
            test_result = Test_Results(
                student = student,
                test = inserted_test,
                score = randint(50,100)
            )
            test_result.save()