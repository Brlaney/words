# from scripts.utils import read_and_process_json

# data = read_and_process_json('data/backed-up/long-entries/after.json')

# ids = [entry['id'] for entry in data]

# print('\nids')
# print(ids)
# print('\n')

import os

def generate_markdown_links(dir_path, base_url):
    """
    Generate markdown links for all files in the given directory.

    :param dir_path: Path to the directory containing markdown files
    :param base_url: The base URL to use in the markdown links
    :return: A list of markdown links
    """
    links = []
    for filename in os.listdir(dir_path):
        if filename.endswith(".md"):
            file_name_without_ext = os.path.splitext(filename)[0]
            link = f"- [{file_name_without_ext.replace('_', ' ')}]({base_url}/{filename})"
            links.append(link)
    return links


# Directories containing markdown files
words_dir = "md/words"
phrases_dir = "md/phrases"

# Generate markdown links for words
print("For words:")
word_links = generate_markdown_links(words_dir, "md/words")
for link in word_links:
    print(link)

print("\nFor phrases:")
# Generate markdown links for phrases
phrase_links = generate_markdown_links(phrases_dir, "md/phrases")
for link in phrase_links:
    print(link)


'''

id_list = [20, 36, 53, 57, 59, 61, 65, 66, 74, 76, 81, 84, 90, 95, 110, 113]

if some_id in id_list:
    print("ID is in the list")
else:
    print("ID is not in the list")
    

'''