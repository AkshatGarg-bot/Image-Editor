from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
from app import app


def b_w(path, filename):
    im = Image.open(path)
    bw = im.convert('L')
    bw.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def flip(path, filename):
    im = Image.open(path)
    image_flip = im.transpose(Image.FLIP_LEFT_RIGHT)
    image_flip.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def blur(path, filename):
    im = Image.open(path)
    im = im.convert('RGB')
    im_blur = im.filter(ImageFilter.GaussianBlur(radius=5))
    im_blur.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def contrast(path, filename):
    im = Image.open(path)
    ImageEnhance.Contrast(im)
    im.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def rotate(path, filename):
    im = Image.open(path)
    im_r = im.rotate(90)
    im_r.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def edge_enhance(path, filename):
    im = Image.open(path)
    im = im.convert('RGB')
    edg_enh = im.filter(ImageFilter.EDGE_ENHANCE)
    edg_enh.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def smooth(path, filename):
    im = Image.open(path)
    im = im.convert('RGB')
    im_smooth = im.filter(ImageFilter.SMOOTH)
    im_smooth.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def emboss(path, filename):
    im = Image.open(path)
    im = im.convert('RGB')
    im_emboss = im.filter(ImageFilter.EMBOSS)
    im_emboss.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def sharpen(path, filename):
    im = Image.open(path)
    im = im.convert('RGB')
    im_sharp = im.filter(ImageFilter.SHARPEN)
    im_sharp.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def find_edges(path, filename):
    im = Image.open(path)
    im = im.convert('RGB')
    im_edge = im.filter(ImageFilter.FIND_EDGES)
    im_edge.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def resize_360(path, filename):
    im = Image.open(path)
    im.thumbnail((360, 360))
    im.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def resize_720(path, filename):
    im = Image.open(path)
    im.thumbnail((720, 720))
    im.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def contour(path, filename):
    im = Image.open(path)
    im = im.convert('RGB')
    im_con = im.filter(ImageFilter.CONTOUR)
    im_con.save(os.path.join(app.config["FILTERED_IMAGES"], filename))


def negative(path, filename):
    im = Image.open(path)
    im = im.convert('RGB')
    im_neg = ImageOps.invert(im)
    im_neg.save(os.path.join(app.config["FILTERED_IMAGES"], filename))
