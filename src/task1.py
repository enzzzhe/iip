import time
import random

#первый варинат
def send_request1(N):
    start_time = time.time()
    dict = {}
    counter = 1
    while True:
        current_time = time.time()
        dict[counter] = current_time
        counter += 1
        
        if N == counter and current_time - start_time < 60:
            exit(print("Invalid rpm"))
        elif N == counter and current_time - start_time >= 60:
            exit(print("Normal rpm"))

#второй вариант(c методом sleep)
def send_request2(N):
    start_time = time.time()
    dict = {}
    counter = 1
    while True:
        current_time = time.time()
        dict[counter] = current_time
        counter += 1
        time.sleep(random.randint(0,1))
        if N == counter and current_time - start_time < 60:
            exit(print("Invalid rpm"))
        elif N == counter and current_time - start_time >= 60:
            exit(print("Normal rpm"))


#if __name__ == "__task1__":
N = int(input())
if N <= 0:
    exit(print("Bad input"))
send_request1(N)



