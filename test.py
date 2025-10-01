def factorial_iter(n):  # 반복문
    if n < 0:
        raise ValueError("\n정수(0 이상의 숫자)만 입력하세요.")
    
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def factorial_rec(n): # 재귀
    if n < 0:
        raise ValueError("\n정수(0 이상의 숫자)만 입력하세요.")
    
    if n == 1:
        return 1
    
    return n * factorial_rec(n-1)

def first():
    n = int(input("\nn값(정수, 0 이상)을 입력하세요: ").strip())
    if n >= 0:
        print(f"반복법 팩토리얼 계산: {factorial_iter(n)}")
    else:
        print("\n정수(0 이상의 숫자)만 입력하세요.")


def second():
    n = int(input("\nn값(정수, 0 이상)을 입력하세요: ").strip())
    if n >= 0:
        print(f"재귀 팩토리얼 계산: {factorial_rec(n)}")
    else:
        print("\n정수(0 이상의 숫자)만 입력하세요.")



def menu():
    print("\n====== 메뉴 ======")
    print("1) 반복법으로 n! 계산")
    print("2) 재귀로 n! 계산")
    print("q) 종료")
    print("-------------------------------------------\n")

def main():
    while True:
        menu()
        choice = input("선택: ").strip().lower()

        if choice == "1":
            first()
        elif choice == "2":
            second()
        elif choice == "q":
            print("종료합니다.")
            break
        else:
            print("1~4 또는 q를 선택해주세요")


if __name__ == "__main__":
    main()
