from flask import Flask, render_template, request

app = Flask(__name__)

# Simple rule-based responses
responses = {
    "hello": "Hello! How can I help you?",
    "how are you": "I'm just a computer program, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg').lower()  
    
    if userText in responses:
        return responses[userText]
    else:
        return render_template("form.html")

@app.route("/submit_form", methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    phoneNumber = request.form.get('password')
    message=request.form.get('message')

    
    # Here you can store the user's data in a database or perform any other action
    return f"""Thank you, Thank you for Your greate response Our Team will reach you 
    {message}"""

if __name__ == "__main__":
    app.run(debug=True)