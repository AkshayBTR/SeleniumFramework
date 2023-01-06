import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

Dev_Env="https://www.dev.firelawn.com"
Test_Env="https://www.test.firelawn.com"
Prod_Env="https://www.firelawn.com"
driver=None
#function to consume commandline arguments
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--env",action="store",default="prod")

#request parameter will have the address of the class from where the request is coming
@pytest.fixture()
def setup(request):
    global driver
    browser=request.config.getoption("--browser")
    url=request.config.getoption("--env")
    if url.lower()=="prod":
        url=Prod_Env
    elif url.lower()=="test":
        url=Test_Env
    else:
        url=Dev_Env
    if browser.lower()=="chrome":
        chrome_service = Service("driver/chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
    elif browser.lower()=="firefox":
        Firefox_service = Service("driver/geckodriver.exe")
        driver = webdriver.Firefox(service=Firefox_service,desired_capabilities=DesiredCapabilities().FIREFOX)
    else:
        Edge_Service = Service("driver/msedgedriver.exe")
        driver = webdriver.Edge(service=Edge_Service,)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(url)
    request.cls.driver=driver
    #request.cls will give the class address to inject this driver
    #request.cls.driver=driver we are creating a variable called driver inside a class which calls the setup method

    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_name="./screenshots/"+file_name.split("/")[-1]
            driver.get_screenshot_as_file(file_name)
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name))
        report.extra = extra