import subprocess
import re

def scan_url(url):
    """ Voert WhatWeb scan uit op de opgegeven URL. """
    result = subprocess.run(["whatweb", url], capture_output=True, text=True)
    return result.stdout

def extract_technologies(scan_result):
    """ Zoek tech & versions uit de WhatWeb-output. """
    matches = re.findall(r'(\w+)/([\d.]+)', scan_result)
    return matches

def search_exploits(tech_versions):
    """ Zoekt naar exploits in Exploit-DB met searchsploit. """
    results = ""
    for tech, version in tech_versions:
        results += f"[+] Zoeken naar exploits voor {tech} {version}...\n"
        search_result = subprocess.run(["searchsploit", f"{tech} {version}"], capture_output=True, text=True)
        results += search_result.stdout + "\n"
    return results

def main():
    url = input("Geef een URL op: ")
    print("[+] Scannen met WhatWeb...")
    scan_result = scan_url(url)
    print(scan_result)
    
    tech_versions = extract_technologies(scan_result)
    if not tech_versions:
        print("[-] Niks bijzonders gevonden")
        return
    
    exploit_results = search_exploits(tech_versions)
    print(exploit_results)

if __name__ == "__main__":
    main()
