import os
import shutil
import time
import math

def move_files(source_dir, target_dir, moving_files_number, delay):
    """
    파일들을 지정한 폴더로 moving_files_number 개수 만큼 옮기며, 각 작업 당 딜레이를 부여 합니다.

    Parameters:
    - source_dir: 이미지 파일들이 있는 원본 폴더 경로
    - target_dir: 이미지 파일들을 옮길 대상 폴더 경로
    - moving_files_number: 한 작업 당 옮길 파일의 개수
    - delay: 각 배치 후의 딜레이 시간 (초)
    """

    # 원본 폴더에서 파일 리스트를 가져옵니다.
    all_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    all_files_number = len(all_files)
    all_tasks_number = math.ceil(all_files_number/moving_files_number)
    count = 0

    print("전체 파일 갯수: ", all_files_number)

    # 파일 리스트를 num_files 개수만큼 분할합니다.
    for i in range(0, all_files_number, moving_files_number): #range(start, stop, step)
        files_to_move = all_files[i:i + moving_files_number]
        count += 1

        # 분할된 파일 리스트를 대상 폴더로 옮깁니다. - 1작업 단위
        for file in files_to_move:
            shutil.move(os.path.join(source_dir, file), os.path.join(target_dir, file))
        print(f"{moving_files_number}개의 파일을 {target_dir}로 옮겼습니다. (작업 진행도: {count}/{all_tasks_number})")

        # 딜레이를 추가합니다.
        time.sleep(delay)


# 사용 예:
source_directory = r"F:\pycharm_projcets\CoporateAssociationProject_20\src\test\afaag"
target_directory = r"F:\pycharm_projcets\CoporateAssociationProject_20\src\dataset\test"
move_files(source_directory, target_directory, 20, 0.5)