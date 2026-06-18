from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import url_for

from middleware import admin_required

from database.db import db

from models.category import Category

from . import admin_bp


@admin_bp.route("/categories")
@admin_required
def categories():

    categories = Category.query.order_by(
        Category.name.asc()
    ).all()

    return render_template(
        "admin/categories/index.html",
        categories=categories
    )


@admin_bp.route(
    "/categories/create",
    methods=["GET", "POST"]
)
@admin_required
def create_category():

    if request.method == "POST":

        category = Category(
            name=request.form.get("name"),
            description=request.form.get(
                "description"
            )
        )

        db.session.add(category)

        db.session.commit()

        flash(
            "Category created successfully.",
            "success"
        )

        return redirect(
            url_for(
                "admin.categories"
            )
        )

    return render_template(
        "admin/categories/create.html"
    )