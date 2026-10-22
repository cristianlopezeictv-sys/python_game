from tqdm import tqdm
import time

for i in tqdm(range(100), desc="Hola"):
    time.sleep(0.005)
