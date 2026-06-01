input_file = open("../data/employees.csv", "r")

output_file = open("../output/it_employees.txt", "w")

next(input_file)

for line in input_file:
    columns = line.strip().split(",")

    department = columns[2]

    if department == "IT":
        output_file.write(line)

input_file.close()
output_file.close()