from collections import deque 

def check(card,word):
    if len(card)>0:
        if card[0]==word:
            return True
    return False

def solution(cards1, cards2, goal):
    
    queue=deque()
    
    answer = ''
    for w in goal:
        if check(cards1,w):
            queue.append(cards1[0])
            cards1.remove(cards1[0])
            # print(cards1)
        elif check(cards2,w):
            queue.append(cards2[0])
            cards2.remove(cards2[0])
            # print(cards2)
        
        else:
            return "No"
        # print(queue)
    return "Yes"



c1=["i", "drink","water" ]
c2=["want", "to"]
g=["i", "want", "to", "drink", "water"]

print(solution(c1,c2,g))