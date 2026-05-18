from flask import Flask, render_template, request, session, redirect, url_for
from app.components.retriever import MedicalQAChain
from markupsafe import Markup
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize QA chain once
qa_chain = MedicalQAChain()


def nl2br(value):
    return Markup(value.replace("\n", "<br>\n"))


app.jinja_env.filters['nl2br'] = nl2br


@app.route("/", methods=["GET", "POST"])
def index():

    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":

        user_input = request.form.get("prompt")

        if user_input:

            messages = session["messages"]

            # Store user message
            messages.append({
                "role": "user",
                "content": user_input
            })

            # Get AI response
            result = qa_chain.ask(user_input)

            # Store assistant response
            messages.append({
                "role": "assistant",
                "content": result
            })

            session["messages"] = messages

        return redirect(url_for("index"))

    return render_template(
        "index.html",
        messages=session.get("messages", [])
    )


@app.route("/clear")
def clear():

    session.pop("messages", None)

    return redirect(url_for("index"))


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )