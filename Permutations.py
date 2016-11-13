def permutations(letters):
    P = []
    if len(letters) <= 1:
        return [letters]
    elif len(letters) == 2:
        return [letters] + [letters[1] + letters[0]]
    else:
        for i in range(len(letters)):
            P += map(lambda s: letters[i] + s,
                       permutations(letters[:i] + letters[i + 1:]))
    return P

def word(letters):
    f = file('words.txt')
    words = f.readlines()
    f.close()
    
    perms = permutations(letters)
    for word in perms:
        if word + '\r' + '\n' in words:
            print word