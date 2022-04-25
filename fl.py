from gc import get_stats
from flask import (
    Flask,
    session,
    render_template,
    request,
    escape,
    redirect,
    url_for,
    flash,
)
from gen import *
from models import *
from storage import *

app = Flask(__name__)
app.secret_key = "secret_key"
USER_STORAGE = "./users_storage.json"
STORAGE = "./storage.json"
STATS_STORAGE = "./stats_storage.json"

get_data_from_storage(USER_STORAGE, users_storage)
get_data_from_storage(STORAGE, storage)
get_data_from_storage(STATS_STORAGE, stats_storage)


def get_user_by_name(name):
    for v in users_storage.values():
        if v["name"] == name:
            return v
    return None


def auth_user(name, password: str) -> dict:
    user = get_user_by_name(name)
    if user is None:
        return None
    if user["password"] == password:
        return user["id"]
    return None


def gen_id() -> int:
    if users_storage == {}:
        return 1
    last_id = max(users_storage.items(), key=lambda x: x[0])
    return int(last_id[0]) + 1


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/", methods=["GET", "POST"])
def index():
    shortened = ""
    if request.method == "POST":
        raw = request.form.get("origin")
        shortened = generate(raw)
        storage[shortened] = raw
        store_data(STORAGE, storage)
    return render_template("index.html", shortened=shortened)


def get_stats(shortened: str):
    get_data_from_storage(STATS_STORAGE, stats_storage)
    data = stats_storage.get(shortened, {})
    return data


def set_stats(shortened: str, data: dict):
    stats_storage[shortened] = data
    store_data(STATS_STORAGE, stats_storage)


@app.route("/shrt/<shortened>/")
def to_real_url(shortened):
    sh = escape(shortened)
    raw = storage.get(sh, "/")
    data = Stats(shortened, get_stats(shortened))
    data.add_redirect()
    data.last_redirect()
    set_stats(shortened, data.to_dict())
    return redirect(raw)


def check_user(name: str) -> bool:
    """Checks if user in storage. Returns True if it is"""
    for k, v in users_storage.items():
        if name == v["name"]:
            return True
    return False


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        log = request.form.get("btn_ok")
        id = None
        if log is not None:
            id = auth_user(name, password)
            if id == None:
                flash("Неверный логин или пароль", "warning")
        else:
            if not check_user(name):
                id = gen_id()
                u = User(id, name, password)
                users_storage[id] = u.to_dict()
            else:
                flash("Такой пользователь уже существует", "warning")
        if id != None:
            session["id"] = id
            session["name"] = name
            store_data(USER_STORAGE, users_storage)
            return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/shrt/<shortened>/stats")
def stats_handler(shortened):
    d = get_stats(shortened)
    return render_template("stats.html", data=d)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
