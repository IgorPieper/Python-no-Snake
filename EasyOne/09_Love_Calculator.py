def calculate_love_score(x, y):
    x = x.lower()
    y = y.lower()

    alphabet = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
        "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
        "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
        "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
        "y": 0, "z": 0
    }

    alphabet1 = alphabet.copy()
    alphabet2 = alphabet.copy()

    true = {"t": 0, "r": 0, "u": 0, "e": 0}
    love = {"l": 0, "o": 0, "v": 0, "e": 0}

    for xx in x:
        if xx in alphabet1:
            alphabet1[xx] += 1

    for yy in y:
        if yy in alphabet2:
            alphabet2[yy] += 1

    merged = {k: alphabet1[k] + alphabet2[k] for k in alphabet1}

    true = {k: merged[k] for k in true}
    love = {k: merged[k] for k in love}

    sum_true = sum(true.values())
    sum_love = sum(love.values())

    result = str(sum_true) + str(sum_love)
    return result

print(calculate_love_score("Kanye West", "Kim Kardashian"))
