import subprocess
import optparse
import re

#interface : wlp2s0


def get_arguments():
    """
    catch the arguments from the console
    """
    parser = optparse.OptionParser()
    parser.add_option("-i",
                      '--interface',
                      dest="interface",
                      help="Herramienta para cambiar MAC")
    parser.add_option("-m",
                      '--mac',
                      dest="new_mac",
                      help="Nueva direccion Mac")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error[
            "[-]  Please input an interface, use --help for more information"]
    elif not options.new_mac:
        parser.error[
            "[-]  Please input a MAC addres, use --help for more information"]
    return options

def change_mac(interface, new_mac):
    """
    change the mac addres
    """
    print(
        f"[+]  Cambiando Direccion MAC para {options.interface} to {new_mac}")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    """
    catch the mac addres 
    """
    ifconfig_results = subprocess.check_output(['ifconfig', options.interface])
    mac_addres_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w",
                                         ifconfig_results)
    if mac_addres_search_result:
        print(mac_addres_search_result.group(0))
    else:
        print("[-]  An error with the MAC direction")


options = get_arguments()
change_mac(options.interface, options.new_mac)
