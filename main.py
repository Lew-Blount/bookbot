def main(path_to_file):
    """
    Analyzes a text file, counting words and characters, and prints a report.

    Args:
        path_to_file: The path to the text file.
    """
    try:
        with open(path_to_file, 'r', encoding='utf-8') as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {path_to_file}")
        return

    word_count = count_words(file_contents)
    character_counts = count_characters(file_contents)

    print(f'--- Begin report of {path_to_file} ---\n')
    print(f'{word_count} words found in the document\n')

    for char, count in character_counts.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print('--- End report ---')


def count_words(file_contents):
    """
    Counts the number of words in a string.

    Args:
        file_contents: The string to analyze.

    Returns:
        The number of words in the string.
    """
    words = file_contents.split()
    return len(words)


def count_characters(file_contents):
    """
    Counts the occurrences of each character in a string (case-insensitive).

    Args:
        file_contents: The string to analyze.

    Returns:
        A dictionary where keys are characters and values are their counts.
    """
    character_counts = {}
    lowered_content = file_contents.lower()
    for char in lowered_content:
        character_counts[char] = character_counts.get(char, 0) + 1
    return character_counts

if __name__ == "__main__":
    main("books/frankenstein.txt")