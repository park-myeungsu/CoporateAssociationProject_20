from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import json
import os


def open_json_dir():
    json_dir_path = filedialog.askdirectory()
    if json_dir_path:
        json_dir_var.set(json_dir_path)

def open_output_dir():
    output_dir_path = filedialog.askdirectory()
    if output_dir_path:
        output_dir_var.set(output_dir_path)

def convert_class_name(class_name):
    if class_name.startswith('c_3'):
        return 'Can'
    elif class_name.startswith('c_4'):
        return 'Glass'
    elif class_name.startswith('c_5') or class_name.startswith('c_6'):
        return 'Plastic'
    else:
        return 'Others'

def convert_to_yolov5_format(data, image_width, image_height):
    yolov5_labels = []
    for obj in data['objects']:
        x = obj['annotation']['coord']['x']
        y = obj['annotation']['coord']['y']
        width = obj['annotation']['coord']['width']
        height = obj['annotation']['coord']['height']

        x_center = x + width / 2
        y_center = y + height / 2
        class_name = obj['class_name']

        x_center /= image_width
        y_center /= image_height
        width /= image_width
        height /= image_height

        class_name = convert_class_name(class_name)  # 클래스 이름 변환

        label = f"{class_name} {x_center} {y_center} {width} {height}"
        yolov5_labels.append(label)

    return yolov5_labels


def convert_json_to_yolov5(json_dir_path, output_dir_path, progress_bar):
    json_files = [filename for filename in os.listdir(json_dir_path) if filename.endswith('.json')]
    total_files = len(json_files)

    for i, filename in enumerate(json_files):
        json_path = os.path.join(json_dir_path, filename)
        output_path = os.path.join(output_dir_path, os.path.splitext(filename)[0] + '.txt')

        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            image_width, image_height = map(int, data['Info']['RESOLUTION'].split('/'))
            yolov5_labels = convert_to_yolov5_format(data, image_width, image_height)

            with open(output_path, 'w') as output_file:
                output_file.write('\n'.join(yolov5_labels))

        # Update progress bar
        progress = int((i / total_files) * 100)
        progress_bar['value'] = progress
        root.update_idletasks()



# GUI 생성
root = tk.Tk()
root.title("JSON to YOLOv5 Converter")
root.geometry("350x200")

json_dir_var = tk.StringVar()
output_dir_var = tk.StringVar()

json_dir_label = tk.Label(root, text="Select JSON Directory:")
json_dir_label.pack()
json_dir_entry = tk.Entry(root, textvariable=json_dir_var, state="readonly")
json_dir_entry.pack()
json_dir_button = tk.Button(root, text="Browse", command=open_json_dir)
json_dir_button.pack()

output_dir_label = tk.Label(root, text="Select Output Directory:")
output_dir_label.pack()
output_dir_entry = tk.Entry(root, textvariable=output_dir_var, state="readonly")
output_dir_entry.pack()
output_dir_button = tk.Button(root, text="Browse", command=open_output_dir)
output_dir_button.pack()

progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress_bar.pack()

convert_button = tk.Button(root, text="Convert to YOLOv5",
                           command=lambda: convert_json_to_yolov5(json_dir_var.get(), output_dir_var.get(), progress_bar))
convert_button.pack()

root.mainloop()