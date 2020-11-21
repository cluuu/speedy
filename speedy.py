import speedtest as st
from influxdb_client import InfluxDBClient
from datetime import datetime


ifuser = "grafana"
ifpass = "1234"
ifdb = speed
ifhost = 127.0.0.1
ifport = 8086
measurement_name = "speed"

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

    def write_to_db(self): 
        body = [
            {
                "measurement": measurement_name,
                "time":self.date,
                "fields": {
                    "download": self.download, 
                    "upload": self.upload, 
                    "ping": self.ping
                }
            }
        ]
        ifclient = influxdb_client()
        ifclient.write_points(body)


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
    res.write_to_db


if __name__ == '__main__':
    test = SpeedcheckResult(str(datetime.now()), 1, 2, 3)
    print(test)

    speedcheck()





class CsvTools:

    def write_header(self, delimiter, path):
        return None
