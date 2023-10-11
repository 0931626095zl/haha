import re
import requests
import threading

urls = '''
https://proxy.webshare.io/proxy/list/download/gyluvedzkfglbcvodfzabxppxsoldvnbgqdvkhzm/-/http/port/direct/
https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt
http://globalproxies.blogspot.com/
http://biskutliat.blogspot.com/
http://alexa.lr2b.com/proxylist.txt
http://vipprox.blogspot.com/2013_03_01_archive.html
http://browse.feedreader.com/c/Proxy_Server_List-1/449196260
http://browse.feedreader.com/c/Proxy_Server_List-1/449196258
http://sock5us.blogspot.com/2013/06/01-07-13-free-proxy-server-list.html#comment-form
http://browse.feedreader.com/c/Proxy_Server_List-1/449196251
http://free-ssh.blogspot.com/feeds/posts/default
http://browse.feedreader.com/c/Proxy_Server_List-1/449196259
http://proxyfirenet.blogspot.com/
https://www.javatpoint.com/proxy-server-list
https://openproxy.space/list/http
http://proxydb.net/
https://raw.githubusercontent.com/ItzRazvyy/ProxyList/main/http.txt
https://raw.githubusercontent.com/ItzRazvyy/ProxyList/main/https.txt
https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt
https://raw.githubusercontent.com/Natthanon823/steam-account-checker/main/http.txt
http://olaf4snow.com/public/proxy.txt
https://openproxy.space/list/socks4
https://openproxy.space/list/socks5
http://atomintersoft.com/transparent_proxy_list
http://atomintersoft.com/anonymous_proxy_list
http://atomintersoft.com/high_anonymity_elite_proxy_list
http://atomintersoft.com/products/alive-proxy/proxy-list/3128
http://atomintersoft.com/products/alive-proxy/proxy-list/com
http://atomintersoft.com/products/alive-proxy/proxy-list/high-anonymity/
http://atomintersoft.com/products/alive-proxy/socks5-list
http://atomintersoft.com/proxy_list_domain_com
http://atomintersoft.com/proxy_list_domain_edu
http://atomintersoft.com/proxy_list_domain_net
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt
http://atomintersoft.com/proxy_list_domain_org
http://atomintersoft.com/proxy_list_port_3128
http://atomintersoft.com/proxy_list_port_80
http://atomintersoft.com/proxy_list_port_8000
http://atomintersoft.com/proxy_list_port_81
http://hack-hack.chat.ru/proxy/allproxy.txt
https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt
http://hack-hack.chat.ru/proxy/anon.txt
http://hack-hack.chat.ru/proxy/p1.txt
http://hack-hack.chat.ru/proxy/p2.txt
http://hack-hack.chat.ru/proxy/p3.txt
http://hack-hack.chat.ru/proxy/p4.txt
https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt
https://free-proxy-list.net/
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt
https://www.us-proxy.org/
https://free-proxy-list.com/
https://sunny9577.github.io/proxy-scraper/proxies.txt
https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all
https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all
https://spys.one/
https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt
https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all
http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http
https://api.proxyscrape.com/v2/?request=getproxies&protocol=http
https://openproxylist.xyz/http.txt
https://proxyspace.pro/http.txt
https://proxyspace.pro/https.txt
https://raw.githubusercontent.com/almroot/proxylist/master/list.txt
https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt
https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt
https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/http.txt
https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/https.txt
https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt
https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt
https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt
https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt
https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt
https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt
https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt
https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt
https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt
https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxy-list/data.txt
https://raw.githubusercontent.com/Zaeem20/FREE_PROXY_LIST/master/http.txt
https://raw.githubusercontent.com/Zaeem20/FREE_PROXY_LIST/master/https.txt
https://rootjazz.com/proxies/proxies.txt
https://sheesh.rip/http.txt
https://spys.me/proxy.txt
https://www.freeproxychecker.com/result/http_proxies.txt
https://www.proxy-list.download/api/v1/get?type=http
https://www.proxy-list.download/api/v1/get?type=https
https://www.proxyscan.io/download?type=http
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt
https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt
https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt
https://proxy-spider.com/api/proxies.example.txt
https://multiproxy.org/txt_all/proxy.txt
http://rootjazz.com/proxies/proxies.txt
https://raw.githubusercontent.com/clarketm/proxy
http://k2ysarchive.xyz/proxy/http.txt
http://proxysearcher.sourceforge.net/Proxy%20List.php?type=socks
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4
https://openproxylist.xyz/socks4.txt
https://proxyspace.pro/socks4.txt
https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt
https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/socks4.txt
https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt
https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt
https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt
https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt
https://raw.githubusercontent.com/Zaeem20/FREE_PROXY_LIST/master/socks4.txt
https://spys.me/socks.txt
https://www.freeproxychecker.com/result/socks4_proxies.txt
https://www.proxy-list.download/api/v1/get?type=socks4
https://www.proxyscan.io/download?type=socks4
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5
https://openproxylist.xyz/socks5.txt
https://proxyspace.pro/socks5.txt
https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt
https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/socks5.txt
https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt
https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt
https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt
https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt
https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt
https://raw.githubusercontent.com/Zaeem20/FREE_PROXY_LIST/master/socks5.txt
https://www.freeproxychecker.com/result/socks5_proxies.txt
https://www.proxy-list.download/api/v1/get?type=socks5
https://www.proxyscan.io/download?type=socks5
https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt
https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt
https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt
https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt
https://github.com/ShiftyTR/Proxy-List/blob/master/socks5.txt
https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/all.txt
https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt
https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt
https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt
https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt
https://raw.githubusercontent.com/ProxyListt/PROXY-list/main/http.txt
https://raw.githubusercontent.com/ProxyListt/PROXY-list/main/socks4.txt
https://raw.githubusercontent.com/ProxyListt/PROXY-list/main/socks5.txt
https://raw.githubusercontent.com/ProxyListt/PROXY-list/main/spesial50k.txt
https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/http.txt
https://free-proxy-list.net
http://proxydb.net/?protocol=http
http://proxydb.net/?protocol=https
http://proxydb.net/?protocol=socks4
http://proxydb.net/?protocol=socks5
https://premiumproxy.net/
https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all
https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all
https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all
https://www.proxy-list.download/HTTP
https://www.proxy-list.download/HTTPS
https://www.proxy-list.download/SOCKS4
https://www.proxy-list.download/SOCKS5
https://www.freeproxy.world/
https://smallseotools.com/de/free-proxy-list/
https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt
https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt
https://www.proxyscan.io/download?type=https
https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks4.txt
https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt
https://raw.githubusercontent.com/RX4096/proxy-list/main/online/socks5.txt
https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt
'''


