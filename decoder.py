import os
import sys
from datetime import datetime
import math
import argparse
from PIL import Image
from PIL.PngImagePlugin import PngInfo


def export_file(rgb, file_out):
    with open(file_out, 'wb') as outfile:
        for int_out in rgb:
            outfile.write(int_out)
    return file_out


def decode_img(encoded_img_path):
    # need the length of data to calculate
    im = Image.open(encoded_img_path)
    int_list_out = list(Image.Image.getdata(im))
    length_of_data = int(im.text['LOD'])

    # print('length_of_data=' + str(length_of_data) )
    trim_int_list_out = int_list_out[: length_of_data]

    rgb = []
    for r,g,b in trim_int_list_out:
        rgb.append(r.to_bytes(1,'big'))
        rgb.append(g.to_bytes(1,'big'))
        rgb.append(b.to_bytes(1,'big'))

    return rgb


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="...")
    parser.add_argument('filename', help="please provide a filename to decode",type=str)
    args = parser.parse_args()
    encoded_img_file_in = args.filename
    ts = datetime.today().strftime("%Y%m%d-%H%M%S.%f")
    head_tail = os.path.split(encoded_img_file_in)
    head_filepath = head_tail[0] +'/'
    tail_filepath = ts +'-' + head_tail[1][:-4]
    file_out = os.path.join(head_filepath, tail_filepath)

    #DECODE FILE
    print( 'Decoding..' + encoded_img_file_in )
    
    sys.stdout.write('-------------------------------\n')
    sys.stdout.write('decoding img file : ' + encoded_img_file_in + '\n')

    rgb = []
    rgb = decode_img(encoded_img_file_in)

    export_file(rgb, file_out)
    sys.stdout.write('exported file : ' + file_out + '\n')


    sys.stdout.write('---- FIN ----------------------\n')
    
