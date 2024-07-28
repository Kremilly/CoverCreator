# CoverCreator

The tool that allows you to create a custom cover image using a background image, scaling it to a specified percentage, adding overlaid text, and saving the output as an image file.

## Getting Started

Clone this repository

```shell
git clone https://github.com/kremilly/CoverCreator.git
cd CoverCreator
```

Install the dependencies using PIP

```shell
pip install -r requirements.txt
```

## Usage

```bash
python covercreator -i <Image_URL> -s <Font_Size> -t <Text> -o <Output_File_Name>
```

## Parameters

- `-i <Image_URL>`: Specifies the URL of the background image to be used for creating the cover.
- `-s <Font_Size>`: Defines the font size for the overlaid text.
- `-t <Text>`: Specifies the text to be overlaid on the background image.
- `-o <Output_File_Name>`: Defines the name of the output image file.

## Usage Example

To create a cover using the image available at `https://kremilly.com/static/images/post-bg.png`, with a font size of 50, adding the text "Test", and saving the file as `cover.png`, use the following command:

```bash
python covercreator -i https://kremilly.com/static/images/post-bg.png -s 50 -t Test -o cover.png
```
