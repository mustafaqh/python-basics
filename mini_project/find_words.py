import io 
def read_file(file_path):
    rows=[]
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line=line.strip()
            rows.append(line)
        return rows



def get_words(row):   
    a=row.lower()
    word_l=[] 
    p='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for c in a:
        if c in p:
            a=a.replace(c,' ')
            sp=a.split()
            for ele in sp:
        
                if not ele.isdigit():
                    word_l.append(ele)

    for ele in word_l:  
        if len(ele) ==1 and ele!="i" or ele!="a":
            word_l.remove(ele)
    return word_l


def save_words(outpath, words):
  
    with open(outpath, 'w', encoding = 'UTF-8') as f:
        for i in words:
            f.write(i)



    


        
