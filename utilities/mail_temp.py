import requests
import re
import time

class MailTmHelper:
    def __init__(self, token):
        self.base_url = "https://api.mail.tm"
        self.headers = {
            "authorization": f"Bearer {token}"
        }

    def extract_verification_code(self, text):
        match = re.search(r'\b\d{6}\b', text)
        if match:
            return match.group(0)
        return None

    def get_verification_code(self):
        while True:

            response = requests.get(f"{self.base_url}/messages", headers=self.headers)
            mail_kutusu = response.json()

            if mail_kutusu["hydra:member"]:
                message_id = mail_kutusu["hydra:member"][0]["id"]
                response = requests.get(f"{self.base_url}/messages/{message_id}", headers=self.headers)
                mail = response.json()
                mail_text = mail.get("text", "")
                code = self.extract_verification_code(mail_text)
                if code:
                    return code
            time.sleep(5)


'''
kullanım
if __name__ == "__main__":
    token = ""
    mail_helper = MailTmHelper(token)
    verification_code = mail_helper.get_verification_code()
    print("Doğrulama kodu:", verification_code)
    '''''

