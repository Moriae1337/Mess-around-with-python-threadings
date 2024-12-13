from calculations import taylor_cos, taylor_sin, taylor_exp
import threading
def calculate(name,x,template, terms=10,start=0):
    """Compute template using the Taylor series expansion."""
    exp_approx = 0
    list_show = []
    for n in range(start,terms+1):
        exp_approx += template(x,n)

    print(name,round(exp_approx,5))

if __name__ == '__main__':
    #thread exp
    t1 = threading.Thread(target=calculate,args=("exp:",5,taylor_exp,10,0))
    #thread sin
    t2 = threading.Thread(target=calculate,args=("sin:",5,taylor_sin,10,0))
    #thread cos

    t1.start()

    t2.start()

    calculate("cos:",5,taylor_cos,10,0)

    t1.join()
    
    t2.join()