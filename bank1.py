class Bank:
    def __init__(self):
        self.bankname = 'UBA'
        self.rc_no = '2033356'
        self.branch = 'Abuja'
    def home(self):
        print(f'''
            Welcome to {self.bankname} {self.rc_no}, {self.branch} branch
            1. Sign up
            2. Sign in
              ''')
bank = Bank()
#bank.home()

