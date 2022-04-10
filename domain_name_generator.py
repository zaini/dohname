from collections import defaultdict
import pandas as pd


def read_file(file_name):
    lst = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            formatted_line = line.strip().replace('.', '')
            lst.append(formatted_line)
    return lst


if __name__ == "__main__":
    # Convert to set just incase of duplicates
    tlds = list(set(read_file('tlds.txt')))
    words = list(set(read_file('words.txt')))

    res = defaultdict(list)

    for tld in tlds:
        for word in words:
            if len(tld) < len(word) and word[len(word)-len(tld):] == tld:
                res[tld].append(word)

    df = pd.concat([pd.DataFrame(data={key: res[key]}) for key in res], axis=1)
    df.to_csv('tld_words.csv', index=False)
