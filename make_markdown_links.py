import os
import json
from scripts.utils import read_and_process_json

def create_markdown_links(words_data):
    words_links = []
    phrases_links = []

    # Iterate through each word entry in the words data
    for word in words_data:
        if word.get("has_md", False):
            text = word.get("text", "")
            md_path = word.get("md_path", "")
            
            # Create the markdown link
            markdown_link = f'[{text}]({md_path})'
            
            # Append to words or phrases list based on md_path
            if 'md/words/' in md_path:
                words_links.append(markdown_link)
            elif 'md/phrases/' in md_path:
                phrases_links.append(markdown_link)

    return words_links, phrases_links

def write_links_to_file(words_links, phrases_links, output_file):
    # Format the output with sections
    output_content = "## Words\n" + '\n'.join(words_links) + '\n\n## Phrases\n' + '\n'.join(phrases_links)
    with open(output_file, 'w', encoding='utf-8') as links_file:
        links_file.write(output_content)

words_data = read_and_process_json('data/words.json')
words_links, phrases_links = create_markdown_links(words_data)
write_links_to_file(words_links, phrases_links, 'markdown_links.txt')

print('Markdown links have been added to markdown_links.txt')

