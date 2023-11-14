nested_list = [[1, 2], [3, 4], ["a", "b"]]
flattened_list = []

for item in nested_list:
    if isinstance(item, list):
        for nested_item in item:
            flattened_list.append(nested_item)
    else:
        flattened_list.append(item)
print(flattened_list)
