import time

def timer(n):
    time.sleep(1)
    print(n)
    if n == 0 :
        print("end")
        return None
    return timer(n-1)

timer(5)