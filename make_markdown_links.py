import os

md_directory = 'data/md/'
markdown_links = []

# Iterate through all files in the specified directory
for filename in os.listdir(md_directory):
    '''
    Check if the file has a .md extension
    Remove the .md extension to get the base name
    Create the markdown link with spaces replaced by hyphens
    Append the link to the list
    '''

    if filename.endswith('.md'):
        base_name = filename.replace('.md', '')
        
        # Replace spaces with hyphens for the link
        link_name = base_name.replace(' ', '-')
        
        # Create the markdown link
        markdown_link = f'[{base_name}]({md_directory}{link_name}.md)'
        
        # Append the link to the list
        markdown_links.append(markdown_link)

# Join the list into a single string with line breaks
output_content = '\n'.join(markdown_links)

# Write the output to the markdown_links.txt file
with open('markdown_links.txt', 'w', encoding='utf-8') as links:
    links.write(output_content)

print('Markdown links have been added to markdown_links.txt')
