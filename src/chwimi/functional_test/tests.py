from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

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

        # 사용자는 회원가입 버튼을 클릭한다.
        # 임시 데이터베이스와 연동하기
        pass

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
        # 임시 데이터베이스와 연동하기
        pass

        self.fail('======기능테스트: 로그인======')

