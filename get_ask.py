import random

def get_ask(am):
    salt = '2021'
    random.seed(str(am).strip()+salt)

    groups = (
        (1,  10),
        (11, 20),
        (21, 30),
        (31, 40),
        (41, 50),
        (51, 60),
        (61, 70),
        (71, 80),
        (81, 90),
        (91, 100),
    )

    ret = [random.randint(g[0], g[1]+1) for g in groups]
    return ret

