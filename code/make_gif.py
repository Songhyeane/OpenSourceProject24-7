from PIL import Image
import glob
import os
import natsort

# 이미지 파일 경로 설정
image_files = os.listdir('simulation_output_images')

image_files = natsort.natsorted(image_files)  # 파일들을 순서대로 정렬 (필요한 경우)

image_files= image_files[2:]

for idx, img_names in enumerate(image_files):
    image_files[idx] = 'simulation_output_images/' + image_files[idx]

# 이미지들을 열고, 리스트에 저장
images = [Image.open(image) for image in image_files]

# 첫 번째 이미지를 기준으로 GIF 생성 및 나머지 이미지 추가
images[0].save('output.gif', save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)
