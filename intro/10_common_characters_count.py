# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32/solutions

def common_character_count(s1, s2):
    common = set(s1) & set(s2)
    return sum(min(s1.count(i), s2.count(i)) for i in common)
