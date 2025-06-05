import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.asset = 0

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def set_asset(self,amount):
        self.asset = amount
        print(f"자산이 {amount}원으로 설정되었습니다.\n")

    def show_balance(self):
        total_spent = sum(e.amount for e in self.expenses)
        balance = self.asset - total_spent
        print(f"\n[잔약 현황]")
        print(f"현재 자산: {self.asset}원")
        print(f"총 지출: {total_spent}원")
        print(f"남은 잔액: {balance}원\n")

    