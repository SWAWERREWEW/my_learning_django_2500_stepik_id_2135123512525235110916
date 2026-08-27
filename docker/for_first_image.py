# docker/for_first_image.py
import time
import numpy
from tqdm import tqdm

total = 300
iter_tqdm = tqdm(range(total))
for i in iter_tqdm:
    iter_tqdm.set_description(f"x = {i/100}, sin = {numpy.sin(i/100):.4f}")
    time.sleep(1)
