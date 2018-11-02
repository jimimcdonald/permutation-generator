from flask import Flask, render_template, request

from permutation import Permutate

app = Flask(__name__)

@app.route('/')
def permutations():
    return render_template("permutations.html")

@app.route("/permutation_results/", methods=['POST', 'GET'])
def permutation_results():
    if request.method=='POST':
        word1=request.form["word_1"]
        word2=request.form["word_2"]
        word3=request.form["word_3"]
        word4=request.form["word_4"]
        word5=request.form["word_5"]
        word6=request.form["word_6"]
        words = [word1,word2,word3,word4,word5,word6]
        perms=Permutate(word1,word2,word3,word4,word5,word6)

        return render_template("permutation_results.html", permutation_results = perms,
        word1=word1,word2=word2,word3=word3,
        word4=word4,word5=word5,word6=word6)

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)
