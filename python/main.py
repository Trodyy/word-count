import threading

with open("/home/trody/code/projects/word-count/test.txt", "r") as file:
    text = file.read()

def reading_file(file_path , batch_size = 1024*1024) : 
    with open(file_path , 'r' , encoding='utf-8') as f :
        while True :
            data = f.read(batch_size)
            if not data :
                break
            yield data