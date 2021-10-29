rounds = int(input())
brokenGlasses = 0
for round in range(rounds):
   cans, glasses = list(map(int, input().split()))
   if cans > glasses:
      brokenGlasses += glasses
print(brokenGlasses)