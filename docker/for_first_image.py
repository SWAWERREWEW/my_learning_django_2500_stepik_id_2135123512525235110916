# docker/for_first_image.py
import time

total = 100
count = 0
while count < total:
    count += 1
    print("kikidon: " + str(count))
    time.sleep(1)
