#!/usr/bin/env python3

from uuid import uuid1
import qrcode

def gen_single_qr_code_png():
    unique_id = uuid1()
    image = qrcode.make(str(unique_id))
    image.save(f"{unique_id}.png")
    print("Made a qr_code for: ", unique_id)
    return unique_id, image

def gen_multiple_qr_code_png(number_of_codes):
    for ii in range(number_of_codes):
        gen_single_qr_code_png()
