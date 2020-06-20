It is recommended to use virtualenv

python3 -m venv .venv     ---- creaete virtualenv where .venv is name of vierualenv
source .venv/bin/activate ---- activate virtualenv
pip install selenium      -----install selenium library

Clone repositor: git clone https://github.com/testertadek/Logintests.git  
From catalog Logintests/Tests run command: python LoginTest.py


You should get following results:
..
----------------------------------------------------------------------
Ran 2 tests in 20.441s

OK
Test completed

additional comments:

1)Knowing problem on Linux :
Message: 'chromedriver' executable may have wrong permissions.

cd to your working directory
$ chmod 755 chromedriver to allow your program to manipulate it

2)In calalog Logintest, we have chromedrivrer.exe file for Windows and
chromedriver fo Linux.  
This file was for chrome version 83.
If you have any problem download appropriate version of chrome driver from https://chromedriver.chromium.org/downloads
