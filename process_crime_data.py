import csv
import random


def build_reduced_dataset(
		original_CSV_filename='crimes.csv',
		reduced_CSV_filename='reduced_crimes.csv',
		reduced_column_descriptions=[
			'Primary Type',
			'Latitude',
			'Longitude',
		],
		row_sample_probability=1.0,
		omit_rows_with_empty_columns=True,
		omit_crimes_before_year=0,
	):
	"""
	Takes the original dataset CSV file (1.34 GB) and reduces it to a new CSV.
	New CSV:
		- Contains only specified features/columns.
		- Contains a sampling of the original rows, given a specified probability with which we keep each row.
		- If desired, omits a row if it does not contain any (or several) of the desired columns.
		- If desired, omits all crimes occurring before a certain year.

	For example, to get a cleaned CSV that:
		- Containing only the crime's 'Primary Type', 'Latitude', and 'Longitude'
		- Samples ~10% of the rows
		- Removes rows that are missing any of the desired columns
		- Removes crimes occurring before 2009
	make the following call:
		>>> build_reduced_dataset(row_sample_probability=0.1, omit_crimes_before_year=2009)
	"""
	# Get the index of each column/feature we wish to keep
	reduced_column_indices = [ORIGINAL_COLUMN_INDEX_FOR_DESCRIPTION[description] for description in reduced_column_descriptions]

	with open(original_CSV_filename, 'rb') as original_CSV_file:
		with open(reduced_CSV_filename, 'wb') as reduced_CSV_file:
			original_CSV_reader = csv.reader(original_CSV_file, delimiter=',')
			reduced_CSV_writer = csv.writer(reduced_CSV_file, delimiter=',')

			# Process each row of the original CSV
			for original_row in original_CSV_reader:

				# Flip a (loaded) coin to determine if this row stays
				if not flip_biased_coin(row_sample_probability):
					continue

				# Create new row with only desired columns
				reduced_row = []
				row_contains_empty_column = False
				for index in reduced_column_indices:
					reduced_row += [ original_row[index] ]
					if not original_row[index]:
						row_contains_empty_column = True

				# Check if row has missing columns
				if omit_rows_with_empty_columns and row_contains_empty_column:
					continue

				try:
					if int(original_row[ORIGINAL_COLUMN_INDEX_FOR_DESCRIPTION['Year']]) < omit_crimes_before_year:
						continue
				except Exception:
					pass

				# Write reduced row to file
				reduced_CSV_writer.writerow(reduced_row)












def flip_biased_coin(probability_true=0.5):
	"""
	Flip a biased coin with the specified 'true' probability; return true or false.
	"""
	sample_result = random.random()
	if sample_result < probability_true:
		return True
	else:
		return False



# Column descriptions
ORIGINAL_COLUMN_DESCRIPTIONS = [
	'ID',
	'Case Number',
	'Date',
	'Block',
	'IUCR',
	'Primary Type',
	'Description',
	'Location Description',
	'Arrest',
	'Domestic',
	'Beat',
	'District',
	'Ward',
	'Community Area',
	'FBI Code',
	'X Coordinate',
	'Y Coordinate',
	'Year',
	'Updated On',
	'Latitude',
	'Longitude',
	'Location'
]

# Map from column description to its index in each CSV row
ORIGINAL_COLUMN_INDEX_FOR_DESCRIPTION = {}
for index, column_name in enumerate(ORIGINAL_COLUMN_DESCRIPTIONS):
	ORIGINAL_COLUMN_INDEX_FOR_DESCRIPTION[column_name] = index




