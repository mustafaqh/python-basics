from find_words import read_file, get_words, save_words

def main():
    #read text files
    import os
    path = "holy_grail.txt"
    rows= read_file(path)
    print(f"\nread {len(rows)}lines from file {path}")

    #collect words
    words=[]
    for row in rows:
        w=get_words(row)
        words += w

    #save words in file
    outpath=os.getcwd()+f"output_{len(words)}_wors.txt"
    save_words(outpath,words)
    print(f"saved{len(words)} words in file {outpath}")
    
main()
