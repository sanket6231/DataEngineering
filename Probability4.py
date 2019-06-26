# Sample set to toss a fair coin three times
sample_set = ('HHH', 'HHT', 'HTH', 'THH', 'TTT', 'TTH', 'THT', 'HTT')
total_no_of_occ = len(sample_set)

# a ->
a = sample_set.count('HHH')
p = a/total_no_of_occ
print('probability = {0} / {1} = {2}'.format(a, total_no_of_occ, p))

# b ->
count1 = 0
for item in sample_set:
    if 'H' in item and item.count('H') == 1:
        count1 += 1

p1 = count1/total_no_of_occ
print('probability = {0} / {1} = {2}'.format(count1, total_no_of_occ, p1))

# c ->
count2 = 0
for item in sample_set:
    if 'H' in item and item.count('H') >= 2:
        count2 += 1

p2 = count2/total_no_of_occ

p_total = p1 / p2
print('Probability = p1 / p2 =  {0} / {1} = {2}'.format(p1, p2, p_total))
