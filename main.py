from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify, render_template
import os
from core.core import agent
os.environ["HTTP_PROXY"] = os.environ['PROXY_URL']
os.environ["HTTPS_PROXY"] = os.environ['PROXY_URL']

app = Flask(__name__)
context = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/xuxu', methods = ['POST'])
def xuxu():
    global context
    name = request.form.get("name")
    print("xu print name is: ", name)

    # Add the human input to the context
    context.append(("human", name))
    context_str = " ".join([f"{role}: {text}" for role, text in context ])

    result = agent(name, context=context_str)
    print("Xuan print result: ", result)

    ## add in ai respone
    context.append(("ai", result))
    print("history is: ", context)


    return jsonify({
        "result": result,
        "history" : context
    })

if __name__ == "__main__":
    app.run(host= "0.0.0.0", debug=True)