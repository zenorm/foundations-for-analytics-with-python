empty_dict = {}
a_dict = {"one":1, "two":2, "three":3}
print("output #102:{}".format(a_dict))
print("output #103:a_dict has {!s}elements".format(len(a_dict)))

another_dict = {"x":"printer", "y":5, "z":['star', 'circle', 9]}
print("output #104:{}".format(another_dict))
print("output #105: another_dict also has {!s} elements".format(len(another_dict)))

print("Output #109: {}".format(a_dict.keys()))
a_dict_keys = a_dict.keys()
print("Output #110: {}".format(a_dict_keys))
print("Output #111: {}".format(a_dict.values()))
print("Output #112: {}".format(a_dict.items()))

if 'y' in another_dict:
    print("Output #114: y is a key in another_dict: {}."\
.format(another_dict.keys()))
if 'c' not in another_dict:
    print("Output #115: c is not a key in another_dict: {}."\
.format(another_dict.keys()))
print("Output #116: {!s}".format(a_dict.get('three')))
print("Output #117: {!s}".format(a_dict.get('four')))
print("Output #118: {!s}".format(a_dict.get('four', 'Not in dict')))