
def simple_resolution_solver(KB, neg_alpha):
    # KB: list of known clauses
    #           clause example: a v b v -c v d
    #           choose your own representation, e.g. ("a", "b", "-c", "d")
    # neg_alpha: query clause, already negated
    # returns True if proof found, False otherwise
    # initialize
    todo = [neg_alpha]
    done = KB.copy()
    # process the todo list one by one
    while todo:
        current = todo.pop()
        # combine current clause with all clauses we've already seen
        for clause in done:
            # apply resolution rule
            resolvents = resolve(current, clause)
            # handle new clauses generated by the resolution rule
            if resolvents == "no results":
                continue #useless reolvent
            for resolvent in resolvents:
                # some important things that can happen here:
                # 1. resolvent is empty: proof found that KB->alpha!
                if len(resolvent) == 0:
                    return True
                # 2. resolvent is always true: throw it away, useless clause
                tautology(resolvent)
                # ONLY if neither of these things happen:
                    todo.append(resolvent)
        # we're done with this clause
        done.append(current)
    # loop ended without proof
    return False


def tautology(resolvent):
    return False
    



def resolve(current, clause: list):
    contr = []
    resolvents = []
    for const in current:
        if const[0] == '-':
            if const[1:] in clause:
                contr.append((const[1:], const))
        else:
            if '-' + const in clause:
                contr.append((const, '-'+const))
    if len(contr) == 0:
        return "no results"
    for pair in contr:
        resolvent = set()
        for term in current + clause:
            if term not in pair:
                resolvent.add(term)
        resolvents.append(list(resolvent))
    return resolvents



"""
def resolution_solver(KB, neg_alpha):
    # KB: list of known clauses
    #           clause example: a v b v -c v d
    #           choose your own representation, e.g. ("a", "b", "-c", "d")
    # neg_alpha: query clause, already negated
    # returns True if proof found, False otherwise
    # initialize
    todo = [neg_alpha]
    done = KB.copy()
    # process the todo list one by one
    while todo:
        current = todo.pop()
        # check if current is redundant
        for clause in done + todo:
            # if clause is a subset of current, then go back to the start of the loop
            # to pick new current
        # combine current clause with all clauses we've already seen
        for clause in done:
            # apply resolution rule
            resolvents = resolve(current, clause)
            # handle new clauses generated by the resolution rule
            for resolvent in resolvents:
                # some important things that can happen here:
                # 1. resolvent is empty: proof found that KB->alpha!
                # 2. resolvent is always true: throw it away, useless clause
                # ONLY if neither of these things happen:
                    todo.append(resolvent)
        # we're done with this clause
        done.append(current)
    # loop ended without proof
    return False
"""

if __name__ == '__main__':
    test_clauses = [(['a', 'b'], ['a', '-b']),
                    (['a', 'b', '-c'], ['a', 'c']),
                    (['a', 'b', '-c', 'd'], ['a', 'c', '-d']),
                    (['d'], ['-d']),
                    (['a', '-b'],	['a', '-c', 'd'])]
    for a, b in test_clauses:
        print(resolve(a, b))

