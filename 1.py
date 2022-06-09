import requests
import random
kn = 0
nk = 0
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[1;32m' #اخضر
A = '\033[2;34m'#ازرق داكن
C = '\033[1;35m' #وردي
B = '\033[1;36m'#سمائي
Y = '\033[1;34m' #ازرق
print(B + 'HUNTING UNDERWAY  ')

k = '855706229'
t = '5442227272:AAGUUhHaqKPh-NumQ95ScRMNt_A-fk93hyM'
message = requests.get(f"https://api.telegram.org/bot{t}/sendMessage?chat_id={k}&text= ⌔ New Start! ").json()
id_msg = str(message['result']["message_id"])
print(X + '- '*15)
oh = 'QAZWSXEDCRFVTGBYHNUJMIKLOP'
op = '0987654321ABCDEFGHIJKLMNOPQRSTUVWXYZ'
no = '1234567890'
aq = '1234567890QAZWSXEDCRFVTGBYHNUJMIKOLP'
aq1 = '_1234567890QAZWSXEDCRFVTGBYHNUJMIKOLP'
s = '_'
Extrra = 1
while True :
    a = ''.join(random.sample(oh, Extrra))
    n = ''.join(random.sample(op, Extrra))
    a1 = ''.join(random.sample(aq, Extrra))
    m = ''.join(random.sample(s, Extrra))
    ln = ''.join(random.sample(no, Extrra))
    aa1 = ''.join(random.sample(aq1, Extrra))
    FF = a + aa1 +  a1 + 'bot'
    NN = a + aa1 + 'bot'
    BB = a + m + n + m + a1
    CC = a + a1 + 'bot'
    DD = a + a1 + a + 'bot'
    AA = a + a + 'bot'
    SS = a + a + a1 + a1 + a + a
    MM = a + n + 'bot'
    LL = a + a + m + a1 + a1
    PP = a + n + m + a + n
    UU = a + n + m + n + a
    QQ = a + a + m + a + aa1
    ZZ = a + a1 + a1 + a1 + a
    XX = a + a1 + a1+ a1 + a1 + a
    VV = a + a + a + a + aa1 + a + a
    II = a + a + a + a1 + a1
    KK = a1 + a1 + a + a + a 
    JJ = a + a1 + a + a + a1 
    HH = a + aa1 + aa1 + a + a
    
    os = (FF, NN, BB, CC, DD, AA, SS, MM, LL, PP, UU, QQ, ZZ, XX, VV, II, KK, JJ, HH)
    os = str(''.join(random.choice(os))) 
    oa = requests.get(f'https://t.me/{os}').text
    if 'tgme_username_link' in oa:
        print(F + f'\r [{kn}] : YES : [{os}]  ')
        kn+=1
        tb = f'https://api.telegram.org/bot{t}/sendMessage?chat_id={k}&text= ⌔ 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴 ✅ : < @{os} >'
        i = requests.post(tb)
    else:
        print(Z + f'\r [{nk}] : NO : [{os}] ')
        nk+=1
        requests.post(f"""https://api.telegram.org/bot{t}/editmessagetext?chat_id={k}&message_id={id_msg}&text= ❖❀～ 𝐑 ࿖ ～❀❖
-------------------------
⌔ user : {os} :
	
⌔️ available {kn} :
⌔ unavailable {nk} :
	
	𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 @E0_88 🌈™
	 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 @HDDDDH 💝
------------------------- """)
