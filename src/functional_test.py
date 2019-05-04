from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        chrome_path = 'C://Users/young/chromedriver_win32/chromedriver.exe'
        self.browser = webdriver.Chrome(chrome_path)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # 사용자는 웹사이트를 종료한다.
        self.browser.quit()

    def test_can_move_to_signup_page(self):
        # 사용자는 chwimi에 접속한다.
        self.browser.get('http://localhost:8000')

        # 웹 사이트의 제목이 'Chwimi'를 표시한다.
        self.assertIn('Chwimi', self.browser.title)

        self.fail('======기능테스트======')

if __name__ == "__main__":
    unittest.main(warnings='ignore')