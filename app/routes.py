from app import app
from flask import request, redirect, render_template, send_from_directory, url_for
import os
from werkzeug.utils import secure_filename
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
from app.functions import *
import datetime

app.config["UPLOADED_IMAGES"] = "/home/akshat/app/app/uploads"
app.config["ALLOWED"] = ["png", "jpg", "jpeg"]
app.config["FILTERED_IMAGES"] = "/home/akshat/app/app/downloads"


def is_allowed(filename):
    if not "." in filename:
        return False

    external = os.path.splitext(filename)[1][1:]

    if external.lower() in app.config["ALLOWED"]:
        return True

    else:
        return False


@app.route("/", methods=["GET", "POST"])
def image_upload():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]

            if image.filename == "":
                print("The image must have a filename")
                return redirect(request.url)

            if is_allowed(image.filename) == False:
                print("That image extension is not allowed")
                return redirect(request.url)

            else:
                file_name = secure_filename(image.filename)
                file_name = os.path.splitext(file_name)[0] + str(datetime.datetime.now()) + "." + os.path.splitext(file_name)[1][1:]

                image.save(os.path.join(app.config["UPLOADED_IMAGES"], file_name))

                if request.form.get("filter") == "1":
                    b_w(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "2":
                    blur(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "3":
                    contrast(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "4":
                    flip(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "5":
                    rotate(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "6":
                    resize_360(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "7":
                    resize_720(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "8":
                    edge_enhance(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "9":
                    emboss(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "10":
                    contour(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "11":
                    find_edges(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "12":
                    smooth(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "13":
                    sharpen(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

                elif request.form.get("filter") == "14":
                    negative(os.path.join(
                        app.config["UPLOADED_IMAGES"], file_name), file_name)
                    if request.form.get("filtered_image") == "15":
                        return redirect(url_for('download_image', filename=file_name))

                    else:
                        return render_template("uploaded.html", image_name=file_name)

    return render_template("index.html")


@app.route("/uploads/<filename>")
def download_image(filename):
    return send_from_directory(app.config["FILTERED_IMAGES"], filename, as_attachment=True)


@app.route("/filtered_image/<filename>")
def display_image(filename):
    return send_from_directory(app.config["FILTERED_IMAGES"], filename, as_attachment=False)
