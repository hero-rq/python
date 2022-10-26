scores = {"수학" : 100, "경제" : 95, "쿠키" : 85}
for subject, score in scores.items():
  print(subject.ljust(5), str(score).rjust(4), sep=":")
