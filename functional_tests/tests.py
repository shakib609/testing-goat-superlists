from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

import time


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about this new to-do app.
        # She goes to check out its home page.
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to insert a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she presses "ENTER" the page updates, and now the page lists
        # 1: "buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still another text box inviting her to add another item
        # to the to-do list. She enters "Use Peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates and now shows both items on her list.
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list. Then she sees
        # the site generated a unique URL for her -- There is some explanatory
        # text to that effect
        self.fail('Finish The TEST')

        # She visits that URL - her to-do list is still there.

        # Satisfied she goes back to sleep
