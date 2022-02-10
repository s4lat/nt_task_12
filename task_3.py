files = ['1.txt', '2.txt', '3.txt']


contents = []
for f_name in files:
    with open(f_name, 'r') as f:
        contents.append(f.read().strip())

contents = list(zip(files, contents))
contents.sort(key=lambda x: x[1].count('\n'))

with open('concatenated.txt', 'w') as f:
    for content in contents:
        lines_count = content[1].count("\n") + 1
        f.write(f'{content[0]}\n{lines_count}\n{content[1]}\n')