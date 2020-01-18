import gzip
from collections import defaultdict
import scipy
import scipy.optimize
import numpy
import random

path = "amazon_reviews_us_Video_Games_v1_00.tsv.gz"
f = gzip.open(path, 'rt', encoding = "utf-8")

header = f.readline()
header = header.strip().split('\t')

dataset = []
for line in f:
    fields = line.strip().split('\t')
    d = dict(zip(header, fields))
    d['star_rating'] = int(d['star_rating'])
    d['helpful_votes'] = int(d['helpful_votes'])
    d['total_votes'] = int(d['total_votes'])
    dataset.append(d)

print(dataset[0])