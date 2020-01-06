
def read_file(file):

    with open(file, 'r', encoding='utf-8') as f:
        words = []
        all_words = f.readline()
        all_words = all_words.replace(',', '')
        all_words = all_words.split(' ')
        for i in all_words:
            words.append(i.lower())
        # for i in all_words:
        #     words.append(i.lower())
        #
        # print(words)
        # # print(words[2])
        return list(set(words))

def save_file(new_file_name, words_list):
    with open(new_file_name, 'w') as f:
        count = len(words_list)
        # print(words_list)
        words_list.sort()
        # print(count)
        # print(words_list)
        f.write(f'колличество строк: {count}\n')
        for i in words_list:
            f.write(f'{i}\n')


f = read_file('data.txt')
save_file('new.txt', f)
