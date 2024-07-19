#단어 정렬
import sys
output =''
n = int(sys.stdin.readline())
word = []
for i in range(n):
    words = sys.stdin.readline()
    if words not in word:
        word.append(words)
set_lst = list(set(word))
sort_list = []
for i in set_lst:
    sort_list.append(len(i),i)
result = sorted(sort_list)
for len_word,word  in result:
    print(word)





        
