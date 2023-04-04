credit1=0
credit2=0
grade=0
num1=0
num2=0

while True:
    print("작업을 선택하세요.")
    a=int(input("1. 입력\n2. 계산\n"))
    if a==1:
        b=int(input("학점을 입력하세요:\n"))
        credit1+=b
        credit2+=b
        num1+=1
        num2+=1
        c=input("평점을 입력하세요:\n")
        match c:
            case "A+":
                grade+=4.5
            case "A":
                grade+=4
            case "B+":
                grade+=3.5
            case "B":
                grade+=3
            case "C+":
                grade+=2.5
            case "C":
                grade+=2
            case "D+":
                grade+=1.5
            case "D":
                grade+=1
            case "F":
                credit1-=b
                num1-=1
        print("입력되었습니다.\n")

    elif a==2:
        print("제출용:", str(credit1)+"학점(GPA:"+str(round(grade/num1,2))+")\n")
        print("열람용:", str(credit2)+"학점(GPA:"+str(round(grade/num2,2))+")\n")
        print("프로그램을 종료합니다.\n")
        break