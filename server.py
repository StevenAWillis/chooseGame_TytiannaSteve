from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def home():
    name = "Steebo"

    print ("////////////////////////////////////")
    return render_template('index.html', context = name)


@app.route('/story')
def story():
    print ("////////////////////////////////////")
    return render_template('story.html')


@app.route('/storya')
def storya():
    print ("////////////////////////////////////")
    return render_template('storya.html')

@app.route('/storyb')
def storyb():
    print ("////////////////////////////////////")
    return render_template('storyb.html')

@app.route('/storya_2')
def storya_2():
    print ("////////////////////////////////////")
    return render_template('storya_2.html')

@app.route('/storyb_2')
def storyb_2():
    print ("////////////////////////////////////")
    return render_template('storyb_2.html')

@app.route('/storyb_2_a')
def storyb_2_a():
    print ("////////////////////////////////////")
    return render_template('storyb_2_a.html')

@app.route('/storyb_2_b')
def storyb_2_b():
    print ("////////////////////////////////////")
    return render_template('storyb_2_b.html')






app.run(debug=True)