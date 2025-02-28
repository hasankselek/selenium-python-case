import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    # Browser ayarları
    BROWSER = os.getenv('BROWSER', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'

    # URL ayarları
    BASE_URL = os.getenv('BASE_URL', 'https://app.forceget.com/system/account')

    # Timeout ayarları
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', 10))
    EXPLICIT_WAIT = int(os.getenv('EXPLICIT_WAIT', 20))

    # Test data
    FIRST_NAME = os.getenv('FIRST_NAME', 'JOHN')
    LAST_NAME = os.getenv('LAST_NAME', 'DOE')
    COUNTRY = os.getenv('COUNTRY', '+90')
    MOBILE_NUMBER = os.getenv('MOBILE_NUMBER', '5555555555')
    COMPANY = os.getenv('COMPANY', 'AMAZON')
    EMAIL = os.getenv('EMAIL', 'testtttt@test.com')
    TITLE = os.getenv('TITLE', 'CEO')
    PASSWORD = os.getenv('PASSWORD', 'Test123!')
    CONFIRM_PASSWORD = os.getenv('CONFIRM_PASSWORD', 'Test123!')
    VERIFICATION_CODE = os.getenv('VERIFICATION_CODE','401128')