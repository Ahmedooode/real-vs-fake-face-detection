from ultralytics import YOLO

model = YOLO('yolov8l.pt')

def main():
    model.train(data='Dataset/SplitData/dataOffline.yaml', epochs=300)

if __name__ == '__main__':
    main()