
import requests , time , threading

class _exchanger:
    def __init__(self) -> None:
        self.BaseuRL = 'https://api.loremboard.finance/api/v1/dashboard/fiat/latest'
        self.USD = None
        threading.Thread(target=self.GetRate).start()
    def GetRate(self):
        while True:
            try:
                res = requests.get(self.BaseuRL).json()
                self.USD = res['rates']['THB']
            except:
                pass

            time.sleep(15)


ex = _exchanger()
            