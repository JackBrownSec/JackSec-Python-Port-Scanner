# IMPORTS
import socket
from concurrent.futures import ThreadPoolExecutor


# ANSI COLOR
GREEN = "\033[92m"
RESET = "\033[0m"


# ASCII ART 
ASCII_ART = f"""{GREEN}
                 _\\@)_       ___               ▄▄▄██▀▀▀▄▄▄       ▄████▄   ██ ▄█▀     ██████ ▓█████  ▄████▄  
                  /`\\      .' -,'-.__,@         ▒██  ▒████▄    ▒██▀ ▀█   ██▄█▒    ▒██    ▒ ▓█   ▀ ▒██▀ ▀█  
                 /        |     `).- '           ░██  ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ░ ▓██▄   ▒███   ▒▓█    ▄ 
               _/       _\\V^V^V^V/_          ▓██▄██▓ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄      ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
              | /\\     .=// ^.^ \\\\=.           ▓███▒   ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄   ▒██████▒▒░▒████▒▒ ▓███▀ ░
              /\\ /     .'/| ._. |\\'.           ▒▓▒▒░   ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
             / /-`.       _\\___/_               ▒ ░▒░    ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░   ░ ░▒  ░ ░ ░ ░  ░  ░  ▒   
              |/\\/\\   _@->`   _  `<-@._         ░ ░ ░    ░   ▒   ░        ░ ░░ ░    ░  ░  ░     ░   ░        
                \\  \\.'  @-'`\\( `'-,@   '-.     ░   ░        ░  ░░ ░      ░  ░            ░     ░  ░░ ░      
                 \\      ,    @    , _.-   `\\                      ░                                  ░        
                  \\   .'|    :    |` /'. _.'                                                    
                   `\"`   \\   :    / /`\\_|  @                                                    
                   @_  _.'`\"\"\"\"\"\"`'-\\_\\.--;`                                                    
                   `-.`      /,     `, .-'                                                    
                   _.@--; .-'| '. ;-._;@                                                    
                 .'     @' _.'.  `@  \\                                                    
                |     _.-'`    '-.    \\                                                    
                 '-._  `-._n_     )   |                                                    
                     `'-._ ) `-,.'   /                                                    
                          u-'--;`@ .'                                                    
                               |  /                                                    
                              ,\\ /,                                                    
                              )\\.'/                                                    
                             /   (                                                    
                             \\_.. '._.@                                                    
                                 `-.-'
{RESET}
"""


# CLASS
class port_scanner:
    """This will be a class that can perform TCP Port Scan"""

    @staticmethod
    def port_scanner(target, port):
        """This will scan TCP Ports"""

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)

                result = s.connect_ex((target, port))

                if result == 0:
                    print(f"Port: {port} is Open")

                elif result in (10060, 113):
                    print(f"Port: {port} is Filtered")

                else:
                    print(f"Port: {port} is Closed")

        except Exception as e:
            print(f"Exception Error: {e}")

    @staticmethod
    def threader(target, thread_count=500):
        """Creates multiple threads for parallel scanning"""

        ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 995, 3389]
        portz = range(1,1024)
        portzz = range(1,65535)

        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            for port in portz:
                executor.submit(port_scanner.port_scanner, target, port)

        print("Port scan Successfully Completed!")


def main():
    print(ASCII_ART)
    choice = input("Enter Target Domain: ").strip().lower()
    target = socket.gethostbyname(choice)
    port_scanner.threader(target)


# RUN MAIN LOGIC
if __name__ == "__main__":
    main()

