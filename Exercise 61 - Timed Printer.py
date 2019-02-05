# Print hello every period of time
import time
i=0
while True:
    i=i+1
    print(i)
    if i >= 10:
        break
    print("hello")
    time.sleep(i)