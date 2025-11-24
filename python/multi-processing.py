import pandas as pd
from multiprocessing import Pool, cpu_count
from collections import Counter


df = pd.read_csv("shakespeare.csv")
df_y = df["y"]


def process_chunk(chunk):
    cleaned = []
    for ch in chunk:
        if ch in [".", ",", ";"]:
            cleaned.append("")
        elif ch == " ":
            cleaned.append(" ")
        else:
            cleaned.append(ch.lower())
    
    text = "".join(cleaned)
    words = text.split()
    
    return Counter(words) 



def chunkify(data, n):
    chunk_size = len(data) // n
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]



def multiprocess_word_count(data):

    num_workers = cpu_count()
    chunks = chunkify(data, num_workers)

    with Pool(processes=num_workers) as pool:
        partial_counts = pool.map(process_chunk, chunks)


    total_count = Counter()
    for cnt in partial_counts:
        total_count.update(cnt)

    return total_count


result = multiprocess_word_count(df_y)
print(result)