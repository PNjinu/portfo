from flask import Flask, render_template, request, redirect
import os
import csv

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def my_home():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            message = "Thank you for sending me a message, I will get back ASAP."
            return render_template('index.html', message=message)
        except Exception as e:
            message = f"Did not save to database: {e}"
            return message
    else:
        return render_template('index.html')

    

# This will be replaced when database is set up.
def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])


if __name__ == "__main__":
    app.run(debug=True)