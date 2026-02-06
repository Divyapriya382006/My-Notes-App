from flask import Flask, redirect,render_template,url_for,session,request
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)

app.secret_key = "babyshark"


supabase: Client=create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

print(os.getenv("SUPABASE_URL"))
print(os.getenv("SUPABASE_KEY"))


print("FLASK FILE LOADED")

@app.route("/landing")
def index():
    return render_template("landing.html")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            res=supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            print("SUPABASE LOGIN SUCCESS")

            session["access_token"] = res.session.access_token
            session["user_id"]=res.user.id
            return redirect(url_for("index"))

        except Exception as e:
            print("SUPABASE LOGIN FAILED:", e)

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            supabase.auth.sign_up({
                "email": email,
                "password": password
            })
            print("SUPABASE SIGNUP SUCCESS")
            return redirect("/login")

        except Exception as e:
            print("SUPABASE SIGNUP FAILED:", e)

    return render_template("signup.html")


@app.route("/inputpg", methods=["GET", "POST"])
def inputpg():
    if request.method == "POST":
        access_token = session.get("access_token")
        user_id = session.get("user_id")

        print("SESSION USER:", user_id)

        if "user_id" not in session:
          return redirect(url_for("login"))


        

        date_value = request.form.get("date")
        if date_value == "":
          date_value = None

        supabase.table("Contents").insert({
    "user_id": user_id,
    "Name": request.form.get("name"),
    "Date": date_value,
    "Category": request.form.get("category"),
    "Content": request.form.get("content")
}).execute()
        return redirect(url_for("contentspg"))

    return render_template("inputpg.html")


@app.route("/contentspg")
def contentspg():
    if "user_id" not in session:
        return redirect(url_for("login"))

    res = supabase.table("Contents") \
        .select("*") \
        .eq("user_id", session["user_id"]) \
        .order("id", desc=True) \
        .execute()

    return render_template("contentspg.html", notes=res.data)


@app.route("/note/<int:note_id>")
def note(note_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    res = supabase.table("Contents") \
        .select("*") \
        .eq("id", note_id) \
        .eq("user_id", session["user_id"]) \
        .single() \
        .execute()

    note = res.data
    return render_template("note.html", notes=note)



if __name__=="__main__":
    app.run(debug=True)