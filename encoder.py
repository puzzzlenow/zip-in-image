import sys
import math
import argparse
import struct
from PIL import Image
from PIL.PngImagePlugin import PngInfo


def import_file():
    """ Return list containing RGB data of each pixel, 8-bit binary data from read file """
    with open(file_in, 'rb') as infile:
        rgb_list = []
        lod=0
        while True:
            try:
                rgb_list.append(struct.unpack('3B', infile.read(3)))
                lod+=3
            except struct.error:
                try:
                    rgb_list.append(struct.unpack('2B', infile.read(2)) + '(0,)')
                    lod+=2
                except struct.error:
                    try:
                        rgb_list.append(struct.unpack('1B', infile.read(1)) + '(0,0,)')
                        lod+=1
                    except struct.error:
                        break
    return rgb_list, lod


def gen_img(data, length_of_data, file_out):
    """ to generate PNG using binary in RGB tuple format """
    # important debug 
    height = math.ceil(math.sqrt( length_of_data ))
    img = Image.new('RGB', (height, height), "white")
    img.putdata(data)

    #save the LOD for future decode use
    metadata = PngInfo()
    metadata.add_text("LOD", str(length_of_data))

    # ENCODED OUTPUT
    img.save(file_out,'png', pnginfo=metadata)
    # img.show()
    # return file_out


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="...")
    parser.add_argument('filename', help="please provide a filename to encode",type=str)

    args = parser.parse_args()
    file_in = args.filename
    file_enc_out = file_in + ".png"

    # ENCODE FILE
    print( 'Encoding..' + file_in )
    sys.stdout.write('-------------------------------\n')

    int_list, length = import_file()
    sys.stdout.write('imported file : ' + file_in + '\n')

    gen_img(int_list, length, file_enc_out)
    sys.stdout.write('generated file : ' + file_enc_out + '\n')

    sys.stdout.write('---- FIN ----------------------\n')

