import sys

def uppercase_keywords(text):

    global f

    # Get keywords
    keywords = open('keywords.txt').read()

    # Create array
    keywords = keywords.split(',')

    # If keyword found, uppercase
    for word in keywords:
        if word in f:   
            f = f.replace(word, word.upper())

    return f
           
if __name__ == '__main__':
    filen = sys.argv[1]
    f = open(filen).read()
    nf = uppercase_keywords(f)
    fh = open(filen+".uppercase","w")
    fh.write(nf)
    fh.close()
