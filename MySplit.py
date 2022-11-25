# it should accept exactly one argument - a string;
# it should return a list of words created from the string, divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;
# its name should be mysplit()

def mysplit(a):
    a = list(a)
    i = 0
    w = 0
    z = []
    while i+1 < len(a):
        if (a[len(a)-1]).isalnum() == (a[i+1]).isalnum():
            a[w] = (a[w] + a[i+1])
            z.append(i+1)
            i = i + 1
        else:
            w = i+2
            i = i+2
    x = range(0, len(z))
    for i in x:
        a.pop(z[i]-x[i])
    for elem in a:
        if elem == " ":
            a.remove(" ")
    return a


print(mysplit("IT FINALLY WORKS"))
