def transform(source, rules):
    a = ""
    for c in source:
        a += rules.get(c, c)
    return(a)

def iterate(depth, axiom, rules):
    yield axiom

    if depth > 0:
        for q in iterate(depth - 1, transform(axiom, rules), rules):
            yield q
    else:
        return

def full_iterate(depth, axiom, rules):
    return(list(iterate(depth, axiom, rules))[-1])

if __name__ == "__main__":
    axiom = "0"
    rules = {"1": "11", "0": "1[0]0"}
    print(transform(axiom, rules))
    for n, r in enumerate(iterate(4, axiom, rules)):
        print("{0}: {1}".format(n, r))
