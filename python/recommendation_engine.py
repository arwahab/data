import pandas as pd

# loading movies metadata
metadata = pd.read_csv('movies_metadata.csv', low_memory=False)

# print the first three rows to a source file
source_file = open('output.txt', 'w')
print(metadata.head(3), file=source_file)
source_file.close()