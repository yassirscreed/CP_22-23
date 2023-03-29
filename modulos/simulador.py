import cap
import event
import obsrand

import matplotlib.pyplot as plt

    
def sim(ht,ba,ss,st):

    c = cap.newc()
    ce = event.evt(0,"arr")
    ct = event.time(ce)
    ck = event.kind(ce)
    tnc = 0
    busy = False
    nwc = 0
    xtrace = [0]
    ytrace = [0]
    
    while ct <= ht:

        if ck == "arr":
            tnc = tnc+1
            c=cap.addE(c,event.evt(ct+obsrand.exprandom(ba),"arr"))
            c=cap.addE(c,event.evt(ct+obsrand.exprandom(ss),"ess"))

        elif ck == "ess":
            if busy:
                nwc = nwc+1
            else:
                busy = True
                c=cap.addE(c,event.evt(ct+obsrand.exprandom(st),"dep"))
        else:
            if nwc == 0:
                busy = False
            else:
                nwc = nwc-1
                c=cap.addE(c,event.evt(ct+obsrand.exprandom(st),"dep"))

        ce = cap.nextE(c)
        ct = event.time(ce)
        ck = event.kind(ce)
        c=cap.delE(c)
        xtrace.append(ct)
        ytrace.append(nwc)

    plt.xlabel('Time')
    plt.ylabel('Cars waiting to pay')
    plt.axis([0, max(xtrace), 0, max(ytrace)])
    plt.plot(xtrace,ytrace,'-')