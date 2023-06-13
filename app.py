from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS =[{
  'id':1,
  'title':'Data Analyst',
  'location':'Birmingham, UK',
  'salary':'Rs. 100,000'
},
      {
  'id':2,
  'title':'Data Scientist',
  'location':'Manchester, UK',
  'salary':'Rs. 150,000'
      },
      {
  'id':3,
  'title':'Frontend Engineer',
  'location':'Birmingham, UK',
  'salary':'& 175,000'
      },
      {
  'id':4,
  'title':'Backend Engineer',
  'location':'California, USA',
  'salary':'$ 150,000'
      }
     
]

@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
