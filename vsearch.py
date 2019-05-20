def searchforvowels(phrase):
    return set('aeiou').intersection(set(phrase))

def searchforletters(phrase,letters):
    return  set(letters).intersection(set(phrase))