grade_list={'A+':4.5, 'A':4, 'B+':3.5, 'B':3, 'C+':2.5, 'C':2, 'D+':1.5, 'D':1, 'F':0}

#클래스
class CourseHistory:
    def __init__(self):
        self.history = []
        self.course_id_map = {'id':10000}
    
    def allocate_course_id(self, course_name):
        if course_name not in self.course_id_map:
            self.course_id_map[course_name]=self.course_id_map['id']
            self.course_id_map[self.course_id_map[course_name]]=course_name
            self.course_id_map['id']+=1
        return str(self.course_id_map[course_name])
    
    def input_process(self):
        print("과목명, 학점, 평점을 입력하세요:")
        data = input()
        course_name, credit, grade = data.split(', ')
        credit = int(credit)
        if course_name in self.course_id_map:
            for code, credit_, grade_ in self.history:
                if course_name == self.course_id_map[int(code)]:
                    if grade_list[grade_]<grade_list[grade]:
                        self.history.remove((code, credit_, grade_))
                        self.history.append((self.allocate_course_id(course_name), credit, grade))   
        else:
            self.history.append((self.allocate_course_id(course_name), credit, grade))
        print("입력되었습니다.\n")
    
    def print_process(self):
        for code, credit, grade in self.history:
            print("["+self.course_id_map[int(code)]+"]", str(credit)+"학점:", grade)
        print("\n")

    def query_process(self):
        search_course=input("과목명을 입력하세요:\n")
        for code, credit, grade in self.history:
            if search_course == self.course_id_map[int(code)]:
                print("["+search_course+"]", str(credit)+"학점:", grade+"\n")
        if search_course not in self.course_id_map:
            print("해당하는 과목이 없습니다.\n")

    def calculate_process(self):
        submit_credit=0
        archive_credit=0
        submit_grade = 0
        archive_grade= 0
        num_F=0
        for code, credit, grade in self.history:
            archive_credit += credit
            archive_grade += grade_list[grade]
            num_F+=1
            if grade !='F':
                num_F-=1
                submit_credit += credit
                submit_grade += grade_list[grade]
        print("제출용:", str(submit_credit)+"학점 (GPA:", str(round(submit_grade/(len(self.history)-num_F),2))+")")
        print("열람용:", str(archive_credit)+"학점 (GPA:", str(round(archive_grade/len(self.history),2))+")\n")

a = CourseHistory()

#반복
while True:
    print("작업을 선택하세요.")
    print("   1.입력")
    print("   2.출력")
    print("   3.조회")
    print("   4.계산")
    print("   5.종료")
    selection = input()

    #입력
    if selection=='1':
        a.input_process()
    
    elif selection=='2':
        a.print_process()

    elif selection=='3':
        a.query_process()

    elif selection=='4':
        a.calculate_process()

    elif selection=='5':
        print("프로그램을 종료합니다.\n")
        break