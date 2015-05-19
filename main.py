import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open("counts.txt") as counts:
    total_tries, successful_tries = (int(number) for number in counts)

with open("words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

def get_char():
    if random.random() < 0.9:
        return random.choice(letters)
    else:
        return ' '

def create_string():
    string = ''
    for _ in range(15):
        string += get_char()
    return string

def end_mark():
    return random.choice(['.', '!', '?'])

def is_in_dict(word):
    return word.lower() in english_words

def is_english_string(string):
    candidates = string.split()
    for word in candidates:
        if not is_in_dict(word):
            return False
    return True

if __name__ == '__main__':
    successes = 0
    while successes < 2:
        string = create_string()
        total_tries += 1
        if is_english_string(string):
            successes += 1
            attempt_number = '{:.3e}'.format(total_tries).replace('e+', ' x 10<sup>') + '</sup>'
            front_matter = '---\nlayout: sentence\nattempt: %s\n---\n' % (attempt_number)
            text = string.strip().capitalize() + end_mark()
            with open("_sentences/%s.html" % (successes + successful_tries), "w+") as new:
                new.write(front_matter + text)
    with open("counts.txt", "w") as counts:
        counts.write('%s\n%s' % (total_tries, successes + successful_tries))