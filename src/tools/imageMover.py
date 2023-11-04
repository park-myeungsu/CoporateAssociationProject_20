import tkinter as tk
from tkinter import filedialog
import os

def select_classified_textfile():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        classified_files_list = load_classified_textfile(file_path)
        file_name = os.path.basename(file_path)
        print(classified_files_list)
        if classified_files_list is not None:
            classified_textfile_label.config(text=f"선택된 파일: {file_name}")
            images_source_directory_button.config(state="normal")
            images_source_directory_label.config(text="폴더를 선택해 주세요.")
            viewer_button.config(state="disabled")
            global selected_image
            selected_classified_files_list = classified_files_list

def select_images_source_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        print(f"선택된 폴더: {dir_path}")
        if validate_image_source_directory(dir_path) == False:
            print(f"잘못된 경로입니다.\n...src/dataset/images 로 경로를 설정해 주세요.")
        else:
            print("올바른 경로입니다.")
            images_source_directory_label.config(text=f"선택된 폴더: {dir_path}")

def load_classified_textfile(selected_textfile):
    with open(selected_textfile, 'r') as classified_files_list:
        result = classified_files_list.readlines()
    return result

# 이미지 소스 경로의 유효성 검사.
def validate_image_source_directory(selected_dir):
    if selected_dir.endswith(r'src/dataset/images'):
        return True
    else:
        return False




root = tk.Tk()
root.title("이미지 분류기")
root.geometry("250x200")

classified_textfile_button = tk.Button(root, text="분류된 파일 목록 선택", command=select_classified_textfile)
classified_textfile_button.pack()
classified_textfile_label = tk.Label(root, text="텍스트 파일을 선택해 주세요.")
classified_textfile_label.pack()

images_source_directory_button = tk.Button(root, text="이미지 소스 폴더 선택", command=select_images_source_directory, state="disabled")
images_source_directory_button.pack()
images_source_directory_label = tk.Label(root, text="")
images_source_directory_label.pack()

viewer_button = tk.Button(root, text="View Image with Labels", state="disabled")
viewer_button.pack()

root.mainloop()