file = open('proxy.txt', 'w')
file.close()
file = open('proxy.txt', 'a')
good_proxies = list()


def pattern_one(url):
    ip_port = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}:\d{2,5})', url)
    if not ip_port: pattern_two(url)
    else:
        for i in ip_port:
            file.write(str(i) + '\n')
            good_proxies.append(i)


def pattern_two(url):
    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
    port = re.findall('td>(\d{2,5})<', url)
    if not ip or not port: pattern_three(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_three(url):
    ip = re.findall('>\n[\s]+(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
    port = re.findall('>\n[\s]+(\d{2,5})\n', url)
    if not ip or not port: pattern_four(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_four(url):
    ip = re.findall('>(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})<', url)
    port = re.findall('>(\d{2,5})<', url)
    if not ip or not port: pattern_five(url)
    else:
        for i in range(len(ip)):
            file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
            good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def pattern_five(url):
    ip = re.findall('(\d{,3}\.\d{,3}\.\d{,3}\.\d{,3})', url)
    port = re.findall('(\d{2,5})', url)
    for i in range(len(ip)):
        file.write(str(ip[i]) + ':' + str(port[i]) + '\n')
        good_proxies.append(str(ip[i]) + ':' + str(port[i]))


def start(url):
    try:
        req = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}).text
        pattern_one(req)
        print(f' [+] Scrapping from: {url}')
    except requests.exceptions.SSLError: print(str(url) + ' [x] SSL Error')
    except: print(str(url) + ' [x] Random Error')


threads = list()
for url in urls.splitlines():
    if url:
        x = threading.Thread(target=start, args=(url, ))
        x.start()
        threads.append(x)


for th in threads:
    th.join()
