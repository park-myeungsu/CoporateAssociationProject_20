from tkinter import filedialog
import os

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        return 0  # 파일을 찾을 수 없을 경우 0 반환
    except Exception as e:
        print(f"파일을 읽는 동안 오류 발생: {str(e)}")
        return -1  # 다른 오류 발생 시 -1 반환

if __name__ == "__main__":
    initial_directory = r"F:\pycharm_projcets\CoporateAssociationProject_20\src\dataset\labeling_datas"
    file_path = filedialog.askopenfilename(title="라인 수 확인할 .txt 파일 선택", initialdir=initial_directory)
    print("선택한 파일:", os.path.basename(file_path))
    line_count = count_lines_in_file(file_path)

    if line_count == 0:
        print("파일을 찾을 수 없습니다.")
    elif line_count == -1:
        print("파일을 읽는 동안 오류가 발생했습니다.")
    else:
        print(f"파일에 총 {line_count}줄이 있습니다.")