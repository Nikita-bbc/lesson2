from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as f:
        while f.readline() != '':
            line = f.readline()
            all_data.append(line.strip())


names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

'''start = time.time()
read_info('file 1.txt')
read_info('file 2.txt')
read_info('file 3.txt')
read_info('file 4.txt')
end = time.time()
print(end - start)'''

start_2 = time.time()
if __name__ == '__main__':
    with Pool() as p:
        p.map(read_info, names)
end_2 = time.time()
print(end_2 - start_2)
