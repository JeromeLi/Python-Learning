import json
import requests
import humanfriendly
import time

# units = {"B": 1, "KB": 10 ** 3, "MB": 10 ** 6, "GB": 10 ** 9, "TB": 10 ** 12}


# def parseSize(size):
#     number, unit = [string.strip() for string in size.split()]
#     return int(float(number) * units[unit])


def percentage(part, whole):
    return 100 * float(part) / float(whole)

def get_vps_data():
    url = "https://api.64clouds.com/v1/getServiceInfo?veid=1493802&api_key=private_OCAqy9mhEUvgiCtMGTAz2lt5"
    json_data = requests.get(url)
    data = json_data.json()
    return data

vps_data = get_vps_data()
class Vps():
    def __init__(self, vps_id, vps_data):
        self.vps_id = vps_id
        self.vps_data = vps_data
    def location(self):
        print(str(self.vps_id) + '\'s ' + "VPS Location:", vps_data.get("node_datacenter"))
    def ip(self):
        ip_str = "".join(vps_data.get("ip_addresses"))
        print("IP:", ip_str)
    def usaged(self):
        monthly_data_plan = humanfriendly.format_size(vps_data.get("plan_monthly_data"))
        monthly_data_used = humanfriendly.format_size(vps_data.get("data_counter"))
        print(
            str(self.vps_id) + '\'s Data Usaged Status:'
            "\nMonthly Data Plan --> ",
            monthly_data_plan,
            "\nMonthly Data Used --> ",
            monthly_data_used,
            "\nData Usage -->",
            "%" + "%.1f" % percentage(vps_data.get("data_counter"), vps_data.get("plan_monthly_data")),
        )
    def date(self):
        reset_date = time.gmtime(vps_data.get("data_next_reset"))
        reset_date = time.strftime("%Y-%b-%d %a", reset_date)
        print("Reset Date:", reset_date)
    def info(self):
        self.location()
        self.ip()
        self.usaged()
        self.date()

jerome = Vps('Jerome', vps_data)
rfid = Vps('Rfid', vps_data)
jerome.location()
rfid.usaged()
# jerome.ip()
# jerome.data()
jerome.info()

