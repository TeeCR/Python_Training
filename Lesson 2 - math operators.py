bill_month_1 = 23.0
bill_month_2 = 32.0
bill_month_3 = 64.0

mean_bill = bill_month_1 + bill_month_2 + bill_month_3

print (mean_bill / 3)

tiles = 6
floorPt1 = 7.0 * 9.0
floorPt2 = 7.0 * 5.0

noOfTilesNeededP1 = float(floorPt1 / tiles)

print (noOfTilesNeededP1, " tiles will be required for the first part of the floor")

NoOfTilesNeededP2 = float(floorPt2 / tiles)

print (NoOfTilesNeededP2, " tile will be required for the second part of the floor")

TotalTilesRequired = NoOfTilesNeededP2 + noOfTilesNeededP1

print (TotalTilesRequired, "tiles are required for the whole floor")

TilesPurchased = (tiles * 17) - TotalTilesRequired

print ("A pack of 17 tiles is: ", tiles * 17, " and ", TilesPurchased, " tile will be left after floor renovation")

# noOfTilesNeededP1 = float(floorPt1/tiles)
# noOfTilesNeededP2 = float(floorPt2/tiles)
#
# TilesNeeded = noOfTilesNeededP1 + noOfTilesNeededP2
# print (TilesNeeded)
#
# tilePack = 17*6
#
# print (tilePack - TilesNeeded) //Code is correct but written inefficient

print(7 * 9 + 7 * 5)

print((17 * 6) - (7 * 9 + 7 * 5))
