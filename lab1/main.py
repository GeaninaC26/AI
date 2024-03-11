import random
import sys
import time

def valid(bin, w, W):
    weight = 0
    for i in range(0, len(bin)):
        if bin[i] == 1:
            weight = weight + w[i]
        if weight > W:
            return False
    return True

def eval(bin, val):
    value = 0
    for i in range(0, len(bin)):
        if bin[i] == 1:
            value = value + val[i]
    return value

def gen_sir_bin(n, w, W):
    correct = False
    bin = []
    while not correct:
        sol = random.randint(0, 2**n-1)
        bin = [0] * n
        i = n-1
        while i >= 0 and sol != 0:
            bin[i] = sol % 2
            sol = sol // 2
            i = i-1
        correct = valid(bin, w, W)
    return bin

def vecini(bin,w,W):
    vec = []
    for i in range(0, len(bin)):
        cop = bin[:]
        if cop[i] == 0:
            cop[i] = 1
            if valid(cop,w,W):
                vec.append(cop)
    return vec

def nahc(k,n,w,val,W):
    c = gen_sir_bin(n,w,W)
    best = c[:]
    average = eval(c, val)
    for i in range(0, k-1):
        better = False
        vec = vecini(c,w,W)
        for sir in vec:
            if eval(sir,val) > eval(c,val):
                c = sir[:]
                if eval(best,val) < eval(c,val):
                    best = c[:]
                better = True
                break
        if better == False:
            if eval(best,val) < eval(c,val):
                best = c[:]
            c = gen_sir_bin(n,w,W)
        average = average + eval(c, val)

    return best, average // k
        
            

def random_search(k,n,w,val, W):
    soln = gen_sir_bin(n,w,W)
    average = eval(soln, val)
    #print(soln, eval(soln, val))
    for i in range(0,k-1):
        sol = gen_sir_bin(n,w,W)
        average = average + eval(sol, val)
     #   print(sol, eval(sol, val))
        if eval(sol, val) > eval(soln, val):
            soln = sol
    return soln, average // k

def main():
    n = 0
    w = []
    val = []
    W = 0
    # Primul argument este numarul de iteratii
    # Al 2-lea argument, daca exista, este fisierul din care se citesc datele
    if len(sys.argv) > 2:
        file = open(sys.argv[2])
        n = int(file.readline()[:-1])
        for i in range(0, n):
            _, value, weight = file.readline()[:-1].split(' ')
            w.append(int(weight))
            val.append(int(value))
        W = int(file.readline())
    else:
        n = int(input('N:'))
        for i in range(0, n):
            _, value, weight = input('Indices, values, and weights:\n').split(' ')
            w.append(int(weight))
            val.append(int(value))
        W = int(input('Capacity:'))
    
    k = int(sys.argv[1])
    
    start_time = time.time()
    sol, avg = random_search(k, n, w, val, W)
    end_time = time.time()
    print('REZ RANDOM:', avg, eval(sol, val), end_time - start_time)

    start_time = time.time()
    sol2, avg2 = nahc(k,n,w,val,W)
    end_time = time.time()
    #print('REZ NAHC:', sol2, eval(sol2, val), avg2, end_time - start_time)


if __name__== "__main__":
    main()

    
