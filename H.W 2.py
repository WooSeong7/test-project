subject = {'base_id':10000}
subject_list=[]
score_list={'A+':4.5, 'A':4, 'B+':3.5, 'B':3, 'C+':2.5, 'C':2, 'D+':1.5, 'D':1, 'F':0}
submit_credit=0
total_credit=0
submit_score=0
total_score=0
num_F=0

#함수
def get_code(subject_name):
    if subject_name not in subject:
        subject[subject_name] = subject['base_id']
        subject[subject[subject_name]] = subject_name
        subject['base_id']+=1
    return str(subject[subject_name])


#반복
while True:
    print("작업을 선택하세요.")
    print("   1.입력")
    print("   2.출력")
    print("   3.계산")
    selection = input()

    #입력
    if selection == '1':
        subject_name = input("과목명을 입력하세요:\n")
        credit = int(input("학점을 입력하세요:\n"))
        score = input("평점을 입력하세요:\n")
        print("입력되었습니다.\n")

        if subject_name in subject:
            for code, credit_, score_ in subject_list:
                if get_code(subject_name)==code:
                    if score_list[score_]>=score_list[score]:
                        continue
                    else:
                        subject_list.remove((code, credit_, score_))
                        if score_ =='F':
                            submit_credit+=credit
                            submit_score+=score_list[score]
                            num_F-=1
                        else:
                            submit_score-=score_list[score_]
                            total_score-=score_list[score_]

                            submit_score+=score_list[score]
                            total_score+=score_list[score]
                        subject_list.append((get_code(subject_name), credit, score))
            continue
        
        subject_list.append((get_code(subject_name), credit, score))

        total_credit+=credit
        total_score+=score_list[score]

        if score=='F':
            num_F+=1
            continue

        submit_credit+=credit
        submit_score+=score_list[score]

    #출력
    if selection == '2':
        for code, credit_, score_ in subject_list:
            print("["+subject[int(code)]+"]", str(credit_)+"학점:", score_)


    #계산
    if selection == '3':
        print("제출용:", str(submit_credit)+"학점 (GPA:", str(round(submit_score/(len(subject_list)-num_F),2))+")\n")
        print("열람용:", str(total_credit)+"학점 (GPA:", str(round(total_score/len(subject_list),2))+")\n")
        print("프로그램을 종료합니다.")
        break