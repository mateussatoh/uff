ethanolPrice, gasolinePrice, ethanolEfficiency, gasolineEfficiency = list(
    map(float, input().split())
)

ethanolPricePerKm = ethanolPrice / ethanolEfficiency
gasolinePricePerKm = gasolinePrice / gasolineEfficiency

if gasolinePricePerKm <= ethanolPricePerKm:
    print("G")
else:
    print("A")
