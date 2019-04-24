from flask import Flask, render_template, url_for

app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/all')
def all():
    return render_template('alleventheat.html')
 
@app.route('/g2')
def g2():
    return render_template('g2eventheat.html')

@app.route('/g3half')
def g3half():
    return render_template('g3halfeventheat.html')

@app.route('/depthm3half')
def depthm3half():
    return render_template('depthm3halfeventheat.html')

if __name__ == '__main__':
  app.run()