# insight_data_engineering_coding_challenge


# Table of Contents
1. [Approach](README.md#approach)
2. [Run Instructions](README.md#run-instructions)
3. [Dependencies](README.md#dependencies)

# Approach

This code is written using Python3. It uses a dictionary to store the number of patients and total cost for each drug, using drug name as key.

While the input data do not really seem to include lines where both the patient and the drug name are the same, to make sure we only count the number of unique patients, as we read each row, we check whether the patient is already prescribed to the drug or not using another dictionary which maps the drug name to the set of patients.
Following problem instructions, we use the first name and last name to identify a unique patient instead of the ID. In this case, key corresponds to drug name and value corresponds to set which is composed of tuple (prescriber_first_name, prescriber_last_name).

After that, the code sorts output according to the total cost (descending order) and drug name (ascending order) using Ordered Dictionary.

# Run Instructions

As given in the problem instructions, we can run the program via the Python script with two command line arguments: the input and output file paths. The script will print out correct usage if arguments are not given or given inappropriately. The shell script run.sh also gives example usage cases.

# Dependencies

The program does not have external dependencies outside of the standard Python3 libraries. System modules used include csv for comma-separated text IO, sys for command line argument parsing, and collections for data representation.



