def in_array(array1, array2):
    result = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and a1 not in result:
                result.append(a1)
    return sorted(result)
array1 = ["arp", "live", "strong"]
array2 = ["lively", "alive", "harp", "sharp", "armstrong"]
result = in_array(array1, array2)
print(result)