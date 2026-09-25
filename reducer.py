import sys
current_key, current_count = None, 0
for line in sys.stdin:
    line = line.strip()
    if line:
        key, count = line.split('\t')
        if current_key == key:
            current_count += int(count)
        else:
            if current_key: print(f'{current_key}\t{current_count}')
            current_key, current_count = key, int(count)
if current_key: print(f'{current_key}\t{current_count}')