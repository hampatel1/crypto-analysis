import pandas_datareader as web
import datetime as dt
import matplotlib.pyplot as plt


class CRYPTO_DATA:

    def __init__(self, crypto_lst, start_date, end_date):
        """
        plot of crypto prices
        :param crypto_lst: list of crypto currencies
        :param start_date: start of data points
        :param end_date: end of data points
        """
        self.currency = "USD"
        self.metric = "Close"
        self.crypto_lst = crypto_lst
        self.start = start_date
        self.end = end_date

        self.get_data()
        self.get_plot()

    def get_data(self):
        """
        get data to plot later
        :return: df with crypto prices
        """
        col_names = []
        first = True

        for ticker in self.crypto_lst:
            data = web.DataReader(f"{ticker}-{self.currency}", "yahoo", self.start, self.end)
            if first:
                self.combined = data[[self.metric]].copy()
                col_names.append(ticker)
                self.combined.columns = col_names
                first = False
            else:
                self.combined = self.combined.join(data[self.metric])
                col_names.append(ticker)
                self.combined.columns = col_names

    def get_plot(self):
        """
        get plot of crypto
        :return:
        """
        self.combined.plot(subplots=True)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    crypto_plot = CRYPTO_DATA(['BTC', 'ETH'], dt.datetime(2021, 1, 1), dt.datetime.now())

print()
