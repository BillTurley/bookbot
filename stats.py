def get_num_words(all_words):
    count_words = len(all_words.split())
    return count_words

def get_character_instances(all_words):
    count_letters = {}
    characters = list(all_words)
    for character in characters:
        if character.lower() in count_letters:
            count_letters[character.lower()] += 1
        else:
            count_letters[character.lower()] = 1
    return count_letters

def sort_key(list_counts):
    return list_counts["num"]

def get_sorted_list(letter_counts):
    list_counts = []
    for letter in letter_counts:
        if letter.isalpha():
            tmp_dict = {"char": letter, "num": letter_counts[letter]}
            list_counts.append(tmp_dict)
    list_counts.sort(reverse=True, key=sort_key)
    return list_counts