import os

def get_subdirectories(path):
    """주어진 경로에 하위 디렉터리가 존재하는지 검사합니다."""
    subdirectories = []
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():  # 엔트리가 디렉터리인 경우
                subdirectories.append(entry.name)
    return subdirectories

# 주어진 경로
path_to_check = r'D:\pycharm_project\Corporate_connection_yolov5\src\dataset\images'
result = get_subdirectories(path_to_check)

# 하위 디렉터리 존재 여부 확인
if result:
    print(f"하위 디렉토리가 존재합니다. : {result}")
else:
    print(f"하위 디렉토리가 존재하지 않습니다.")