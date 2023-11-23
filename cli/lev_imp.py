from functools import cache


@cache
def lev_cond(s1: str, s2: str):
    """basic levenstain implementation

    :s1: first word
    :s2: second word
    :return int: number of actions to turn first word into second word
    """
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    elif s1[-1] == s2[-1]:
        return lev_cond(s1[:-1], s2[:-1])
    return 1 + min(
        lev_cond(s1[:-1], s2),
        lev_cond(s1, s2[:-1]),
        lev_cond(s1[:-1], s2[:-1]),
    )


OTBET = lev_cond(input("First word: "), input("Second word: "))
print(f"There {OTBET} actions between this words")
