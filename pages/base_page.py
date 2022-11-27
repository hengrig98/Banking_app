class BasePage:

    USER = 'Demo-User'
    USER_PASSWORD = 'Demo-Access1'
    ADMIN = 'Bank-Admin'
    ADMIN_PASSWORD = 'Demo-Access1'
    TIMEOUT = 10


    def __init__(self, driver) -> None:
       self.driver = driver