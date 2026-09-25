import sys
for line in sys.stdin:
    line = line.strip()
    if line:
        parts = line.split('\t')
        if len(parts) == 3:
            print(f'{parts[1]}_{parts[2]}\t1')