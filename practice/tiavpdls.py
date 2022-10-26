import pickle 
who_file = open("who.pickle", "wb")
who = {"이름" : "알파고", "나이" : "6살", "취미" : ["축구", "베이킹", "콜라 마시기"]}
pickle.dump(who, who_file)
who_file.close()

who_file = open("who.pickle", "rb")
who = pickle.load(who_file)
print(who)
who_file.close()
