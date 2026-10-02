class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict = {
            
        }

        newdict = {

        }

        for i in s:
            if i in mydict: 
                #scans through keys
                mydict[i]+=1
            else:
                mydict[i]=1

        for i in t:
            if i in newdict: 
                #scans through keys
                newdict[i]+=1
            else:
                newdict[i]=1

        if mydict == newdict:
            return True
        else:
            return False

        
        