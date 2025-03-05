from ultralytics import YOLO
import cv2

# YOLOv8 모델 로드 (사전 학습된 COCO 데이터셋 모델)
model = YOLO("yolov8n.pt")  # 'n'은 nano 모델 (빠름). 's', 'm', 'l', 'x'도 가능

# 테스트할 이미지 로드
image_path = "/Users/bytemaster/Documents/GitHub/AI/obama.jpeg"
image = cv2.imread(image_path)

# 객체 탐지 수행
results = model(image)

# 탐지 결과 출력
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # 경계 상자 좌표
        conf = box.conf[0].item()  # 신뢰도
        cls = int(box.cls[0].item())  # 클래스 번호
        label = model.names[cls]  # 클래스 이름
        
        # 경계 상자 그리기
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 결과 이미지 표시
cv2.imshow("YOLOv8 Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
