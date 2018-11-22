Fshards = [
    [1,2,3,4,5,6,7,8,9,1,3,4,2,6,4,5],
    [3,4,5,6,7,8,9,3,3,3,3,4,2,6,7,5],
    [3,4,5,6,3,3,9,3,3,3,3,4,4,6,4,5],
    [1,2,3,4,5,6,7,8,9,1,3,4,2,5,4,5],
    [3,4,5,2,7,8,9,3,3,3,3,4,2,6,5,5],
    [3,4,5,4,3,3,9,3,3,3,3,4,2,3,4,5],
    [1,2,3,4,5,6,7,8,9,1,3,4,2,7,4,5],
    [3,4,5,7,7,8,9,3,3,3,3,4,2,9,4,5],
    [3,4,5,6,2,3,4,3,3,3,3,4,2,3,4,5],
    [1,2,3,9,6,6,7,8,9,1,3,4,2,2,4,5],
    [3,4,5,6,5,8,9,3,3,3,3,4,2,6,6,5],
    [3,4,5,3,4,3,9,3,3,3,3,4,2,6,1,5],
]

def alocate(F, n):
    """
    F - macierz shardów z ich obciążeniem w czasie
    n - liczba węzłów chmury
    """

    # 1
    wts = sum([sum(x) for x in F])
    # 2
    nwts = wts/n
    # 3
    #TODO: Posortuj F po sumie
    #sortedF = [sum(x) for x in F].sort()
    # 4
    N = [[y*0 for y in F[0]] for x in range(0, n)]
    for shard in F:
        sumaSharda = sum(shard)

        maxValue = None
        maxNodeIndex = None

        for index, node in enumerate(N):
            sumaWezla = sum(node)
            if(sumaWezla > nwts):
                continue

            value = abs(nwts-sumaWezla)-abs(nwts-(sumaWezla+sumaSharda))

            if(maxValue is None or value > maxValue):
                maxValue=value
                maxNodeIndex=index

        # suma dwóch wektorów
        N[maxNodeIndex]=list(map(sum, zip(N[maxNodeIndex], shard)))

    return N

N = alocate(Fshards, 3)
print(N)

power = 15

loadN = list()
for node in N:
    nodeLoad = 0
    for index, value in enumerate(node):
        load = value-power
        if(load > 0):
            if(index < len(node)-1):
                node[index+1] += load
            nodeLoad += load
        
    loadN.append(nodeLoad)

print(loadN)