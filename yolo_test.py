# YOLO 라이브러리 임포트
from ultralytics import YOLO
import cv2

# YOLOv8 모델 로드 (사전 학습된 COCO 데이터셋 모델)
model = YOLO("yolov8n.pt")  # 'yolov8n.pt'는 YOLOv8의 nano 모델로 가장 빠르고 가벼운 모델
# 's', 'm', 'l', 'x' 모델도 가능하며, 'n'은 속도와 경량화가 강조된 모델입니다.

# 테스트할 이미지 경로
image_path = "이미지경로"  # 이 부분에 실제 이미지 경로를 입력하세요. 예: "image.jpg"

# 이미지 로드
image = cv2.imread(image_path)  # OpenCV를 이용해 이미지를 읽어들입니다.

# 객체 탐지 수행 (YOLO 모델에 이미지를 입력하여 탐지 결과를 얻습니다.)
results = model(image)  # 모델에 이미지를 넣어서 결과를 추출합니다.

# 탐지 결과 출력
for result in results:  # 결과가 여러 개일 수 있으므로 for문을 통해 하나씩 처리합니다.
    for box in result.boxes:  # 'boxes'는 탐지된 각 객체의 경계 상자 정보를 포함합니다.
        # 경계 상자 좌표 (x1, y1, x2, y2)를 추출하여 정수형으로 변환
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # box.xyxy는 (x1, y1, x2, y2) 좌표를 반환합니다.
        
        # 탐지된 객체의 신뢰도 (confidence) 값 추출
        conf = box.conf[0].item()  # box.conf는 신뢰도 값으로, 첫 번째 값만 사용합니다.
        
        # 객체의 클래스 번호 (0부터 시작하는 숫자)
        cls = int(box.cls[0].item())  # box.cls는 객체의 클래스 번호입니다.
        
        # 클래스 번호를 클래스 이름으로 변환
        label = model.names[cls]  # model.names는 클래스 번호에 대응하는 클래스 이름 리스트입니다.
        
        # 이미지에 경계 상자 그리기 (색상은 초록색, 두께는 2)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 경계 상자를 그려줍니다.
        
        # 탐지된 객체 이름과 신뢰도 텍스트 표시 (경계 상자 위에 출력)
        cv2.putText(image, f"{label} {conf:.2f}", (x1, y1 - 10),  # 텍스트는 경계 상자 위에 표시
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # 글꼴, 크기, 색상, 두께 설정

# 결과 이미지 표시
cv2.imshow("YOLOv8 Object Detection", image)  # 객체 탐지된 이미지를 화면에 띄워줍니다.
cv2.waitKey(0)  # 사용자가 키를 누를 때까지 대기
cv2.destroyAllWindows()  # 모든 OpenCV 창을 닫습니다.
