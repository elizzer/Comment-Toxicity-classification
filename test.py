# text='hello!you are a stupid and idiot'
# span=[16,17,18,19,20,21,22,27,28,29,30,31,32]
# i=0
# t=list(text)

# for index in span:
#     if(t[index]==' ' and span[i+1]==index+1):
#         t.pop(index)
#         print(span.pop(i))
#         print(span)
#         for x in range(i,len(span)):
#             span[x]=span[x]-1
#         print(span)
            
#     i+=1
# print( ''.join(t))
# print(span)

text = 'hello!you are a stupid and idiot'
span = [16, 17, 18, 19, 20, 21, 22, 27, 28, 29, 30, 31, 32]
t = list(text)
new_text = []
new_span = []

i = 0
while i < len(span):
    if span[i] < len(t) and (i == len(span) - 1 or t[span[i]] != ' ' or span[i] != span[i + 1] - 1):
        new_text.append(t[span[i]])
        new_span.append(span[i])
    i += 1

print(''.join(new_text))
print(new_span)
