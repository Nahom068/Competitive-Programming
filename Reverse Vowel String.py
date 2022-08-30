class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ['a', 'e','i','o','u','A', 'E', 'I', 'O', 'U']
        i=0
        j=len(s)-1
        s = list(s)
        while i<j and j>0:
               if s[i] in vow and s[j] in vow:
                    s[i],s[j]=s[j],s[i]
                    i+=1
                    j-=1
                
               elif s[j] not in vow:
                    j-=1
             
               elif s[i] not in vow:
                    i+=1
            
        return ''.join(s)
