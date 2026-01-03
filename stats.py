def get_num_words(text: str) -> int:
    """
    Return the number of words in the given text string.
    Splits on any whitespace.
    """
    return len(text.split())

def get_char_counts(text: str) -> dict:
    """
    Return a dictionary mapping each character (lowercased) to its count in the text.
    Counts spaces and punctuation as well.
    """
    counts = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def get_sorted_char_counts(char_counts: dict) -> list:
    """
    Convert the character counts dictionary into a list of dictionaries
    like {"char": <char>, "num": <count>} for alphabetical characters
    only, and sort the list from greatest to least by count.
    """
    items = []
    for ch, count in char_counts.items():
        if ch.isalpha():
            items.append({"char": ch, "num": count})

    def _num_key(d: dict) -> int:
        return d["num"]

    items.sort(key=_num_key, reverse=True)
    return items

