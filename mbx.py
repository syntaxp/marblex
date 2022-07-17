
import requests , time , threading
from exlorem import ex


class exchangeRate:
    def __init__(self , tokenType) -> None:
        self.BaseuRL = 'https://ninokuni.marblex.io/api/price?tokenType={}'.format(tokenType)
        self.Percent = None
        self.Price = None
        threading.Thread(target=self.getPrice).start()
    def getPrice(self):
        while True:
            try:
                res = requests.get(self.BaseuRL).json()['currencies']['USD']
                ePercent = "{:.2f} %".format( float(res['percentMajor'] + "." + res["percentMinor"]) )

                if "-" not in ePercent:
                    self.Percent = "+" + ePercent
                else:
                    if ePercent == "-0.00 %" :
                        self.Percent = "+0.00 %"
                    else:
                        self.Percent = "{:.2f} %".format( float(res['percentMajor'] + "." + res["percentMinor"]) )
                self.Price  = "{:.2f}".format((float("{:.4f}".format( float(res['priceMajor'] + "." + res["priceMinor"]) )) * ex.USD))
            except:
                pass

            time.sleep(3)


    

NKA = exchangeRate("NKA")
NKT = exchangeRate("NKT")



