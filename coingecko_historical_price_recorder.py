
from time import sleep
import arrow
import numpy
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

tokenId = input("Coingecko token ID: ")
startDate = input("Start Date, Format is dd-mm-yyyy: ")
endDate = input("End Date, Format is dd-mm-yyyy: ")


startDate = arrow.get(startDate, 'DD-MM-YYYY')
endDate = arrow.get(endDate, 'DD-MM-YYYY')
endDate = endDate.shift(days=+1)

# create csv file
csvname = tokenId + ".csv"
f = open(csvname, "w")

while startDate != endDate:
    # fetch price at specific date
    historicalData = cg.get_coin_history_by_id(id=tokenId, date=str(startDate.format('DD-MM-YYYY')),
                                               localization='false')
    historicalPrice = historicalData['market_data']['current_price']['usd']
    historicalPrice = round(historicalPrice, 2)
    # print(historicalPrice)

    historicalMcap = historicalData['market_data']['market_cap']['usd']
    historicalMcap = round(historicalMcap, 2)

    # print(historicalMcap)
    historicalVolume = historicalData['market_data']['total_volume']['usd']
    historicalVolume = round(historicalVolume, 2)
    # print(historicalVolume)

    # create array of date and price
    list_row_append = [[startDate.format('DD-MM-YYYY'), historicalPrice, historicalMcap, historicalVolume]]
    numpy_array_rows_append = numpy.array(list_row_append)
    with open(csvname, 'a') as csvfile:
        numpy.savetxt(csvfile, numpy_array_rows_append, delimiter=',', fmt='%s')

    print(startDate)
    startDate = startDate.shift(days=+1)
    sleep(1.4)


