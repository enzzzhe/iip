import random
def music_queue (amount_of_songs, N):
    f = open('task2.txt', 'r')
    queue = [] #создаем очередь для отслеживания последних N элементов
    list_of_music = [] #массив с песнями
    playlist = [] #то, что мы выведем в итоге
    #заполняем массив list_of_music песнями из файла
    for line in f:
        line = line.replace('\n', '')
        line = line.replace('\t', ' - ')
        list_of_music.append(line)

    while True:
        #выходим из цикла while True
        if len(playlist) == amount_of_songs:
            f.close()
            print(f"{playlist} \n")
            exit()

        #генерируем случайную песню из списка
        temporary = list_of_music[random.randint(0, len(list_of_music)) - 1]

        #это пришлось написать, потому что выдавалась ошибка пустой очереди
        if len(queue) == 0:
            queue.append(temporary)
            playlist.append(temporary)
            continue

        #выходим из цикла (или задаем новое значение переменной), если она уже есть в очереди
        if temporary in queue:
            continue
        #если песня еще не встречалась, а очередь меньше N, расширяем очередь и плейлист
        elif len(queue) < N:
            queue.append(temporary)
            playlist.append(temporary)
        #если размер очереди превысил N, избавляемся от элемента в начале и добавляем новый
        else:
            queue.pop(0)
            queue.append(temporary)
            playlist.append(temporary)

amount_of_songs = int(input())
N = int(input())
if N <= 0:
    exit(print('Bad input'))
print(music_queue(amount_of_songs, N))
