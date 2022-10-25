#사이트를 입력할 때 특정 비밀번호로 전환하는 프로그램을 작성하세요

#프로그램 처리 
#1) http://부분은 제외 
#2) 처음으로 . 이 등장하는 이후 부분은 제외 
#3) 남은 글자 중 처음 세 자리 + 남은 글자 갯수 + 글자 내 'a' 갯수 + * 

s = input().split('//')
s = s[1].split('.')
k = list(s[0])
t = len(k)
main = str(k[0]) + str(k[1]) + str(k[2]) + str(t) + str(k.count("a")) + '*'
print(main)
