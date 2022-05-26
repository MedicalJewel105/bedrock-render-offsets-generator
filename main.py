from tkinter import filedialog
from PIL import Image
import json
import os


def create_render_offsets(image_size):
    default_render_offsets_values = [0.075, 0.125]
    render_offsets_scales = [
        default_render_offsets_values[0]/(image_size/16),
        default_render_offsets_values[1]/(image_size/16),
        default_render_offsets_values[0]/(image_size/16)
    ]
    render_offsets = {
        'minecraft:render_offsets': {
            'main_hand': {
                'first_person': {'scale': render_offsets_scales},
                'third_person': {'scale': render_offsets_scales}
            },
            'off_hand': {
                'first_person': {'scale': render_offsets_scales},
                'third_person': {'scale': render_offsets_scales}
            }
        }
    }
    render_offsets_json = json.dumps(render_offsets, indent=4)
    print("Generated render offsets:\n", render_offsets_json)
    render_offsets_output_file_path = os.getcwd() + '/render_offsets.json'
    with open(render_offsets_output_file_path, 'w') as render_offsets_output_file:
        json.dump(render_offsets, render_offsets_output_file, indent=4)
        print("Your render offsets have also been written to file in the same folder this script is.")


image_path = filedialog.askopenfilename()

if not image_path.endswith('.png'):
    print("Please, select a .png texture!")
else:
    (image_width, image_height) = Image.open(image_path).size
    if image_width != image_height:
        print("Your texture height and size need to be the same!")
    else:
        image_size = image_height
        create_render_offsets(image_size)

print("Thank you for using this render offsets generator. Created by MJ105#0448.")