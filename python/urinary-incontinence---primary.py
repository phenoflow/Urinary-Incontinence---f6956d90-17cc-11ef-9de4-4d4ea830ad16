# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"8HTX.00","system":"readv2"},{"code":"R083100","system":"readv2"},{"code":"3940.00","system":"readv2"},{"code":"8C14.00","system":"readv2"},{"code":"1A26.00","system":"readv2"},{"code":"16F..00","system":"readv2"},{"code":"Z9EA.00","system":"readv2"},{"code":"R083z00","system":"readv2"},{"code":"R083200","system":"readv2"},{"code":"15918.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('urinary-incontinence-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["urinary-incontinence---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["urinary-incontinence---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["urinary-incontinence---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
