from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('checkerboard.html', x=8, y=8)

@app.route('/<x>/<y>')
# Multiplying x and y by 100 to help with page sizing since each square = 100px
def defineableBoard(x,y):
    x=int(x)
    y=int(y)
    return render_template('checkerboard.html', x=x, y=y)
    
if __name__ == '__main__':
    app.run(debug=True)
