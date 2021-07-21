from Test8_densenet import model
from faster_rcnn_pytorch_master_julei2 import frcnn
from pytorch_yolov4_master import models
from pytorch_yolov4_master import demo
from pytorch_yolov4_master import yolov4_stage1_stage2
from faster_rcnn_pytorch_master_julei2 import predict_two_stage


import argparse

def detect_insulator(input_data):
    parser = argparse.ArgumentParser('Test your image or video by trained model.')
    parser.add_argument('-cfgfile', type=str, default='./pytorch_yolov4_master/cfg/yolov4-insulator.cfg',
                        help='path of cfg file', dest='cfgfile')
    parser.add_argument('-weightfile', type=str,
                        default='./pytorch_yolov4_master/weights/yolov4-insulator_final.weights',
                        help='path of trained model.', dest='weightfile')
    parser.add_argument('-imgfile', type=str,
                        default=str(input_data),
                        help='path of your image file.', dest='imgfile')
    args = parser.parse_args()
    demo.detect_cv2(args.cfgfile, args.weightfile, args.imgfile)


if __name__=="__main__":
    f = open("two_stage_split_pins_input_address.txt", "r")
    input_data = f.read()
    f.close()
    # detect_insulator(input_data)
    # yolov4_stage1_stage2.detect_connected_fitting(input_data)
    predict_two_stage.detect_bolts(input_data)