from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem

# launch_tbb_tor_with_stem("C:\\Users\\CodeCrusha\\Desktop\\Tor Browser") # I think you can remove this, but maybe some future usages need that 
with TorBrowserDriver("D:\\program files\\Tor Browser", tor_cfg=cm.USE_STEM) as driver:
    driver.load_url("https://check.torproject.org", wait_on_page=3, wait_for_page_body=True)
    print(driver.find_element_by("h1.on").text)
    print(driver.find_element_by(".content > p").text)