class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)% groupSize !=0:
            return False

        count=Counter(hand)
        for card in sorted(count):
            if count[card] > 0:
                freq = count[card]
                for i in range(groupSize):
                    count[card + i] -= freq
                    if count[card + i] < 0:
                        return False
        return True

        