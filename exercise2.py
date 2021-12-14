def bigger_Is_greater(w: str) -> str:
    letters = list(w)
    i = j = len(letters) - 1

    while i > 0 and letters[i] <= letters[i - 1]:
        i -= 1

    if i <= 0:
        return "no answer"
    
    while letters[j] <= letters[i - 1]:
        j -= 1

    letters[j], letters[i - 1] = letters[i - 1], letters[j]
    letters[i:] = letters[len(letters) - 1:i - 1:-1]
    
    return "".join(letters)

