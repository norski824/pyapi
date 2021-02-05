#!/usr/bin/env python3
vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp']

print("Currently the value of vendor:", vendors)
print()
print("\nThe results of the sorted() function:", sorted(vendors))
print()
print("\nBut the value of the list hasn't actually changed:", vendors)
print()



sortedvendors = sorted(vendors)

print('Our sorted vendor list looks like this: ' + str(sortedvendors))
print()
baksortvendors = sorted(vendors, reverse=True)


print('Our sorted vendor list looks like this: ', baksortvendors)
print()



vendorsdeux = ['CISCO', 'JUNIPER', 'cisco', 'juniper', 'BIG_IP', 'big_ip', \
'f5', 'arista', 'HP', 'F5', 'hp', 'ARISTA']

print('Our new vendordeux list looks like this: ', vendorsdeux)
print()

print('Our sorted vendor list looks like this: ', sorted(vendorsdeux))
print()


