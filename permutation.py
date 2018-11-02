from itertools import permutations

def Permutate(w1,w2,w3,w4,w5,w6):

    words = [w1,w2,w3,w4,w5,w6]
    perms = []

    # generates a list
    for word in permutations(words):
        perms.append(" ".join(word))

    # converts to html_string
    html_string = "<ul>\n"
    for p in perms:
        html_string += str(p) + "<br>\n"
    html_string += "</ul>"

    return html_string
    #return perms
