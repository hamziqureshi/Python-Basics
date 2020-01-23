'''
Implement a group_by_owners dictionary
'''
def group_by_owners(files):
    result = {}
    for key,val in files.items():
        result[val] = result.get(val,[])+[key]
    return result
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(group_by_owners(files))
