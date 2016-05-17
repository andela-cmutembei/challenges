original_string = list(raw_input())
sub_string = list(raw_input())
count = 0
indexes = [i for i, x in enumerate(original_string) if x == sub_string[0]]
for i in range(0, len(indexes)):
    if sub_string == original_string[indexes[i]: indexes[i] + len(sub_string)]:
        count += 1
print count
