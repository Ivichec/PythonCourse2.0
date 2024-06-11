def snail(snail_map):
    if not snail_map or not snail_map[0]:
        return []

    array = []
    while snail_map:
        array.extend(snail_map.pop(0))
        if snail_map and snail_map[0]:
            for row in snail_map:
                array.append(row.pop())
        if snail_map:
            array.extend(snail_map.pop()[::-1])
        if snail_map and snail_map[0]:
            for row in snail_map[::-1]:
                array.append(row.pop(0))

    return array


print(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
