from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.urls import resolve
import unittest
import time

## 기능 테스트
class A_NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        chrome_path = 'C://Users/young/chromedriver_win32/chromedriver.exe'
        self.browser = webdriver.Chrome(chrome_path)
        self.browser.maximize_window()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # 사용자는 웹사이트를 종료한다.
        self.browser.quit()

    def test_can_register_user_account_and_login(self):
        # 사용자는 chwimi의 회원가입 페이지에 접속한다.
        self.browser.get(self.live_server_url)
        signupBtn = self.browser.find_element_by_class_name('signup')
        signupBtn.click()

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
        time.sleep(1)

        # 사용자는 회원가입 버튼을 클릭한다.
        signupButton = self.browser.find_element_by_class_name('signupBtn')
        signupButton.send_keys(Keys.ENTER)

        time.sleep(1)

        # 사용자는 chwimi의 로그인 페이지에 접속한다.
        loginBtn = self.browser.find_element_by_class_name('login')
        loginBtn.click()

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
        time.sleep(1)

        # 사용자는 로그인 버튼을 클릭한다.
        loginButton = self.browser.find_element_by_class_name('loginBtn')
        loginButton.send_keys(Keys.ENTER)
        
        # 페이지 상단에 Mypage가 표시된다.
        mypage = self.browser.find_element_by_class_name('mypage')
        self.assertTrue(mypage)
        time.sleep(1)

        # 사용자는 취미테스트 목록을 클릭한다.
        testBtn = self.browser.find_element_by_class_name('testBtn')
        testBtn.click()
        time.sleep(1)

        # 취미테스트 시작 버튼을 누른다.
        startBtn = self.browser.find_element_by_class_name('startBtn')
        startBtn.click()
        time.sleep(1)

        # 1번 문항에 대한 응답을 한다. (축구)
        ans_1 = self.browser.find_element_by_class_name('usual-hobby')
        ans_1.send_keys('축구')
        
        nextBtn_1 = self.browser.find_element_by_class_name('nxt_1')
        nextBtn_1.click()
        time.sleep(1)

        # 2번 문항에 대한 응답을 한다. (2)
        ans_2 = self.browser.find_element_by_xpath('/html/body/div[2]/form/div[3]/label')
        ans_2.click()

        nextBtn_2 = self.browser.find_element_by_class_name('nxt_2')
        nextBtn_2.click()
        time.sleep(1)

        # 3번 문항에 대한 응답을 한다. (10)
        ans_3 = self.browser.find_element_by_xpath('/html/body/div[2]/form/div[11]/label')
        ans_3.click()

        nextBtn_3 = self.browser.find_element_by_class_name('nxt_3')
        nextBtn_3.click()
        time.sleep(1)

        # 4번 문항에 대한 응답을 한다. (9)
        ans_4 = self.browser.find_element_by_xpath('/html/body/div[2]/form/div[10]/label')
        ans_4.click()

        nextBtn_4 = self.browser.find_element_by_class_name('nxt_4')
        nextBtn_4.click()
        time.sleep(1)

        # 5번 문항에 대한 응답을 한다. (3)
        ans_5 = self.browser.find_element_by_xpath('/html/body/div[2]/form/div[4]/label')
        ans_5.click()

        nextBtn_5 = self.browser.find_element_by_class_name('nxt_5')
        nextBtn_5.click()
        time.sleep(10)

        # 결과를 확인한다. (감성형)
        returnBtn = self.browser.find_element_by_class_name('goHome')
        returnBtn.click()

        # self.fail('======기능테스트======')

