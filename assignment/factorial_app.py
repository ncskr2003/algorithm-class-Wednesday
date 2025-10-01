import time

Test_Number= [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

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
    
    if n == 0 or n == 1:   # 0! = 1, 1! = 1
        return 1
    
    return n * factorial_rec(n-1)

def run_with_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start

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



def third():
     n = int(input("\nn값(정수, 0 이상)을 입력하세요: ").strip())
     res_iter, t_iter = run_with_time(factorial_iter, n)
     res_rec, t_rec = run_with_time(factorial_rec, n)
     match = (res_iter == res_rec)

     print(f"[반복] {n}! = {res_iter}")
     print(f"[재귀] {n}! = {res_rec}")
     if match:
         print(f"결과 일치 여부: 일치")
     else:
         print(f"결과 일치 여부: 불일치")
     print(f"[반복] 시간:{t_iter:.6f}s")
     print(f"[재귀] 시간: {t_rec:.6f}s")

def fourth():
    for n in Test_Number:
            res_iter, t_iter = run_with_time(factorial_iter, n)
            res_rec, t_rec = run_with_time(factorial_rec, n)
            match = (res_iter == res_rec)

            print(f"\nn! = {n}  |  same = {match}   | iter = {t_iter:.6f}s |   rec =   {t_rec:.6f}s")
            if match:
                 print(f"{n}! = {res_iter}")
            else:
                print(f"{n}! = [rec]{res_iter} | [iter]{res_rec} ")

def menu():
    print("\n====== 메뉴 ======")
    print("1) 반복법으로 n! 계산")
    print("2) 재귀로 n! 계산")
    print("3) 두 방식 모두 계산 후 결과/시간 비교")
    print("4) 준비된 테스트 데이터 일괄 실행")
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
        elif choice == "3":
            third()
        elif choice == "4":
            fourth()
        elif choice == "q":
            print("종료합니다.")
            break
        else:
            print("정수 1~4 또는 q를 선택해주세요")

if __name__ == "__main__":
    main()