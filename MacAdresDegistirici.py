import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-m", "--mac", dest="mac_address", help="Yapmak istediğiniz mac adresini giriniz")
parser.add_option("-i", "--interface", dest="interface", help="İnternet arayüzünüzü giriniz")

def mac_degistirici(interface, mac_address):
    subprocess.call(["ifconfig", "eth0", "down"])
    subprocess.call(["ifconfig", "eth0", "hw", "ether", "44:ee:bc:6c:76:ba"])
    subprocess.call(["ifconfig", "eth0", "up"])

mac_degistirici(interface, mac_address)
