import tkinter as tk
from tkinter import filedialog
import cv2
import os
import numpy as np


def auto_select_label_file(image_file_path):
    print(image_file_path)
    separator = '/'
    split_path = image_file_path.split(separator)
    print(split_path)
    dataset = separator.join(map(str, split_path[0:5]))
    section = split_path[6]
    labeling_textfile = os.path.splitext(split_path[7])[0] + ".txt"
    print(labeling_textfile)
    file_path = dataset + "/formatted_labelings/" + section + "/" + labeling_textfile
    print(file_path)

    if file_path:
        labels = load_labels(file_path)
        if labels:
            label_label.config(text=f'Selected label file: {file_path}')
            viewer_button.config(state="normal")
            global selected_labels
            selected_labels = labels
        else:
            label_label.config(text="No label file selected.")
            viewer_button.config(state="disabled")

def open_image_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        image = load_image(file_path)
        if image is not None:
            image_label.config(text=f'Selected image file: {file_path}')
            labels_button.config(state="normal")
            viewer_button.config(state="disabled")
            global selected_image
            selected_image = image

            auto_select_label_file(file_path)
    else:
        image_label.config(text="No image file selected.")
        labels_button.config(state="disabled")
        viewer_button.config(state="disabled")

def open_label_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        labels = load_labels(file_path)
        if labels:
            label_label.config(text=f'Selected label file: {file_path}')
            viewer_button.config(state="normal")
            global selected_labels
            selected_labels = labels
    else:
        label_label.config(text="No label file selected.")
        viewer_button.config(state="disabled")

def view_image_with_labels():
    if selected_image is not None and selected_labels:
        result_image = display_image_with_bounding_boxes(selected_image, selected_labels)
        cv2.imshow('Image with Bounding Boxes', result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        image_label.config(text="No image file selected.")
        label_label.config(text="No label file selected.")
        labels_button.config(state="disabled")
        viewer_button.config(state="disabled")

def load_image(file_path):
    if not file_path:
        return None
    image = cv2.imread(file_path)
    if image is None:
        return None
    return image

def load_labels(file_path):
    if not file_path:
        return []
    with open(file_path, 'r') as label_file:
        labels = label_file.readlines()
    return labels

def display_image_with_bounding_boxes(image, labels):
    if image is None or not labels:
        return
    result_image = image.copy()
    image_height, image_width, _ = image.shape
    for label in labels:
        label = label.strip().split()
        class_name = label[0]
        x_center, y_center, width, height = map(float, label[1:])
        x = int((x_center - width / 2) * image_width)
        y = int((y_center - height / 2) * image_height)
        w = int(width * image_width)
        h = int(height * image_height)
        cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(result_image, class_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return result_image

# GUI 생성
root = tk.Tk()
root.title("Image and Label Viewer")
root.geometry("350x160")

selected_image = None
selected_labels = None

image_button = tk.Button(root, text="Open Image File", command=open_image_file)
image_button.pack()

image_label = tk.Label(root, text="No image file selected.")
image_label.pack()

labels_button = tk.Button(root, text="Open Label File", command=open_label_file, state="disabled")
labels_button.pack()

label_label = tk.Label(root, text="No label file selected.")
label_label.pack()

viewer_button = tk.Button(root, text="View Image with Labels", command=view_image_with_labels, state="disabled")
viewer_button.pack()

root.mainloop()