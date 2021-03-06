from slot_faker.providers import BaseProvider


class Provider(BaseProvider):

    stocks = {
        'Catalyst Pharmaceuticals': 'CPRX',
        'Alibaba': 'BABA',
        'Amazon': 'AMZN',
        'Sony': 'SNE',
        'Aphria': 'APHA',
        'Alphabet Class A': 'GOOGL',
        'Microsoft': 'MSFT',
        'New Residential Investment': 'NRZ',
        'Plug Power': 'PLUG',
        'Peloton Interactive': 'PTON',
        'Nike': 'NKE',
        'Facebook': 'FB',
        'GM': 'GM',
        'Coca-Cola': 'KO',
        'Uber': 'UBER',
        'Moderna': 'MRNA',
        'Zynga': 'ZNGA',
        'TherapeuticsMD': 'TXMD',
        'Li Auto Inc': 'LI',
        'Johnson & Johnson': 'JNJ',
        'Royal Caribbean Group': 'RCL',
        'Walmart': 'WMT',
        'Draftkings': 'DKNG',
        'AstraZeneca': 'AZN',
        'Penn National Gaming': 'PENN',
        'Snap': 'SNAP',
        'GE': 'GE',
        'Energy Transfer': 'ET',
        'Nokia': 'NOK',
        'British Petroleum': 'BP',
        'Delta Air Lines': 'DAL',
        'Southwest Airlines': 'LUV',
        'Disney': 'DIS',
        'Sirius XM': 'SIRI',
        'Netflix': 'NFLX',
        'NVIDIA': 'NVDA',
        'Bank of America': 'BAC',
        'Apple': 'AAPL',
        'NIO': 'NIO',
        'OrganiGram': 'OGI',
        'Pfizer': 'PFE',
        'Square': 'SQ',
        'ADT': 'ADT',
        'Starbucks': 'SBUX',
        'Zoom': 'ZM',
        'Kosmos Energy': 'KOS',
        'Dave & Buster\'s': 'PLAY',
        'United Airlines': 'UAL',
        'Spirit Airlines': 'SAVE',
        'AMD': 'AMD',
        'Boeing': 'BA',
        'Norwegian Cruise Line': 'NCLH',
        'Halliburton': 'HAL',
        'Hecla Mining': 'HL',
        'AT&T': 'T',
        'JetBlue Airways': 'JBLU',
        'Wells Fargo': 'WFC',
        'Marathon Oil': 'MRO',
        'Inovio': 'INO',
        'Rocket Companies': 'RKT',
        'Tesla': 'TSLA',
        'Cronos Group': 'CRON',
        'Twitter': 'TWTR',
        'Canopy Growth': 'CGC',
        'MGM Resorts': 'MGM',
        'American Airlines': 'AAL',
        'Gap': 'GPS',
        'Ford Motor': 'F',
        'GoPro': 'GPRO',
        'Aurora Cannabis': 'ACB',
        'MFA Financial': 'MFA',
        'Tilray': 'TLRY',
        'Carnival': 'CCL',
        'Exxon Mobil': 'XOM',
        'Coty': 'COTY',
        'Antero Midstream': 'AM',
        'Macy\'s': 'M',
        'AMC Entertainment': 'AMC',
        'Fitbit': 'FIT',
        'Nikola': 'NKLA',
        'Genius Brands': 'GNUS',
        'Prospect Capital': 'PSEC',
        'Direxion Daily S&P Oil & Gas Exp. & Prod. Bull 2X Shares': 'GUSH',
        'Workhorse': 'WKHS',
        'Palantir Technologies': 'PLTR',
        'Invesco Mortgage Capital': 'IVR',
        'Ideanomics': 'IDEX',
        'FuelCell Energy': 'FCEL',
        'ProShares Ultra Bloomberg Crude Oil ETF': 'UCO',
        'United States Oil Fund': 'USO',
        'Vanguard S&P 500 ETF': 'VOO',
        'Airbnb': 'ABNB',
        'SPDR S&P 500 ETF': 'SPY',
        'Sorrento Therapeutics': 'SRNE',
        'Kodak': 'KODK',
        'Electrameccanica Vehicles': 'SOLO',
        'XPeng': 'XPEV',
        'Vaxart': 'VXRT'
    }

    def stock(self):
        return self.random_element(
            [*self.stocks.keys(), *self.stocks.values()]
        )

    def stock_name(self):
        return self.random_element([*self.stocks.keys()])

    def stock_symbol(self):
        return self.stocks.get(self.stock_name())

    def random_dollars(self, min: int = 50, max: int = 10000, step: int = 10):
        amount = self.random_int(min, max, step)
        return f"${amount:.2f}"

    def common_currency(self):
        return self.random_element(
            ('USD', 'GBP', 'Euro', 'JPY', 'AUD')
        )