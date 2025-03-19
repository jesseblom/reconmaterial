import subprocess
import re

def scan_url(url):
    """ Run Whatweb on the specified URL """
    result = subprocess.run(["whatweb", url], capture_output=True, text=True)
    return result.stdout

def extract_technologies(scan_result):
    """ Search all software, tech and versions WhatWeb-output. """
    matches = re.findall(r'(\w+)/([\d.]+)', scan_result)
    return matches

def search_exploits(tech_versions):
    """ Search for exploits in the Exploit-DB with searchsploit. """
    results = ""
    for tech, version in tech_versions:
        results += f"[+] Searching for exploits for.. {tech} {version}...\n"
        search_result = subprocess.run(["searchsploit", "-w", f"{tech} {version}"], capture_output=True, text=True)
        results += search_result.stdout + "\n"
    return results

def main():
    url = input("What URL are we scanning: ")
    print("[+] Scanning WhatWeb...")
    scan_result = scan_url(url)
    print(scan_result)
    
    tech_versions = extract_technologies(scan_result)
    if not tech_versions:
        print("[-] Nothing out of the ordinary found, unfortunate :()")
        return
    
    exploit_results = search_exploits(tech_versions)
    print(exploit_results)

if __name__ == "__main__":
    main()
