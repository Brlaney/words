from scripts.utils import read_and_process_json

data = read_and_process_json('data/backed-up/long-entries/after.json')

ids = [entry['id'] for entry in data]

print('\nids')
print(ids)
print('\n')

'''

id_list = [20, 36, 53, 57, 59, 61, 65, 66, 74, 76, 81, 84, 90, 95, 110, 113]

if some_id in id_list:
    print("ID is in the list")
else:
    print("ID is not in the list")
    

'''