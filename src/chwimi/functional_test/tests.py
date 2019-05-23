from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.urls import resolve
import unittest
import time

## 기능 테스트
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        chrome_path = 'C://Users/young/chromedriver_win32/chromedriver.exe'
        self.browser = webdriver.Chrome(chrome_path)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # 사용자는 웹사이트를 종료한다.
        self.browser.quit()

    def test_can_register_user_account(self):
        # 사용자는 chwimi의 회원가입 페이지에 접속한다.
        self.browser.get('http://localhost:8000/account/signup')
        # self.browser.get(self.live_server_url)

        # 웹 사이트의 제목이 'Chwimi'를 표시한다.
        self.assertIn('Chwimi', self.browser.title)

        # 사용자는 회원 가입을 하기로 한다.
        
        # 사용자는 아이디 란에 'helloworld'를 입력한다.
        inputbox_id = self.browser.find_element_by_class_name('userid')
        self.assertEqual(
            inputbox_id.get_attribute('placeholder'),
            '아이디'
        )
        inputbox_id.send_keys('helloworld')
        
        # 사용자는 비밀번호 란에 '1234k5678'을 입력한다.
        inputbox_pw = self.browser.find_element_by_class_name('password')
        self.assertEqual(
            inputbox_pw.get_attribute('placeholder'),
            '비밀번호'
        )
        inputbox_pw.send_keys('1234k5678')

        # 사용자는 비밀번호 확인 란에 '1234k5678'을 입력한다.
        inputbox_pw_check = self.browser.find_element_by_class_name('password_check')
        self.assertEqual(
            inputbox_pw_check.get_attribute('placeholder'),
            '비밀번호 확인'
        )
        inputbox_pw_check.send_keys('1234k5678')

        # 사용자는 이메일 란에 'helloworld@gmail.com'을 입력한다'
        inputbox_email = self.browser.find_element_by_class_name('email')
        self.assertEqual(
            inputbox_email.get_attribute('placeholder'),
            '이메일'
        )
        inputbox_email.send_keys('helloworld@gmail.com')
        
        # 사용자는 회원가입 버튼을 클릭한다.
        signupButton = self.browser.find_element_by_class_name('signupBtn')
        signupButton.send_keys(Keys.ENTER)

        # 페이지 상단에 Mypage가 표시된다.
        ## todo: selenium으로 받아온 정보 text 출력하기
        menus = self.browser.find_elements_by_class_name('nav-item')
        self.assertTrue(menus)
        time.sleep(10)
        self.assertTrue(any(menu.text == 'Mypage' for menu in menus),)

        self.fail('======기능테스트: 회원가입======')

class AccessTest(unittest.TestCase):
    def setUp(self):
        chrome_path = 'C://Users/young/chromedriver_win32/chromedriver.exe'
        self.browser = webdriver.Chrome(chrome_path)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # 사용자는 웹사이트를 종료한다.
        self.browser.quit()

    def test_can_access_to_service(self):
        # 사용자는 chwimi의 로그인 페이지에 접속한다.
        self.browser.get('http://localhost:8000/account/login')

        # 웹 사이트의 제목이 'Chwimi'를 표시한다.
        self.assertIn('Chwimi', self.browser.title)

        # 사용자는 회원 가입을 하기로 한다.
        # 사용자는 아이디 란에 'helloworld'를 입력한다.
        inputbox_id = self.browser.find_element_by_class_name('userid')
        self.assertEqual(
            inputbox_id.get_attribute('placeholder'),
            '아이디'
        )
        inputbox_id.send_keys('helloworld')
        
        # 사용자는 비밀번호 란에 '1234k5678'을 입력한다.
        inputbox_pw = self.browser.find_element_by_class_name('password')
        self.assertEqual(
            inputbox_pw.get_attribute('placeholder'),
            '비밀번호'
        )
        inputbox_pw.send_keys('1234k5678')

        # 사용자는 로그인 버튼을 클릭한다.
        loginButton = self.browser.find_element_by_class_name('loginBtn')
        loginButton.send_keys(Keys.ENTER)
        
        # 임시 데이터베이스와 연동하기
        pass

        self.fail('======기능테스트: 로그인======')

