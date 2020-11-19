import speedtest as st
import influxdb_client
from datetime import datetime


class SpeedcheckResult:

    def __init__(self, date='', upload=0, download=0, ping=0):
        self.upload = upload
        self.download = download
        self.ping = ping
        self.date = date

    def __str__(self):
        return ('Test run on: {}. Download Speed: {}. Upload Speed: {}. Ping: {}').format(self.date, self.download,
                                                                                          self.upload,
                                                                                          self.ping)


def speedcheck():
    print("running download test..")
    s = st.Speedtest()
    dl = s.download()
    ping_dl = s.results.ping
    print(ping_dl)

    print("running upload test..")
    s = st.Speedtest()
    ul = s.upload()
    ping_ul = s.results.ping
    print(ping_ul)

    timestamp = datetime.now().replace(microsecond=0)

    servernames = []
    s.get_servers(servernames)
    ping = s.results.ping

    res = SpeedcheckResult(timestamp, ul, dl, ping)

    print(res)


if __name__ == '__main__':
    test = SpeedcheckResult(str(datetime.now()), 1, 2, 3)
    print(test)

    speedcheck()


class CsvTools:

    def write_header(self, delimiter, path):
        return None
