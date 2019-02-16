import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "ud-source": "www",
    "ud-style": "default,default,full",
    "ud-validationsubmit": "true",
    "ud-viewport": "8"
}


class LoginError(Exception):
    pass


class Uniday:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers.update(headers)
        self.logged_in = False
        # dict to store when code can be reissued
        self.reissue_on = {}

    def login(self, email, password):
        if self.logged_in:
            return False
        self.email = email
        self.password = password
        self.loginform = {
            "QueuedPath": "/CA/en-CA",
            "EmailAddress": self.email,
            "Password": self.password,
            "Human": None
        }
        r = self.s.post(
            "https://account.myunidays.com/CA/en-CA/account/log-in", data=self.loginform)
        if r.status_code == 200:
            self.logged_in = True
        else:
            raise Exception("Invalid credentials")

    def logout(self):
        if self.logged_in:
            # clear dict and cookies
            self.reissue_on = {}
            self.s.cookies.clear()
        else:
            return False

    def get_code(self, url):
        if not self.logged_in:
            return False
        form = {
            "forceNew": "true"
        }
        r = self.s.post(url, data=form)
        if r.status_code == 200:
            # save reissue date and return code
            self.reissue_on[url] = r.json()["canReissueOn"]
            return r.json()["code"]
        else:
            return False

    def get_reissue(self, url):
        if not self.logged_in:
            return False
        if url in self.reissue_on:
            return self.reissue_on[url]


if __name__ == '__main__':
    pass