from math import *

def tournament(lst):
    while len(lst)>1:
        for i in range(len(lst)//2):
            print(lst)
            if(lst[i]>lst[i+1]):
                if checkKey(winnerDict,lst[i]):
                    winnerDict[lst[i]].append(lst[i+1])
                    
                else:
                    winnerDict[lst[i]]=[lst[i+1]]
                  
                del lst[i+1]
            else:
                if checkKey(winnerDict,lst[i+1]):
                    winnerDict[lst[i+1]].append(lst[i])
                   
                else:
                    winnerDict[lst[i+1]]=[lst[i]]
                  
                del lst[i]

            print(winnerDict)


def checkKey(dic,key):
    if key in dic.keys():
        return True
    return False

def findmax(dic):
    max_key=max(dic)
    values=dic[max_key]
    max_value=max(values)
    return max_value
    
    
lst=[21,1,3,15,4,29,7,17]
winnerDict={}
tournament(lst)
print("Second largest element:",findmax(winnerDict))
    
