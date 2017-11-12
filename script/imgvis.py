import io
import bson                       # this is installed with the pymongo package
import csv
import matplotlib.pyplot as plt
from skimage.data import imread   # or, whatever image library you prefer
import multiprocessing as mp      # will come in handy due to the size of the data
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from textwrap import wrap


mydict = None
with open('data/category_names.csv') as infile:
    reader = csv.reader(infile)
    next(reader) # ignore the header line
    mydict = {int(rows[0]):(rows[1], rows[2], rows[3]) for rows in reader}

data = bson.decode_file_iter(open('data/train_example.bson', 'rb'))


prod_to_category = dict()

for c, d in list(enumerate(data))[0:20]:
    product_id = d['_id']
    category_id = d['category_id'] # This won't be in Test data
    prod_to_category[product_id] = category_id
    for e, pic in enumerate(d['imgs']):
        picture = imread(io.BytesIO(pic['picture']))
        # do something with the picture, etc
        plt.imshow(picture)
        cats = mydict[d['category_id']]
        title = cats[0] + " > " + cats[1] + " > " + cats[2]
        plt.title("\n".join(wrap(title, 40)))
        plt.savefig('out/img-'+str(c) + '-' + str(e) + '.pdf', format='pdf')
