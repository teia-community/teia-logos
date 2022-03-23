""" Teia logos submissions checker

Usage:
    [NOT USABLE WITHOUT TEIA's GOOGLE RIGHTS]
    install rclone
    pip install pillow
    python sync.py <OPTIONS>

Options:
    -c,     Make contact sheet from all submissions
    -d,     Download submissions
    -q,     Do not print anything from gdown

Author:
    © mel https://teia.art/mel

"""
import subprocess
# import gdown
import sys
import os
import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import datetime


fontFile = os.path.join(os.path.dirname(__file__),"IBMPlexMono-Bold.otf")
# get a font
fontT = ImageFont.truetype(fontFile, 8)


def make_contact_sheet(
    fnames,
    ncols,
    nrows,
    photow,
    photoh,
    marl=5,
    mart=5,
    marr=5,
    marb=5,
    padding=1,
    bg=(255, 255, 255),
):
    # Read in all images and resize appropriately
    img_dict = {
        fn: ImageOps.expand(
            Image.open(fn).resize((photow, photoh)),
            border=20,
            fill=bg,
        )
        for fn in fnames
    }

    photoh = photoh + 40
    photow = photow + 40

    # Calculate the size of the output image, based on the
    # photo thumb sizes, margins, and padding
    marw = marl + marr
    marh = mart + marb

    padw = (ncols - 1) * padding
    padh = (nrows - 1) * padding
    isize = (ncols * photow + marw + padw, nrows * photoh + marh + padh)

    # Create the new image to store the contact sheet
    inew = Image.new("RGB", isize, bg)

    # Insert each thumb:
    for irow in range(nrows):
        for icol in range(ncols):
            left = marl + icol * (photow + padding)
            right = left + photow
            top = mart + irow * (photoh + padding)
            bottom = top + photoh
            bbox = (left, top, right, bottom)
            try:
                name, img = img_dict.popitem()
            except Exception as e:
                print(f"Error occured: {e}")
                break

            # initialized to transparent text color
            info_image = Image.new(
                "RGBA", (img.width, img.height), (0, 0, 0, 0)
            )

            # get a drawing context
            d = ImageDraw.Draw(info_image)
            redu = 60
            # d.rectangle(
            #     ((0 + redu, img.height-15), (img.width- redu, img.height)),
            #     fill=(0, 0, 0, 255),
            #     outline=None,
            #     width=0,
            # )
            name = os.path.basename(name)
            new_text = ".".join(name.split(".")[:-1])

            # inew.paste(img, bbox)
            w, h = d.textsize(new_text)

            d.text(
                (redu / 2 + ((img.width - redu) - w) / 2, img.height - 10),
                new_text,
                font=fontT,
                fill="white" if bg == "black" else "black",
                align="center",
            )

            # Paste the photo into the output image
            inew.paste(img, bbox, img.convert("RGBA"))
            # Paste the text into the output image
            inew.paste(info_image, bbox, info_image.convert("RGBA"))
    return inew


if __name__ == "__main__":

    quiet = False

    if "-q" in sys.argv:
        quiet = True
        sys.argv.remove("-q")

    # urls = {
    #     "dark": "1PVn8Q_JJFCbo0FM8oNpftiOeAI5vkNJo",
    #     "light": "15UIPJeE2uUyrVryTxkP1guc7aCxjOIOv",
    # }
    urls = {
        "dark": "approved_conformed_dark",
        "light": "approved_conformed_light",
    }

    if "-d" in sys.argv:
        sys.argv.remove("-d")

        for key, value in urls.items():
            # if not quiet:
            #     print("Downloading {}...".format(key))
            # gdown.download_folder(
            #     f"https://drive.google.com/drive/folders/{value}",
            #     output=key,
            #     quiet=quiet,
            # )
            out_dir = f"dist/logos/{key}"
            subprocess.call("/usr/local/bin/rclone copy teia-remote:'{}' --drive-shared-with-me {} ".format(value, out_dir), shell=True)
            # rename to lowercase
            files = [x for x in os.listdir(out_dir) if x.endswith(".png")]
            for file in files:
                filename = os.path.join(out_dir, file.lower())
                os.rename(os.path.join(out_dir, file), filename)
                if "-r" in sys.argv:
                    # breaks apngs
                    im = Image.open(filename)
                    width, height = im.size
                    new_width = 256
                    new_height = new_width * height // width
                    im1 = im.resize((new_width, new_height), Image.ANTIALIAS)
                    im1.save(filename)

    if "-c" in sys.argv:
        for key, _ in urls.items():
            out_dir = f"dist/logos/{key}"
            files = [
                os.path.join(out_dir, x)
                for x in os.listdir(out_dir)
                if x.endswith(".png")
            ]

            photow, photoh = 256, 64
            margins = [5, 5, 5, 5]
            col = 4
            row = len(files) // col
            padding = 1
            inew = make_contact_sheet(
                files,
                col,
                row,
                photow,
                photoh,
                margins[0],
                margins[1],
                margins[2],
                margins[3],
                padding,
                "black" if key == "dark" else "white",
            )
            inew.save(f"dist/contact-sheet/{key}.png")

    logos_light = [x for x in os.listdir("dist/logos/light") if x.endswith(".png")]
    logos_dark = [x for x in os.listdir("dist/logos/dark") if x.endswith(".png")]

    # same lenght
    assert len(logos_light) == len(logos_dark)

    # matchig counterpart
    assert logos_light == logos_dark

    logos = [x for x in os.listdir("dist/logos/dark") if x.endswith(".png")]
    logos.sort()
    now = datetime.datetime.now()
    # TODO: add date to json
    with open("dist/logos.json", "w") as logo:
        json.dump(
            {
                "logos": logos,
                "sync_date": now.strftime("%Y-%m-%d %H:%M:%S"),
                "count": len(logos),
            },
            logo,
        )
