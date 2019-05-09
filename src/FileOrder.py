

def equals(a, b):
    resultA = ''.join(c for c in a if (c.isalpha()))
    resultB = ''.join(c for c in b if c.isalpha())
    if resultA.lower().strip() == resultB.lower().strip():
        return True
    else:
        return False

def lean(a):
    resultA = ''.join(c for c in a if c.isalpha() or " " or "(" or ")")
    return resultA

def order():
    #PLEASE ADD THE FILE YOU WANT TO USE AND REPLACE IT WITH "theMovies.txt" HERE BY HAND
    movieList = open("theMovies.txt", "r+", encoding="utf-8")
    newList = open("aa.txt", "w", encoding="utf-8")

    x = movieList.readlines()

    for i in range(len(x)):
        x[i] = x[i].strip()

    for t in range(len(x)):
        movie = x[t]
        #  if the item was dublicated it deletes the replication
        addable = True
        for peek in range(t + 1, len(x)):
            index = x[peek]
            if equals(index, movie):
                addable = False
        if addable:
            newList.write(movie + "\n")

    movieList.close()
    newList.close()

def get_aa():
    order()
    theList = open("aa.txt", "r", encoding="utf-8")
    list = []
    x = theList.readlines()
    for i in range(len(x)):
        x[i] = x[i].strip()

    for movie in x:
        list.append(lean(movie))
        print(lean(movie))
    return list

