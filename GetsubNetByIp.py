# pip install ipwhois
from ipwhois import IPWhois

def get_ip_info(ip):
    try:
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        print(f"IP Address: {ip}")
        print("Whois Data:")
        for key, value in results.items():
            if isinstance(value, dict):
                print(f"{key}:")
                for sub_key, sub_value in value.items():
                    print(f"  {sub_key}: {sub_value}")
            else:
                print(f"{key}: {value}")
    except Exception as e:
        print(f"Error fetching information for {ip}: {e}")

if __name__ == "__main__":
    ip_address = "1.13.20.177"
    get_ip_info(ip_address)
