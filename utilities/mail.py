import requests
import re
import json

while True:
    header = {
        "authorization": ""}
    r = requests.get("https://api.mail.tm/messages", headers=header)
    mail_kutusu = r.text
    mail_kutusu = json.loads(mail_kutusu)
    if str(mail_kutusu["hydra:member"]) != "[]":
        id = mail_kutusu["hydra:member"][0]["id"]
        r = requests.get(f"https://api.mail.tm/messages/{id}",headers = header)
        mail = r.text
        mail = json.loads(mail)
        mail_text = mail["text"]
        break

def extract_verification_code(text):
    # 6 haneli tam sayı arıyoruz
    match = re.search(r'\b\d{6}\b', text)
    if match:
        return match.group(0)
    return None

verification_code = extract_verification_code(mail_text)
print(verification_code)


