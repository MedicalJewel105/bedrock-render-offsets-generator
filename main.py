from tkinter import filedialog
from PIL import Image
import json
import os


def calculate_scale_fp(texture_size: int):
    default_scale = 0.039 # nearly correct
    calculated_scale = round(default_scale*16/texture_size, 8)
    return [calculated_scale]*3

def calculate_scale_fp_offhand(texture_size: int):
    default_scale = 0.065
    calculated_scale = round(default_scale*16/texture_size, 8)
    return [calculated_scale]*3

def calculate_scale_tp(texture_size: int):
    default_scale = 0.0965
    calculated_scale = round(default_scale*16/texture_size, 8)
    return [calculated_scale]*3

def calculate_scale_tp_offhand(texture_size: int):
    default_scale = 0.0965
    calculated_scale = round(default_scale*16/texture_size, 8)
    return [calculated_scale]*3

def create_render_offsets(image_size: int) -> dict:
    main_hand = calculate_scale_fp(image_size)
    main_hand_tp = calculate_scale_tp(image_size)
    off_hand = calculate_scale_fp_offhand(image_size)
    off_hand_tp = calculate_scale_tp_offhand(image_size)
    render_offsets = {
        'minecraft:render_offsets': {
            'main_hand': {
                'first_person': {'scale': main_hand},
                'third_person': {'scale': main_hand_tp}
            },
            'off_hand': {
                'first_person': {'scale': off_hand},
                'third_person': {'scale': off_hand_tp}
            }
        }
    }
    return render_offsets

def main():
    image_path = filedialog.askopenfilename()
    if not image_path.endswith('.png'):
        print("Please, select a .png texture!")
    else:
        (image_width, image_height) = Image.open(image_path).size
        if image_width != image_height:
            print("Your texture height and size need to be the same!")
        else:
            image_size = image_height
            render_offsets = create_render_offsets(image_size)
            render_offsets_output_path = os.path.join(os.getcwd(), 'render_offsets.txt')
            with open(render_offsets_output_path, 'w') as render_offsets_output_file:
                json.dump(render_offsets, render_offsets_output_file, indent=4)
            print(json.dumps(render_offsets, indent=4))
            print("Your render offsets have also been written to file in the same folder this script is.")
    print("Thank you for using this render offsets generator. Created by MJ105#0448.")


if __name__ == '__main__':
    main()