# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that
# the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.


# Solution -

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        map = defaultdict(int)
        playersWonAtleast1Match = set()
        losersWith1Match = []
        playersWithZeroLose = []

        # Create mapping of loser -> no. of lose
        for winner, loser in matches:
            map[loser] += 1
            playersWonAtleast1Match.add(winner)

        # if count == 1 means player lost EXACTLY 1 match
        for loser in map:
            if map[loser] == 1:
                losersWith1Match.append(loser)
        
        # if player is not in map then there must be ZERO lose
        for winner in playersWonAtleast1Match:
            if map[winner] == 0:
                playersWithZeroLose.append(winner)
        return [sorted(playersWithZeroLose), sorted(losersWith1Match)]