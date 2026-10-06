def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    
    if len(a[0]) != len(b):
        return -1

    c = []

    for row in range(len(a)):
        new_row = []

        for column in range(len(b[0])):
            total = 0

            for k in range(len(b)):
                total += a[row][k] * b[k][column]

            new_row.append(total)
        c.append(new_row)
    return c