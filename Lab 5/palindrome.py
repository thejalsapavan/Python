#palindrome Recursion
def palindrome(l,n):
    if(n>=0):
        sr=l[n]
        st=""
        z=len(sr)
        
        for i in range(z):
            st=st+sr[z-i-1]
        
        if(st==sr):
            print(sr+" is a palindrome",)
        else:
             print(sr+" is not a palindrome ")
        palindrome( l,n-1)
