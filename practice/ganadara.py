#주어진 이름은 가나다 순서로 배정하고 번호를 매겨서 출력 
import locale

student = ['강판다', '파파박사', '박쿠키', '최락훈', '최명호', '박지호', '권윤일', '한지호', '퍈다']

sorted_list = sorted(student, key=locale.strxfrm)

korean_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

for index, value in enumerate(sorted_list):
    print(f"{korean_numbers[index]}번: {value}")

'''
student = ['강판다', '파파박사', '박쿠키', '최락훈', '최명호', '박지호', '권윤일', '한지호', '퍈다']

sorted_list = sorted(student, key=locale.strxfrm)


sorted(student)
print(student)
my_list = ["apple", "banana", "cherry"]

korean_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

for index, value in enumerate(sorted_list, start=1):
    print(f"{korean_numbers[index-1]}번: {value}")

'''   
