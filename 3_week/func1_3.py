def solve(numheads, numlegs):
    '''
    chic + rab = heads
    2chic + 4rab = legs
    2heads - 2rab + 4rab = legs
    2rab = legs - 2heads
    rab = (legs - 2heads)/2
    chic = heads - rab
    '''
    rab = int((l - 2*h)/2)
    chic = h - rab
    print(str(rab) + " rabbits and "+ str(chic) + " chickens")
h, l = [int(x) for x in input().split()]
solve(h, l)