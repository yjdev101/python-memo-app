"""
#1.메모장 프로그램 제작
#2.파일 이름을 설정할 수 있게 제작
#3.쓰기 작업시 파일 없으면 생성, 있으면 추가

#4-1.저장 위치를 선택해서 저장할 수 있게 만들기
#4-2.저장 위치가 다르면 읽는 작업도 처리를 해야 합니다.
#os모듈

"""
import os
import memo_func

#memo_func.move_to_dir()

#메뉴 반복

while True:
    print("\n0. 새 메모장 만들기")
    print("1. 메모장 선택")
    print("2. 메모 작성")
    print("3. 메모 읽기")
    print("4. 메모장 옮기기")
    print("5. 종료")

    choice = input("번호 선택: ")

    action = memo_func.menu.get(choice)
    if action:
        action()
    else:
        print("잘못된 입력입니다. 다시 선택해 주세요.")

