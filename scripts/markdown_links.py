from scripts.utils import read_and_process_json
from scripts.utils import create_markdown_links
from scripts.utils import write_links_to_file

'''
    Read the words data from JSON
    Create markdown links from the words data
    Write the links to the output file
'''
words_data = read_and_process_json('data/words.json')
words_links, phrases_links = create_markdown_links(words_data)
write_links_to_file(words_links, phrases_links, 'data/markdown_links.txt')

print('Markdown links have been added to markdown_links.txt')
print('Markdown links have been added to markdown_links.txt')
