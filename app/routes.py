from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
from werkzeug.utils import secure_filename

from .models import db, User, Article
from .storage import upload_image

main = Blueprint("main", __name__)

# ---------------- LOGIN ----------------
@main.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(
            username=username,
            password=password
        ).first()

        if user:
            session["user"] = user.username
            return redirect(url_for("main.create_article"))

    return render_template("login.html")


# ---------------- CREATE ARTICLE ----------------
@main.route("/create", methods=["GET", "POST"])
def create_article():
    if "user" not in session:
        return redirect(url_for("main.login"))

    if request.method == "POST":
        # ✅ Validate image
        image = request.files.get("image")
        if not image or image.filename == "":
            return "No image uploaded", 400

        # ✅ Sanitize filename
        image.filename = secure_filename(image.filename)

        # ✅ Upload to Azure Blob
        image_url = upload_image(
            image,
            current_app.config["BLOB_CONNECTION_STRING"],
            current_app.config["BLOB_CONTAINER"]
        )

        # ✅ Save article
        article = Article(
            title=request.form.get("title"),
            author=request.form.get("author"),
            body=request.form.get("body"),
            image=image_url
        )

        db.session.add(article)
        db.session.commit()

        return redirect(url_for("main.view_article", article_id=article.id))

    return render_template("create.html")


# ---------------- VIEW ARTICLE ----------------
@main.route("/article/<int:article_id>")
def view_article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template("article.html", article=article)
