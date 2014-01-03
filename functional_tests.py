from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # User notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # User is invited to enter a to-do item straight away

        # User types "Buy peacock feathers"

        # When user hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting the user to add another item.
        # User enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on their list

        # User wonders whether the site will remember their list.
        # Then user sees that the site has generated a unique URL for them
        # -- there is some explanatory text to that effect.

        # User visits that URL - their to-do list is still there.

        # Satisfied, user goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')

