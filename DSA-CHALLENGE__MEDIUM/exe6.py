def first_unique(text):
    for character in text:
        if text.count(character) == 1:
            return character

    return None