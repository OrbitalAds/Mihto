from mihto import Mihto
regla = "((((((Conversions < 1) and (Ctr > 20)) and (Clicks > 5)) and (ConversionRate < 100 ))) or ( ((Conversions > 0) and (Clicks > 10)) and (ConversionRate > 5)))"

mihto = Mihto({"Conversions": 1,
               "Ctr" : 19,
               "ConversionRate" : 6,
               "Clicks" : 11})

print(eval(regla, {"Conversions": 1,
               "Ctr" : 19,
               "ConversionRate" : 6,
               "Clicks" : 11}))