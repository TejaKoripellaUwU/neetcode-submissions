class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        d = {}
        for i in hand:
            d[i] = d.get(i, 0) + 1
            
        while d:
            first = next(iter(d))
            
            for i in range(groupSize):
                card = first + i
                
                if card not in d:
                    return False
                
                d[card] -= 1
                
                if d[card] == 0:
                    del d[card]
                    
        return True
