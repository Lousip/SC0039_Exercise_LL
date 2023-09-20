# First need to make sure to import csv
import csv
# Where "brca_cnvs_tcga-1.csv" is the name of your file
with open("brca_cnvs_tcga-1.csv", "r") as file:
   # If your first row is the names of each column you need to skip them otherwise you can't make calculations
   next(file)
   # Create a new variable capable of using the file as csv
   reader = csv.reader(file)
    # create a new CSV file named new_file to put your new column in
   with open("new_file.csv", "w", newline='') as new_file: 
            writer = csv.writer(new_file) 
            # Rewrite the names of the headers you skipped previously
            header = ["ID","chrom","loc.start","loc.end","seq_length"]
            writer.writerow(header)
            for row in reader:
                # row[3] is the column content you want to substract from the other column which is row[2]
                # You have to replace by the columns numbers you want to substract
                # 5 is the number of the column you want the substraction to be in
                # change int by the type of variable you have
                row.insert(5, (int(row[3]) - int(row[2])))
                writer.writerow(row) 

            
