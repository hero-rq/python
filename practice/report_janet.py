'''매주 1회 보고서 자동 형식 작성 프로그램 
- o 주차 주간 보고 - 
부서 : 
이름 : 파파고 
업무 요약 :   
1주차부터 7주차까지 '''


for i in range(1, 8):
  with open(str(i) + ".txt", "w", encoding="utf-8") as report_file:
    report_file.write("- {0} 주차 주간 보고 -\n".format(i))
    report_file.write("부서 : \n")
    report_file.write("이름 : 파파고 \n")
    report_file.write("업무 요약 :")
