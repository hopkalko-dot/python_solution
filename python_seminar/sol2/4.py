import csv

with open('products.csv', newline='', encoding='utf-8') as fin, \
     open('expensive.csv', 'w', newline='', encoding='utf-8') as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    header = next(reader, None)
    if header:
        writer.writerow(header)
    for row in reader:
        try:
            if float(row[2]) > 100:
                writer.writerow(row)
        except:
            pass
