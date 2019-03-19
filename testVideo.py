import cv2
import fillAPI
import mask_rcnn.samples.test as mrcnn
import numpy as np

cap = cv2.VideoCapture('hall_objects_qcif.y4m')
frame_list = []

img_dir = 'input/hallway'
i = 0
# loop through all the frames and store them in a list
while (i < 330):
    # Capture frame-by-frame
    i += 1
    ret, frame = cap.read()
    print(type(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(i)
    frame_list.append(frame)
    cv2.imshow('frame', frame)
    if(i>100):
        mrcnn.get_image_mask(frame, i)
        input_img = 'input/hallway_'+str(i)+'_input.png'
        mask_img = 'input/hallway_' + str(i) + '_mask.png'
        fillAPI.fillVideo(input_img, mask_img, 1)
        # img_name = img_dir + str(i) + '.png'
        # cv2.imwrite(img_name, frame)
    cv2.waitKey(10)

print(frame_list[0].shape)
# fillAPI.fillVideo('examples/street_input.png', 'examples/street_mask.png', 1)



