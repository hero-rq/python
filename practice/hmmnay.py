'''다음과 같이 점수 계산을 하기로 하였다. 1번 문제가 맞는 경우에는 1점으로 계산한다. 앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점으로 계산한다. 또한, 연속으로 문제의 답이 맞는 경우에서 두 번째 문제는 2점, 세 번째 문제는 3점, ..., K번째 문제는 K점으로 계산한다. 틀린 문제는 0점으로 계산한다.

입력 : 첫 줄 n회 
n회 만큼 1/0으로 정답/오답 여부 입력
사실 이 문제의 포인트는 중복되는 만큼 어떻게 누적해서 점수를 줄 것인가 어떻게 그것을 판별할 수 있는가이다
s=0으로 만들어두고 1을 만날 때 s=1, 0을 만날 때 s=0으로 다시 되돌아간다 
1을 만날 때마다 s는 누적해서 점수로 상승하며 이걸 그대로 값에 추가한다(추가하는 것만 다른 변수이면 될 듯)

n = int(input())
k_list = [int(x) for x in input().split()]

#print(k_list)
s = 0
k = 0
for i in range(0, len(k_list)):
  if k_list[i] == 1:
    s += 1
    k += s
  elif k_list[i] == 0:
    s = 0
    k += s

print(k)'''

n = int(input())
k_list = [int(x) for x in input().split()]
s = 0
score = 0

for i in range(n):
    if k_list[i] == 1:
        s += 1
        score += s
    elif k_list[i] == 0:
        s = 0

print(score)
