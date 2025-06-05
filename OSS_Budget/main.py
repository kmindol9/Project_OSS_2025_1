from budget import Budget

PASSWORD = "0613"

def check_password():
    for _ in range(3):
        pw = input("비밀번호를 입력하세요: ")
        if pw == PASSWORD:
            print("성공적으로 인증이 완료되었습니다.\n")
            return True
        else:
            print("비밀번호가 틀렸습니다.")
    print("비밀번호 3회 입력 실패. 프로그램이 종료됩니다.")
    return False


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    if check_password():
        main()