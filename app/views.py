from flask import render_template
from flask import request
from app import app
import test

defaultpath = '/Users/foresummer/trypython/app'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', user_name='weigy14')

@app.route('/search', methods=['GET'])
def search_page():
	return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
	if request.method == 'POST':
		query = request.form['imgurl']
		print request.form['imgurl']
		if query[1:6] == 'static':
			query = defaultpath + squery
		result = test.just_for_fun(query)
	return render_template('result.html', 
		query_url= query,
		query_type= result[0],
		result1_url= result[1],
		result2_url= result[2],
		result3_url= result[3],
		result4_url= result[4],
		result5_url= result[5],
		result6_url= result[6],
		result7_url= result[7],
		result8_url= result[8],
		result9_url= result[9],
		result10_url= result[10])

@app.route('/result', methods=['GET', 'POST'])
def result():
	return 'result'

