xA = 31
xB = 27
xP = 10000000018354

yA = 56
yB = 16
yP = 10000000008640


for nA in range(108267716477):
    for nB in range(246062992875):
        cxp = nA * xA + nB * xB
        cyp = nA * yA + nB * yB
        if cxp == xP and cyp == yP:
            print("Solution found")
            print("nA, nB", nA, nB)
            print("Total tokens", 3*nA + nB)