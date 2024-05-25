from flask import Flask,request,render_template
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app=Flask(__name__)


## Route for a home page

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    else:
        return render_template('home.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')

    else:
        data=CustomData(
            position=request.form.get('position'),
            height=float(request.form.get('height')),
            age=float(request.form.get('age')),
            appearance=float(request.form.get('appearance')),
            goals=float(request.form.get('goals')),
            assists=float(request.form.get('assists')),
            yellow_cards=float(request.form.get('yellow_cards')),
            second_yellow_cards=float(request.form.get('second_yellow_cards')),
            red_cards=float(request.form.get('red_cards')),
            goals_conceded=float(request.form.get('goals_conceded')),
            clean_sheets=float(request.form.get('clean_sheets')),
            minutes_played=float(request.form.get('minutes_played')),
            days_injured=float(request.form.get('days_injured')),
            games_injured=float(request.form.get('games_injured')),
            award=float(request.form.get('award')),
            highest_value=float(request.form.get('highest_value'))
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('end.html',results='{:.2f}'.format(results[0]/1000000))
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)      