#preview
subjects = "python c++ database linux"
subject = input("수강신청과목 입력: ")

try:
    print(f"해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다")
except ValueError:
    print(f'해당 과목이 존재하지않습니다.')


