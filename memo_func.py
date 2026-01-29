import os

memo_files = []
current_file = None

def move_to_dir():
    if not os.path.exists("memo"):
        os.mkdir("memo")
    os.chdir("memo")

def move_current_memo():
    global current_file

    if current_file is None:
        print("선택된 메모장이 없습니다.")
        return

    target_dir = input("이동할 디렉터리명 입력: ")

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    filename = os.path.basename(current_file)
    new_path = os.path.join(target_dir, filename)

    if os.path.exists(new_path):
        print("해당 디렉터리에 같은 이름의 메모장이 이미 있습니다.")
        return

    os.rename(current_file, new_path)
    current_file = new_path

    print("메모장이 이동되었습니다.")


def new_memo():
    global current_file

    filename = input("새 메모장 파일명 입력: ")

    if filename in memo_files:
        print("이미 존재하는 메모장입니다.")
        return

    memo_files.append(filename)

    path = filename
    with open(path, "w", encoding="utf-8") as f:
        pass    # 빈 파일 생성

    current_file = path
    print(f"{filename} 메모장이 생성되고 선택되었습니다.")

def select_memo():
    global current_file

    if not memo_files:
        print("메모장이 없습니다. 먼저 생성하세요.")
        return

    print("\n메모장 목록")
    for i, name in enumerate(memo_files):
        print(f"{i}. {name}")

    try:
        choice = int(input("선택할 번호: "))
        current_file = memo_files[choice]
        print(f"[{current_file}] 메모장이 선택되었습니다.")
    except (ValueError, IndexError):
        print("잘못된 선택입니다.")

def write_memo():
    if current_file is None:
        print("선택된 메모장이 없습니다.")
        return

    content = input("내용 입력: ")

    with open(current_file, "a", encoding="utf-8") as f:
        f.write(content + "\n")

    print("메모가 저장되었습니다.")

def read_memo():
    if current_file is None:
        print("선택된 메모장이 없습니다.")
        return

    try:
        with open(current_file, "r", encoding="utf-8") as f:
            print("\n=====메모 내용 =====")
            print(f.read())
    except FileNotFoundError:
        print("메모 파일이 존재하지 않습니다.")


def exit_program():
    print("프로그램을 종료합니다.")
    exit()

menu = {
    "0": new_memo,
    "1": select_memo,
    "2": write_memo,
    "3": read_memo,
    "4": move_current_memo,
    "5": exit_program
}