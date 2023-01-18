#문자열을 입력받아 중앙에 둔다 
#70문자열내에서 나머지 모든 부분을 *표시로 채운다(70문자열)

p = input()
width = 70
centered_string = p.center(width)
print(centered_string.replace(" ", "*"))
