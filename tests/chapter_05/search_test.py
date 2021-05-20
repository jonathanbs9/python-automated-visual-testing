from tests.chapter_05.conftest import validate_window
from assertpy import assert_that
from time import sleep

from page_objects.search_page import SearchPage

def test_filter_book(eyes, driver):
    page = SearchPage(driver)

    page.filter_books('James')
    #sleep(5)
    #result = page.verify_visible_books_by_title('Agile Testing')
    #assert_that(result).is_equal_to(True)

    validate_window(driver, eyes, tag='filter_text')