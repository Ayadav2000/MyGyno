
from flask import Blueprint, request, session, redirect, render_template
from werkzeug.security import check_password_hash
from ..models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u = User.query.filter_by(username=request.form["username"]).first()
        if u and check_password_hash(u.password_hash, request.form["password"]):
            session["user_id"] = u.id
            session["role"] = u.role
            return redirect("/doctor" if u.role=="doctor" else "/patient")
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
