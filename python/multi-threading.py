import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
import string


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
    return "".join(cleaned)


def multi_thread_word_count(data, num_threads=8):
    chunk_size = len(data) // num_threads
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        partial_texts = list(executor.map(process_chunk, chunks))


    full_text = "".join(partial_texts)


    words = full_text.split()

    return Counter(words)



result = multi_thread_word_count(df_y, num_threads=8)

print(result)


