from flask import Flask, request, render_template
import pickle

modelo = pickle.load(open('../../models/modelo.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html', titulo="Airline Passenger Satisfaction")
    #return "API"

#@app.route('/soma/<int:valor>')
#def soma(valor):
#    return "Resultado: {}".format(valor+5)

@app.route('/predicaoform', methods=['POST'])
def form():
    r1 = request.form['r1']
    r2 = request.form['r2']
    r3 = request.form['r3']
    r4 = request.form['r4']
    r5 = request.form['r5']
    r6 = request.form['r6']
    r7 = request.form['r7']
    r8 = request.form['r8']
    r9 = request.form['r9']
    r10 = request.form['r10']
    r11 = request.form['r11']
    r12 = request.form['r12']
    r13 = request.form['r13']
    r14 = request.form['r14']
    r15 = request.form['r15']
    r16 = request.form['r16']
    r17 = request.form['r17']

    result = modelo.predict([[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17]])

    #if result[0]==0:
    #    resultado = 'Neutral ou dissatisfied'
    #elif result[0]==1:
    #    resultado = 'Satisfied'
    
    return render_template('resultado.html', titulo = "Previsão", resultado = result)


#@app.route('/predicao/<float:v1>/<float:v2>/<float:v3>/<float:v4>/<float:v5>/<float:v6>/<float:v7>/<float:v8>/<float:v9>/<float:v10>/<float:v11>/<float:v12>/<float:v13>/<float:v14>/<float:v15>/<float:v16>/<float:v17>/')
#def predicao(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17):
#    resultado = modelo.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17]])
#    return "Classe: {}".format(resultado)

#@app.route('/predicao2/', methods = ['POST'])
#def predicao2():
#    dados = request.get_json()
#    colunas = ['seila1','seila2','seila3','seila3','seila5','seila6','seila7','seila8','seila9','seila10','seila11','seila12','seila13','seila14','seila15','seila16','seila17']
#    dados_input = [dados[col] for col in colunas]
#    result = modelo.predict([dados_input])
#    return "Classe: {}".format(result)

app.run(debug=True)