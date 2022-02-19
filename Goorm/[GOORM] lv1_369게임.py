N = int(input())
num_str = ''
for i in range(1, N):
	num_str += str(i)

answer_list = filter(lambda x: x=="3" or x=="6" or x=="9", num_str)
print(len(list(answer_list)))