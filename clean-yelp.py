"""
Cleaning Yelp dataset
    1. Taking JSON and converting it to CSV
    2. Removing type, business_id, user_id, date

"""

# -*- coding: utf-8 -*-
import argparse, collections, os, csv, sys
import simplejson as json

def read_and_write_file(json_file_path, csv_file_path, column_names):
    """Read in the json dataset file and write it out to a csv file, given the column names."""
    with open(csv_file_path, 'wb+') as fout:
        csv_file = csv.writer(fout)
        csv_file.writerow(list(column_names))
        with open(json_file_path) as fin:
            for line in fin:
                line_contents = json.loads(line)
                csv_file.writerow(get_row(line_contents, column_names))

def get_superset_of_column_names_from_file(json_file_path):
    """Read in the json dataset file and return the superset of column names."""
    column_names = set()
    with open(json_file_path) as fin:
        for line in fin:
            line_contents = json.loads(line)
            column_names.update(
                    set(get_column_names(line_contents).keys())
                    )
    return column_names

def get_column_names(line_contents, parent_key=''):
    """
    Return a list of flattened key names given a dict.
    These will be the column names for the eventual csv file.
    """
    column_names = []
    for k, v in line_contents.iteritems():
        column_name = "{0}.{1}".format(parent_key, k) if parent_key else k
        if isinstance(v, collections.MutableMapping):
            column_names.extend(
                    get_column_names(v, column_name).items()
                    )
        else:
            column_names.append((column_name, v))
    return dict(column_names)

def get_nested_value(d, key):
    """Return a dictionary item given a dictionary `d` and a flattened key from `get_column_names`."""
    if '.' not in key:
        if key not in d:
            return None
        return d[key]
    base_key, sub_key = key.split('.', 1)
    if base_key not in d:
        return None
    sub_dict = d[base_key]
    return get_nested_value(sub_dict, sub_key)

def get_row(line_contents, column_names):
    """Return a csv compatible row given column names and a dict."""
    row = []
    for column_name in column_names:
        line_value = get_nested_value(
                        line_contents,
                        column_name,
                        )
        if isinstance(line_value, unicode):
            row.append('{0}'.format(line_value.encode('utf-8')))
        elif line_value is not None:
            row.append('{0}'.format(line_value))
        else:
            row.append('')
    return row

if __name__ == '__main__':
    json_file = './yelp/yelp_academic_dataset_review.json'
    csv_file = './yelp/yelp_academic_dataset_review.csv'
    csv_file_removed = './yelp/yelp_academic_dataset_review_1.csv'

    # 1. JSON to CSV
    if not os.path.isfile(csv_file):
        print 'Converting JSON to CSV'
        column_names = get_superset_of_column_names_from_file(json_file)
        read_and_write_file(json_file, csv_file, column_names)
    
    # 2. Cleaning Data Step One
    # current: user_id,review_id,text,votes.cool,business_id,votes.funny,stars,date,type,votes.useful
    # removing: user_id,review_id,business_id,date,type 
    # becomes: text,votes.cool,votes.funny,stars,votes.useful
    print 'Cleaning Data Now'
    if not os.path.isfile(csv_file_removed):
        with open(csv_file, "rb") as fp_in, open(csv_file_removed, "wb") as fp_out:
            reader = csv.reader(fp_in, delimiter=",")
            writer = csv.writer(fp_out, delimiter=",")
            for row in reader:
                del row[0] # user_id
                del row[0] # review_id
                del row[2] # business_id
                del row[4] # date
                del row[4] # type
                writer.writerow(row)
