import subprocess
import socket
from mailer import MailObject
from settings import settings
import time

class ServerInfo(object):
    def __init__(self):
        self.hostname = self._get_hostname()
        self.ip = self._get_outgoing_ip()
        self.cpu_temp = self._get_cpu_temp()
        self.now = self._get_current_datetime()

    def _get_hostname(self):
        p1 = subprocess.Popen(["hostname"], stdout=subprocess.PIPE)
        out1 = p1.communicate()[0]
        return out1.strip()

    def _get_outgoing_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception as err:
            print("Error getting external ip: {0}".format(str(err)))
            return "Unknown"

    def _get_cpu_temp(self):
        try:
            fp = open('/sys/class/thermal/thermal_zone0/temp', 'r')
            a = fp.read()
            fp.close()
            t = float(int(a.strip())/1000.0)
            return t
        except Exception as err:
            print("Failed to retrieve CPU Temperature: {0}".format(str(err)))
            return "Unknown"

    def _get_current_datetime(self):
        timezone = time.strftime("%z")
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return "{0} {1}".format(now, timezone)


def get_usage(device_name):
    try:
        p = subprocess.Popen(["df", device_name], stdout=subprocess.PIPE)
        output = p.communicate()[0]
        device, size, used, available, percent, mountpoint = output.split('\n')[1].split()
        return device, size, used, available, percent, mountpoint
    except Exception as err:
        print("An error occurred: {0}".format(str(err)))
        return None

def check_usage(devices, threshold):
    for disk in devices:
        disk_usage = get_usage(disk)
        if disk_usage[4][:-1] >= threshold:
            generate_alarm()
            return

def generate_alarm():
    p = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    output = p.communicate()[0]

    info = ServerInfo()

    a = settings()
    subject = "Veriteknik - Disk Usage Alert"
    msg = """
    <h2>Disk usage report</h2>
    <pre>
    Server Time: <b>{now}</b>
    Threshold: <b>%{thres}</b>
    Hostname: <b>{hostname}</b>
    External IP Address: <b>{ip}</b>
    CPU Temperature: <b>{cpu_temp}</b> Celsius
    -----------------------------------
    
    
    {df}
    </pre>

    """.format(thres=a.threshold, df=output, hostname=info.hostname, ip=info.ip, cpu_temp=info.cpu_temp, now=info.now)

    msg = msg.replace("\n", "<br>")

    mail = MailObject(a.hostname, a.sender, a.receivers, subject, msg, a.port, a.username, a.password)