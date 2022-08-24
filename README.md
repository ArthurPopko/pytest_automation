# Web and api automation with pytest.

### Setting up the env:

1. Install [Python](https://www.python.org)
   ```
   check: python3 --version
   ```
2. Configure python env:
   ```
   cd /usr/local/bin
   python3 -m venv ~/venvs/python310
   ```
3. Activate py env:
   ```
   source ~/venvs/python310/bin/activate
   ```
4. Install selenium:
   ```
   pip install selenium
   pip list
   ```
5. Download [chromedriver](https://chromedriver.chromium.org/)
6. Add the webdriver to your PATH environment variable:
   ```
   add a string in: .bashrc, bash_profile, .zshrc or .profile
   e.g.: export PATH=$PATH:~/drivers
   ```
**NOTE: It's highly recommended to use [WebdriverManager](https://pypi.org/project/webdriver-manager/)**
   ```
   # selenium 4
   from selenium import webdriver
   from selenium.webdriver.chrome.service import Service as ChromeService
   from webdriver_manager.chrome import ChromeDriverManager
   
   browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
   ```

### Check the selenium interacts the browser:
   ```
   python3
   from selenium import webdriver
   browser = webdriver.Chrome()
   browser.get('google.com')
   browser.close()
   ```

**Allure integration:**
```
brew install allure
pip install allure-pytest
pytest -v --alluredir reports
allure generate reports --clean && allure open
```

**Install requirements.txt:**
```
pip freeze > requirements.txt - to generate requirements.txt
pip install -r requirements.txt - to install all dependences
``` 