lines = []

with open("merania\\mereni.txt", encoding="utf-8") as file:
    for line in file:
        day, temp = line.split('\t')
        lines.append([day, float(temp)])
print(lines)

"""
\t - tabulator
\n - nový riadok
\\ - backslash
"""
