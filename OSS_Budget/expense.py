
class Expense:
    def __init__(self, date, category, description, amount, memo=""):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.memo = memo

    def __str__(self):
        base = f"[{self.date}] {self.category} - {self.description}: {self.amount}원"
        return f"{base} / 메모: {self.memo}" if self.memo else base