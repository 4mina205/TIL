def bigNuminlist(numlist):
    import itertools
    bignumlist=[]
    permu=[]
    for i in numlist:
        bignumlist.append(max(i, int(str(i)[::-1])))
    for i in itertools.permutations(bignumlist):
        permu.append(int("".join(map(str,i))))
    print(max(permu))
numl = [1,24]
bigNuminlist(numl)







