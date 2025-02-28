# Case Study Project

# English Documentation

## Overview
This project is a case study implementation that demonstrates modern web development practices using Python and various web technologies. It includes a comprehensive test suite and follows best practices for code organization and maintainability.

## Project Structure
```
├── base/           # Base configurations and core functionality
├── config/         # Configuration files and settings
├── pages/          # Page components and routing
├── tests/          # Test suites and test utilities
├── utilities/      # Helper functions and utility modules
└── requirements.txt # Project dependencies
```

## Prerequisites
- Python 3.x
- Virtual Environment (venv)
- Git

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [project-directory]
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

The project uses environment variables for configuration. These can be set in a `.env` file in the root directory. The following variables are required for testing:

```env
# Browser Settings
BROWSER=chrome
HEADLESS=False

# URL Settings
BASE_URL=....

# Timeout Settings
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20

# Test Data
FIRST_NAME=....
LAST_NAME=....
COUNTRY=....
MOBILE_NUMBER=....
COMPANY=....
EMAIL=....
TITLE=....
PASSWORD=....
CONFIRM_PASSWORD=....
VERIFICATION_CODE=....
```

All configuration values can be found and modified in `config/config.py`. Make sure to update these values according to your test requirements before running the tests.

## Running the Project

1. Activate the virtual environment (if not already activated):
```bash
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Run the application:
```bash
pytest tests/test_register_login.py -v
```

## Running Tests

The project includes automated tests for registration and login functionality. The main test file is `tests/test_register_login.py`.

To run the tests:
```bash
pytest tests/test_register_login.py -v
```

The test suite includes:
- Registration process testing
- Login verification
- Dashboard access verification

Make sure to configure the test data in `config/config.py` or through environment variables before running the tests.

## Project Features
- Modular architecture with clear separation of concerns
- Comprehensive test coverage
- Configuration management
- Utility functions for common operations
- Automated registration and login testing
- Environment-based configuration

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Your Name - hasankucukselek7@gmail.com
Project Link: [https://github.com/hasankselek/selenium-python-case]

---

# Türkçe Dokümantasyon

## Genel Bakış
Bu proje, Python ve çeşitli web teknolojilerini kullanarak modern web geliştirme uygulamalarını gösteren bir vaka çalışması uygulamasıdır. Kapsamlı bir test paketi içerir ve kod organizasyonu ve sürdürülebilirlik için en iyi uygulamaları takip eder.

## Proje Yapısı
```
├── base/           # Temel yapılandırmalar ve çekirdek işlevsellik
├── config/         # Yapılandırma dosyaları ve ayarlar
├── pages/          # Sayfa bileşenleri ve yönlendirme
├── tests/          # Test paketleri ve test yardımcı programları
├── utilities/      # Yardımcı fonksiyonlar ve yardımcı program modülleri
└── requirements.txt # Proje bağımlılıkları
```

## Ön Koşullar
- Python 3.x
- Sanal Ortam (venv)
- Git

## Kurulum

1. Depoyu klonlayın:
```bash
git clone [repository-url]
cd [project-directory]
```

2. Sanal ortamı oluşturun ve etkinleştirin:
```bash
python -m venv venv
source venv/bin/activate  # Windows'ta kullanın: venv\Scripts\activate
```

3. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

## Yapılandırma

Proje, yapılandırma için ortam değişkenlerini kullanır. Bunlar kök dizindeki `.env` dosyasında ayarlanabilir. Test için aşağıdaki değişkenler gereklidir:

```env
# Tarayıcı Ayarları
BROWSER=chrome
HEADLESS=False

# URL Ayarları
BASE_URL=....

# Zaman Aşımı Ayarları
IMPLICIT_WAIT=10
EXPLICIT_WAIT=20

# Test Verileri
FIRST_NAME=....
LAST_NAME=....
COUNTRY=....
MOBILE_NUMBER=....
COMPANY=....
EMAIL=....
TITLE=....
PASSWORD=....
CONFIRM_PASSWORD=....
VERIFICATION_CODE=....
```

Tüm yapılandırma değerleri `config/config.py` dosyasında bulunabilir ve değiştirilebilir. Testleri çalıştırmadan önce bu değerleri test gereksinimlerinize göre güncellediğinizden emin olun.

## Projeyi Çalıştırma

1. Sanal ortamı etkinleştirin (henüz etkinleştirilmediyse):
```bash
source venv/bin/activate  # Windows'ta kullanın: venv\Scripts\activate
```

2. Uygulamayı çalıştırın:
```bash
pytest tests/test_register_login.py -v
```

## Testleri Çalıştırma

Proje, kayıt ve giriş işlevselliği için otomatik testler içerir. Ana test dosyası `tests/test_register_login.py`'dir.

Testleri çalıştırmak için:
```bash
pytest tests/test_register_login.py -v
```

Test paketi şunları içerir:
- Kayıt işlemi testi
- Giriş doğrulama
- Gösterge paneli erişim doğrulama

Testleri çalıştırmadan önce test verilerini `config/config.py` dosyasında veya ortam değişkenleri aracılığıyla yapılandırdığınızdan emin olun.

## Proje Özellikleri
- Net görev ayrımına sahip modüler mimari
- Kapsamlı test kapsamı
- Yapılandırma yönetimi
- Genel işlemler için yardımcı fonksiyonlar
- Otomatik kayıt ve giriş testi
- Ortam tabanlı yapılandırma

## Katkıda Bulunma
1. Depoyu fork'layın
2. Özellik dalınızı oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit'leyin (`git commit -m 'Add some AmazingFeature'`)
4. Dala push'layın (`git push origin feature/AmazingFeature`)
5. Bir Pull Request açın

## Lisans
Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için LICENSE dosyasına bakın.

## İletişim
İsminiz - hasankucukselek7@gmail.com
Proje Bağlantısı: https://github.com/hasankselek/selenium-python-case 