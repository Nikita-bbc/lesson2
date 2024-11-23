import time
import threading


def write_words(words_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(words_count):
            time.sleep(0.1)
            f.write(f'Какое-то слово № {i + 1}\n')
        print(f'Завершилась запись в файл {file_name}')


start = time.time()
write_words(10, 'example_1.txt')
write_words(20, 'example_2.txt')
write_words(30, 'example_3.txt')
write_words(40, 'example_4.txt')
end = time.time()
print(f'Затраченное время выполнения программы без потоков: {end - start}')

start_flow = time.time()

thread_1 = threading.Thread(target=write_words, args=(10, 'example_5.txt'))
thread_1.start()


thread_2 = threading.Thread(target=write_words, args=(20, 'example_6.txt'))
thread_2.start()


thread_3 = threading.Thread(target=write_words, args=(30, 'example_7.txt'))
thread_3.start()


thread_4 = threading.Thread(target=write_words, args=(40, 'example_8.txt'))
thread_4.start()
thread_4.join()


end_flow = time.time()

print(f'Затраченное время выполнения программы с потоками: {end_flow - start_flow}')
