import csv

values = [["customer_id", "customer_name"], ["1", "Ani"], ["2", "Sunny"], ["3", "Max"]]


def write_csv_file(filename, values):
    with open(filename, "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(values)


write_csv_file(filename="data.csv", values=values)


def read_csv_file(filename):
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


print(read_csv_file(filename="data.csv"))
