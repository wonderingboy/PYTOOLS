import sys
import numpy as np
import lmdb
import caffe 
#lmdbpath = '/media/data/hc/COCOVOC/lmdb/COCOVOC_test_lmdb'
lmdbpath = 'mylmdb'
env = lmdb.open(lmdbpath, readonly=True)
with env.begin() as txn:
    cursor = txn.cursor()
    for key, value in cursor:
        print 'key: ',key
        datum = caffe.proto.caffe_pb2.Datum()
        datum.ParseFromString(value)
        flat_x = np.fromstring(datum.data, dtype=np.uint8)
        x = flat_x.reshape(datum.channels, datum.height, datum.width)
        y = datum.label
        print 'x: ',x
        print 'y: ',y

