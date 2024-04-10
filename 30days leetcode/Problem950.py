class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()

        n = len(deck)
        output = [0]*n
        ind = deque(range(n))

        for card in deck:
            i = ind.popleft()
            output[i] = card
            if ind:
                ind.append(ind.popleft())

        return output