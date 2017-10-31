from csv import DictReader

# Read in locations.txt and parse data as ImageData class, compile into ImageSet
def parse_csv_to_object(csv, obj, attributes, delimiter):
    objects = []


    with open(csv) as csvFile:
        reader = DictReader(csvFile, delimiter=delimiter)
        for row in reader:
            new_obj = obj()

            for attr in attributes:
                setattr(new_obj, attr, row[attr])

            new_obj.init_params()
            objects.append(new_obj)

    return objects


# Read in locations.txt and parse data as ImageData class, compile into ImageSet
def parse_csv_with_constructor(csv, obj, delimiter):
    objects = []

    with open(csv, 'r') as csvFile:
        for line in csvFile:
            new_obj = obj(line)
            objects.append(new_obj)

    return objects


def clean_leading_whitespace(csv):
    lines = []

    with open(csv, 'r') as csvFile:
        for line in csvFile:
            lines.append(line.replace(', ', ','))

    cleaned_csv = ''.join(lines)

    with open(csv, 'w') as csvFile:
        csvFile.write(cleaned_csv)

    return cleaned_csv
