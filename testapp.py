import pytest
import os
import sys
from app import app

# Challenges faced and solutions:
#1. Driver Pathing:  the terminal rejected the --webdriver flag path.
#I solved this by using os.path.dirname to dynamically add the driver folder
#to the system path so the testing framework finds it automatically.
#2. Version Mismatch: Chrome updated requiring the new 'Chrome for Testing' driver.
#I had to manually locate the correct stable binary to match my local browser.
#3. Dash Fixture Errors: Trying to manually set the driver attribute caused an AttributeError.
#I fixed this by letting the dash_duo fixture handle the driver creation.

#This finds the current folder and adds it to the system path
#so dash_duo can find chromedriver.exe automatically.
chrome_driver_path = os.path.dirname(os.path.abspath(__file__))
if chrome_driver_path not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + chrome_driver_path

#This tells dash-testing to use Chrome and run it without opening a window
def pytest_setup_options():
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return options

#My tests

def test_header_present(dash_duo):
    #Start the app
    dash_duo.start_server(app)
    #Look for the H1 header
    header = dash_duo.wait_for_element("h1", timeout=10)
    #Check if it exists and says Pink Morsel
    assert header is not None
    assert "Pink Morsel" in header.text

def test_visualization_present(dash_duo):
    #Start the app
    dash_duo.start_server(app)
    #Make sure the chart shows up
    visualization = dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    assert visualization is not None

def test_region_picker_present(dash_duo):
    #Start the app
    dash_duo.start_server(app)
    #Check if my region filter is there
    region_picker = dash_duo.wait_for_element("#region-filter", timeout=10)
    assert region_picker is not None