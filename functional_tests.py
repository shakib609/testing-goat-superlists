from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about this new to-do app.
        # She goes to check out its home page.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish The TEST')

        # She is invited to insert a to-do item straight away

        # She types "buy peacock feathers" into a text box

        # When she presses "ENTER" the page updates, and now the page lists
        # 1: "buy peacock feathers" as an item in a to-do list

        # There is still another text box inviting her to add another item
        # to the to-do list. She enters "Use Peacock feathers to make a fly"

        # The page updates and now shows both items on her list.

        # Edith wonders whether the site will remember her list. Then she sees
        # the site generated a unique URL for her -- There is some explanatory
        # text to that effect

        # She visits that URL - her to-do list is still there.

        # Satisfied she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
