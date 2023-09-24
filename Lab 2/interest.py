import math as m
def simp_intr(p,t,r=11.5):
    return (p*r*t)/100
def comp_intr(p,t,r=11.5):
    ci=p*m.pow((1+r/100),t)
    return ci-p
