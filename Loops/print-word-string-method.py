String=input()

start_index=2
step_index=3
word=""

for i in range(start_index,len(String),step_index):
    word=word+String[i]
print(word)