def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])  # Sort balloons based on end coordinates
    arrows = 1  # Initialize the number of arrows as 1
    end = points[0][1]  # End coordinate of the first balloon

    for i in range(1, len(points)):
        if points[i][0] > end:
            arrows += 1
            end = points[i][1]
        else:
            end = min(end, points[i][1])

    return arrows
