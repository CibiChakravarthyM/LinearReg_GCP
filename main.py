import pickle

from flask import Flask, render_template, request

application= Flask(__name__)
@application.route("/", methods=["GET"])
def homePage():
    return render_template("index.html")

@application.route("/predict", methods=["POST", "GET"])
def predictApp():
    if request.method== 'POST' :
        try:
            gre_score = float(request.form["gre_score"])
            toefl_score = float(request.form["toefl_score"])
            university_rating = float(request.form["university_rating"])
            sop = float(request.form["sop"])
            lor = float(request.form["lor"])
            cgpa = float(request.form["cgpa"])

            is_research = request.form['research']

            if is_research=="yes":
                research=1
            else:
                research=0

            filename= "finalized_model.pickle"
            loaded_file = pickle.load(open(filename, "rb"))
            predicted_point = loaded_file.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            print("TEST 1")
            print("predicted_point", predicted_point)
            print("TEST 2")
            print(predicted_point[0])

            predicted_value = round((predicted_point[0]*100),3)
            print("TEST 3")

            return render_template("results.html", prediction= predicted_value)
        except Exception as e:
            print("Error due to ", e)
            print("Something went wrong")

    else:
        return  render_template("index.html")


if __name__=="__main__":
    application.run(debug=True)