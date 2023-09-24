#Longest Word
def longest_word(f):
    file=open(f,'r')
    s=file.read()
    x=s.split(" ")
    x.sort(key=len,reverse=True)
    print("Longest word is :",x[0])
    print("Length is :",len(x[0]))

n=input("Enter the file name with extension : ")
longest_word(n)

