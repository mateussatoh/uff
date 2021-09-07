mariaX, mariaY, locationX, locationY = list(map(int, input().split()))

distanceX = abs(locationX - mariaX)
distanceY = abs(locationY - mariaY)

totalIntersections = totalDistance = distanceX + distanceY

print(totalIntersections)