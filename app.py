from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for daily routines (to be replaced with database later)
daily_routines = []

# Home route
@app.route('/')
def home():
    return render_template('index.html', routines=daily_routines)

# Route to add a new daily routine
@app.route('/add_routine', methods=['POST'])
def add_routine():
    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    due_time = request.form['due_time']

    new_routine = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'due_time': due_time
    }

    daily_routines.append(new_routine)

    return render_template('index.html', routines=daily_routines)

if __name__ == '__main__':
    app.run(debug=True)

