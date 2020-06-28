#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from sys import platform
from traceback import print_exc
from os.path import dirname, abspath

LINUXPATH = dirname(abspath(__file__))  + "/drivers/chromedriver"
WINPATH = ""
URL = "https://tuimac.signin.aws.amazon.com/console"
LOG = dirname(abspath(__file__))  + "/logs/webdriver.log"

def main():
    try:
        with open(LOG, "w") as f:
            f.write("")
        driver = ""
        if platform == "linux":
            driver = Chrome(
                executable_path = LINUXPATH,
                service_args = [
                    "--verbose", 
                    "--log-path=" + LOG
                ]
            )
        elif platform == "win32":
            #driver = webdriver.Chrome(WINPATH)
            pass
        else:
            raise OSError("Unexpected platform")
        driver.get(URL)
        timeout = 10
        logo = expected_conditions.presence_of_element_located((By.ID, 'logo_id'))
        WebDriverWait(driver, timeout).until(logo)
    except TimeoutException as e:
        print_exc()
    except OSError as e:
        print_exc()
    except:
        print_exc()

if __name__ == "__main__":
    main()
