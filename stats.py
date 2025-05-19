def words_counter(book_string):
    num_words = book_string.split()
    words_number = len(num_words)
    return words_number

def character_counter(text):
    characters_count = {} 
    letters = text.lower()
    for character in letters:
        if character in characters_count:
            characters_count[character] += 1
        else:
            characters_count[character] = 1
    return characters_count


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

