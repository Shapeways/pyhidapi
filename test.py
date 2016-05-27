import base64
import binascii

__author__ = 'matt'

import hidapi

hidapi.hid_init()

# for dev in hidapi.hid_enumerate():
#     print '------------------------------------------------------------'
#     print dev.description()

dev = hidapi.hid_open(0x1430, 0x0150)
arr = hidapi.hid_read(dev, 1024)
report = ''.join(chr(x) for x in [0x00, 0x00, 0x00, 0x00, 0x08, 0x00])
# num = hidapi.hid_write(dev, report)
print "i don't think we'll get here"
# val = 0
# while (True):
#     arr = hidapi.hid_read(dev, 1024)
#     new_val = arr[1]
#     if new_val is not val:
#         test_one = new_val
#         test_two = hidapi.hid_read(dev, 1024)[1]
#         while test_one is not test_two:
#             test_one = test_two
#             test_two = hidapi.hid_read(dev, 1024)[1]
#         print "Got {}".format(test_two)
#         val = test_two
#         print binascii.hexlify(arr)

# print arr[1]
for val in arr:
    print val