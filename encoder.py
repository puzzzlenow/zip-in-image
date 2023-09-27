import sys
import math
import argparse
from PIL import Image
from PIL.PngImagePlugin import PngInfo


def import_file():
    with open(file_in, 'rb') as infile:
        int_list = []
        byte = infile.read(1)
        int_list.append(  int.from_bytes(byte, "big")  )
        while byte != b"":
            byte = infile.read(1)
            int_list.append(  int.from_bytes(byte, "big")  )
        # for byte in byte_list:
        #     sys.stdout.write('{0:08b}'.format(ord(byte)))
    return int_list


def gen_img(int_list, file_enc_out):
    data = []
    int_list_iter = iter(int_list)
    try:
        while True:
            a = b = c = 0
            a = next(int_list_iter)
            b = next(int_list_iter)
            c = next(int_list_iter)
            data.append( (a,b,c) )

    except(StopIteration):
        data.append( (a,b,c) )

    # important debug 
    length_of_data = len(data)
    height = math.ceil(math.sqrt( length_of_data ))
    area = height * height

    # remainder should be padded to form a complete image
    remainder=area-len(data)
    for i in range(remainder):
        data.append( (0,0,0) )

    img = Image.new('RGB', (height, height), "white")
    img.putdata(data)

    #save the LOD for future decode use
    metadata = PngInfo()
    metadata.add_text("LOD", str(length_of_data))

    # ENCODED OUTPUT
    img.save(file_enc_out,'png', pnginfo=metadata)
    # img.show()
    return file_enc_out


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="...")
    parser.add_argument('filename', help="please provide a filename to encode",type=str)

    args = parser.parse_args()
    file_in = args.filename
    file_enc_out = file_in + ".png"

    # ENCODE FILE
    print( 'Encoding..' + file_in )
    sys.stdout.write('-------------------------------\n')

    int_list = import_file()
    sys.stdout.write('imported file : ' + file_in + '\n')

    gen_img(int_list, file_enc_out)
    sys.stdout.write('generated file : ' + file_enc_out + '\n')

    sys.stdout.write('---- FIN ----------------------\n')
    
