import cv2

# 이미지 경로를 정확히 지정해 주세요.
image_path = '/Users/사용자이름/Documents/GitHub/AI/1.jpg'

# 이미지를 읽어들입니다.
image = cv2.imread(image_path)

# 그레이스케일로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 결과를 저장할 경로
output_path = '/Users/사용자이름/Documents/GitHub/AI/gray_image.jpg'

# 그레이스케일 이미지를 저장
cv2.imwrite(output_path, gray_image)
