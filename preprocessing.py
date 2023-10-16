#remove urls and combine repeated special characters
import re
import pandas as pd

input_csv_file = 'dataset.csv'  
# df = pd.read_csv(input_csv_file)

def remove_urls(text):
    return re.sub(r'http\S+', '', text)

def combine_repeated_chars(text):
    return re.sub(r'([!@#$%^&*()_+=\-{}[\]:;"\'|<>,./?\\])\1+', r'\1', text)

# df['comment_text'] = df['comment_text'].apply(lambda x: combine_repeated_chars(remove_urls(x)))

def filter_singleton(text,span):
    span=span[1:-1]
    span=span.split(",")
    for i in span:
        if " " in i:
            print("[+]This span has space:",i,":",i.strip(" "),":")
    # span=[integer(s) for s in span]
    # print(span)
    # for i in span:
        # print(type(int(i.strip())))
        # if(text[i]==' '):
        #     print('[+] singleton example'+text)
    # print(text,span)

#remove leading whitespace 
def r_whitespace(text,span):
    i=0
    t=list(text)

    for index in span:
        if(t[index]==' '):
            list.pop(index) 
            span.pop(i)
            for x in range(i,len(span)):
                span[x]=span[x]-1
    i+=1


def run():
    df = pd.read_csv(input_csv_file)
    # for i in range(d["comment_text"]):
    for i in range(100):
        # filter_singleton(df["comment_text"][i],df["span"][i])
        r_whitespace(df["comment_text"][i],df["span"][i])

# run()
# Python3 code to remove whitespace
def remove(string):
	return "".join(string.split())


# Driver Program
string = '   Hello   '
print(string)
print(":",string.strip(),":")


# df[['comment_text', 'span']] = df.apply(lambda row: r_whitespace(row['comment_text'], row['span']), axis=1)



# output_csv_file = 'processed_dataset.csv'  
# df.to_csv(output_csv_file, index=False)
# print(df.head(10))


