#remove urls and combine repeated special characters
import re
import pandas as pd

input_csv_file = 'dataset.csv'  
df = pd.read_csv(input_csv_file)

def remove_urls(text):
    return re.sub(r'http\S+', '', text)

def combine_repeated_chars(text):
    return re.sub(r'([!@#$%^&*()_+=\-{}[\]:;"\'|<>,./?\\])\1+', r'\1', text)

df['comment_text'] = df['comment_text'].apply(lambda x: combine_repeated_chars(remove_urls(x)))


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
    i++





df[['comment_text', 'span']] = df.apply(lambda row: r_whitespace(row['comment_text'], row['span']), axis=1)



# output_csv_file = 'processed_dataset.csv'  
# df.to_csv(output_csv_file, index=False)
print(df.head(10))


