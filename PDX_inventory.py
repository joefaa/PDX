item_list = ()
file = "Example_excel.csv"
number = 0
for line in open(file):
    file = open("output.csv", "w")
    if line.startswith("DoI"):
        number += 1
        info = line.split("HT")
        DOI = info[0][3:].rstrip()
        DOS = info[1][3:].rstrip()
        mouse = info[3][3:].rstrip()
        passage = info[4].rstrip()
        PDX_ID = info[5].rstrip()
        TR = info[6][3:].rstrip()
        print_string += "{},{},{},{},{},{}\n".format(PDX_ID, TR, mouse, passage, DOI, DOS)
        print(print_string)
        file.write(print_string)
    else:
        print_string = ""
        number += 1
        barcode = line.rstrip()
        print_string = "{},".format(barcode)
file.write(print_string)
