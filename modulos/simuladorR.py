import capR as cap
import eventR as event
import car
import myqueue as queue
import obsrand

import matplotlib.pyplot as plt

    
def sim(ht,ba,ss,st):

    c = cap.newc()
    ta = 0
    ce = event.evt(0,"arr",car.new_car(0))
    ct = event.time(ce)
    ck = event.kind(ce)    
    cc = event.car(ce)
    tnc = 0
    busy = False
    qwc = queue.newq()
    av_wait = 0.0
    nav_wait = 0
    max_time = 0.0
    av_ss_time = 0.0
    nav_ss_time = 0
    
    xtrace = []
    ytrace = []
    
    while ct <= ht:

        if ck == "arr":
            tnc = tnc+1
            ta = ct+obsrand.exprandom(ba)
            c=cap.addE(c,event.evt(ta,"arr",car.new_car(ta)))
            
            ts = ct+obsrand.exprandom(ss)
            cc=car.update_ss(cc,ts)
            c=cap.addE(c,event.evt(ts,"ess",cc))

        elif ck == "ess":
            if busy:
                qwc=queue.enter(cc,qwc)
            else:
                busy = True
                c=cap.addE(c,event.evt(ct+obsrand.exprandom(st),"dep",cc))

        else:
            # Tempo de espera para efectuar pagamento
            wt = ct - car.ss_time(cc)
            
            # Actualizar tempo maximo a espera para pagar
            if wt > max_time:
                max_time = wt
            
            # Actualizar o tempo medio de espera para pagar
            av_wait = av_wait + wt
            nav_wait = nav_wait + 1
            
            # Actualizar o tempo medio na zona de self-service
            av_ss_time = av_ss_time + (car.ss_time(cc)-car.arr_time(cc))
            nav_ss_time = nav_ss_time + 1
            
            xtrace.append(ct)
            ytrace.append(wt)           
            
            if queue.empty(qwc):
                busy = False
            else:
                cc = queue.first(qwc)
                qwc = queue.leave(qwc)
                c = cap.addE(c,event.evt(ct+obsrand.exprandom(st),"dep",cc))

        ce = cap.nextE(c)
        ct = event.time(ce)
        ck = event.kind(ce)
        cc = event.car(ce)
        c = cap.delE(c)

    print('Average waiting time: %5.1f' %(av_wait/nav_wait))
    print('Maximum waiting time: %5.1f' %max_time)
    print('Average self-service time: %5.1f' %(av_ss_time/nav_ss_time))
    
    plt.xlabel('Time')
    plt.ylabel('Current waiting time')
    plt.axis([0, max(xtrace), 0, max(ytrace)])
    plt.plot(xtrace,ytrace,'-')