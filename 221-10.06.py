with open('file1.txt') as f1, open('file2.txt') as f2, open('merged.txt', 'w') as fout:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    for l1, l2 in zip(lines1, lines2):
        fout.write(l1.strip() + '\n')
        fout.write(l2.strip() + '\n')

    # Write remaining lines from longer file
    if len(lines1) > len(lines2):
        fout.writelines(lines1[len(lines2):])
    else:
        fout.writelines(lines2[len(lines1):])

print("Files merged.")
