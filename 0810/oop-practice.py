class CurrencyConverter:
    def __init__(self,rate=0.201):
        self.rate=rate

    def twd_to_jpy(self,twd_dollar):
        return twd_dollar / self.rate

    def jpy_to_twd(self, jpy_dollar):
        return jpy_dollar * self.rate

    def convert(self, dollar, mode):
        if mode == '0':
            result = self.twd_to_jpy(dollar)
            print(f'{dollar}台幣大約為{result:.0f}日幣')
        else:
            result = self.jpy_to_twd(dollar)
            print(f'{dollar}日幣大約為{result:.0f}台幣')

    def interactive(self):
        m = input('台幣換算日幣請按0，日幣換算台幣請按1:')
        d = float(input('請輸入金額:'))

        return self.convert(d, m)



c1 = CurrencyConverter()
c1.convert(10000,'0')
c1.convert(10000,'1')
c1.interactive()
