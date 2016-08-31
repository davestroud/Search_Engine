def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graphA:
            newranks = (1 - d) / npages
            #update by summing in the inlink ranks

        newranks[page] = newrank
    ranks = newranks
    return ranks
