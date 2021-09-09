dummy, height = list(map(int, input().split()))
pins = list(map(int, input().split()))
movements = 0

for index, pin in enumerate(pins):
   if index < len(pins) - 1:
      diff = height - pin
      pins[index + 1] += diff
      pin = height
      movements += abs(diff)

print(movements)
