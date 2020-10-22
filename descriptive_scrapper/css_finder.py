from os import stat
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class PageWork:
    def __init__(self, driver: webdriver.Chrome, details: dict) -> None:
        self.driver = driver
        self.items_name = details.keys()
        self.items_css, self.items_method  = self._detail_getter(details)

        # changing within the instance
        self._pointer = 0
        self._element = None

    def execute(self): 
        """
        Excute the page scrap
        """
        for name in self.items_name:
            self._element = self.working_element # loop each possible css variaion
            self.working_method() # input the information
            self._pointer += 1 


    @staticmethod
    def _detail_getter(details: dict):
        css = []
        method = []

        for v in details.values():
            css.append(v.pop('css')) # append the css
            method.append(v) # append other non css 

        return css, method

    @property
    def working_element(self): 
        element = None
        i = self._pointer

        for el in self.items_css[i]:
            try: 
                element = self.driver.find_element_by_css_selector(el)
                break
            except NoSuchElementException:
                continue

        print(element)
        return element

    def working_method(self): 
        i = self._pointer

        for method, in_val in self.items_method[i].items():
            print(method)
            getattr(self, method)(in_val) # using the key to retrieve the class method 


    ## method names need to be consistent to those in the json
    def write(self, in_val):
        """
        Driver to use send_keys
        """
        self._element.send_keys(in_val)

    def press(self, _): 
        """
        Same as click
        """
        self._element.click()
