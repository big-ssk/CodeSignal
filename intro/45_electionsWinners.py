def electionsWinners(votes, k):
    res = 0
    curr_max = max(votes)
    rv = votes.count(curr_max)
    
    if not k and rv == 1:
        return 1

    for i in votes:
        if i + k > curr_max:
            res += 1

    return res

