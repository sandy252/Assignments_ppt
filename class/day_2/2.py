def merget(arr):
    arr.sort(key = lambda i:i[0])
    output = [arr[0]]
    for start, end in arr[1:]:
        x = output[-1][1]
        if start <= x:
            # output[-1]=[output[-1][0], end]
            output[-1][-1] = max(x,end)
        else:
            output.append([start, end])
    return output

print(merget([[1,3],[2,6],[8,10],[15,18]]))