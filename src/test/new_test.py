import os

path = "F:\\pycharm_projcets\\CoporateAssociationProject_20\\src\\dataset\\images\\A1\\A1C_20220818_000001.jpg"

# os.path.dirname을 두 번 사용하여 상위 디렉토리를 두 번 추출합니다.
base_path = os.path.dirname(os.path.dirname(os.path.dirname(path)))
filename = os.path.basename(path)
filename_without_extension = os.path.splitext(os.path.basename(path))[0]

separator = '\\'
split_path = path.split(separator)
dataset = separator.join(map(str, split_path[0:4]))
section = split_path[6]
labeling_textfile = f"{split_path[7]}.txt"
file_path = dataset + "formatted_labelings\\" + section + "\\" + labeling_textfile

print(file_path)