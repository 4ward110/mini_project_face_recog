# Nhận diện khuôn mặt và Xuất ra tiếng nói

## 1. Install

- **Note**:
- Môi trường cài đặt `python 3.7` (bắt buộc)
- Nên tạo môi trường ảo để cài đặt các gói package

```
pip install -r requirement.txt
```

## Tạo data set:

- Tạo thư mục `Dataset` trong Face_Recog, trong thư mục con tạo tiếp hai thưc mục raw và processed
- Trong thư mục raw tạo thư mục chứa ảnh với tên mỗi thư mục là tên của từng người

- Tạo thư mục `Models` để chứa model


## Pre-processing
- Thực hiện tiền xwur lý ảnh đầu vào (cắt ra mặt người mỗi ảnh)

```
python src/align_dataset_mtcnn.py  Dataset/FaceData/raw Dataset/FaceData/processed --image_size 160 --margin 32  --random_order --gpu_memory_fraction 0.25
```

- Tải weight pretrain, giải nén và đưa vào `Models` tại [đây](https://drive.google.com/file/d/1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-/view)

## Train

```
python3 src/classifier.py TRAIN Dataset/FaceData/processed Models/20180402-114759.pb Models/facemodel.pkl --batch_size 1000
```

## Run: 
- Sử dụng webcam máy tính

```
python3 src/face_rec_cam.py
```


