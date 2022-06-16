# Bedrock Render Offsets Generator

Generates render offsets for MC Bedrock.
Created by MedicalJewel105 a.k.a MJ105#0448

# What is render_offsets

If you are an add-on creator and you want to add an item (1.16.100+) with texture bigger than 16x16, you will need to add render offsets to your item so it renders correctly in-game. Render offsets component is in your item's code, in components.
You can see render offsets syntax [here](https://wiki.bedrock.dev/items/items-16.html#minecraft-render-offsets).

# How to use

Warning: This script requires [Pillow](https://pypi.org/project/Pillow/) library.
You will need to run `pip install -r requirements.txt` in the directory of this script.
Clone this repository and run `main.py`. It should ask you to open your texture file, if not - re-run the script. You can see the result in terminal or in render_offsets.json file in the same folder script is.