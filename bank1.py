class Bank:
    def __init__(self):
        self.bankname = 'DAVE'
        # self.rc_no = '2033356'
        # self.branch = 'Abuja'
    def home(self):
        print(f'''
        Welcome to {self.bankname} bank
        1. Sign up
        2. Sign in
        ''')
bank = Bank()
bank.home()

