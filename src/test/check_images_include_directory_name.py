import os

def check_images_include_directory_name(parent_directory):
    """하위 디렉터리 안의 이미지 파일들이 디렉터리 이름을 포함하고 있는지 확인합니다."""
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}  # 지원되는 이미지 파일 확장자
    all_files_include_dir_name = True  # 모든 파일이 조건을 만족하는지 확인하는 플래그

    for subdir in os.listdir(parent_directory):
        subdir_path = os.path.join(parent_directory, subdir)

        if os.path.isdir(subdir_path):
            for file in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, file)
                file_extension = os.path.splitext(file_path)[1].lower()

                if file_extension in image_extensions:
                    # 이미지 파일이면 디렉터리 이름을 포함하는지 확인
                    if subdir not in file:
                        all_files_include_dir_name = False
                        print(f"이미지 파일 '{file}'은(는) 디렉터리 이름 '{subdir}'을 포함하지 않습니다.")

    return all_files_include_dir_name

# 주어진 경로
path_to_check = r'D:\pycharm_project\Corporate_connection_yolov5\src\dataset'

# 이미지 파일 이름 확인
if check_images_include_directory_name(path_to_check):
    print(f"모든 이미지 파일이 해당 디렉터리 이름을 포함하고 있습니다.")
else:
    print(f"일부 이미지 파일이 해당 디렉터리 이름을 포함하고 있지 않습니다.")