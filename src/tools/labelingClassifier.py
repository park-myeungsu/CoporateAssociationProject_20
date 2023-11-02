import os
import tkinter as tk
from tkinter import filedialog

# GUI를 생성하는 함수
def create_gui():
    root = tk.Tk()
    root.withdraw()  # 기본 창 숨기기
    lablings_directory = filedialog.askdirectory(title="라벨링 파일이 있는 디렉토리 선택")
    if not lablings_directory:
        print("디렉토리 선택이 취소되었습니다.")
        return
    classified_labeling_directory = r"D:\pycharm_project\Corporate_connection_yolov5\src\dataset"
    # classified_labeling_directory = filedialog.askdirectory(title="분류된 라벨링 파일을 저장할 디렉토리 선택")
    # if not classified_labeling_directory:
    #     print("디렉토리 선택이 취소되었습니다.")
    #     return

    classify_and_save_labels(lablings_directory, classified_labeling_directory)

# 라벨링 파일을 처리하고 분류하여 저장하는 함수
def classify_and_save_labels(lablings_directory, classified_labeling_directory):
    existing_files_content = {}
    for class_name in ["Plastic", "Glass", "Can", "Others"]:
        save_path = os.path.join(classified_labeling_directory, f"{class_name.lower()}_list.txt")
        if os.path.exists(save_path):
            with open(save_path, 'r') as save_file:
                existing_files_content[class_name] = set(save_file.read().splitlines())

    for filename in os.listdir(lablings_directory):
        if filename.endswith(".txt"):
            class_counts = {
                "Plastic": 0,
                "Glass": 0,
                "Can": 0,
                "Others": 0
            }
            with open(os.path.join(lablings_directory, filename), 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) > 0:
                        class_name = parts[0]
                        if class_name in class_counts:
                            class_counts[class_name] += 1

            # 클래스 비율 확인 및 분류
            max_class = max(class_counts, key=class_counts.get)
            save_path = os.path.join(classified_labeling_directory, f"{max_class.lower()}_list.txt")

            # 이미 분류된 파일에 filename이 존재하는지 확인
            if os.path.exists(save_path):
                with open(save_path, 'r') as save_file:
                    existing_files = save_file.readlines()
                if filename + "\n" in existing_files:
                    print(f"{filename}은(는) 이미 {max_class.lower()}_list.txt에 존재합니다.")
                    continue

            with open(save_path, 'a') as save_file:
                save_file.write(filename + "\n")

    print("라벨링 파일 분류 완료!")

if __name__ == "__main__":
    create_gui()