'''
This program is to find the Flames between the couples
'''

from flask import Flask, render_template, redirect, url_for, request

#app = Flask(__name__)
app = Flask(__name__, static_url_path='/static', static_folder='static')


@ app.route('/')

def index():
    #Function to Display index.html file in browser

    return render_template('index.html')

@ app.route('/result/<name>')

def result (name):

    #Function to Display result.html file in browser with name as an argument

    return render_template('result.html', relation=name)

@ app.route('/check_flames', methods=['POST', 'GET'])

def check_flames():

    #Performs the main process (checks the relation)

    #Getting Input
    if request.method == 'POST':
        couple1 = request.form['Couple1']
        couple2 = request.form['Couple2']
    else:
        couple1 = request.args.get('Couple1')
        couple2 = request.args.get('Couple2')

    strcouple1 , strcouple2 = couple1,couple2
    couple1 = couple1.lower()
    couple2 = couple2.lower()

    couple1 = couple1.replace(" ","")
    couple2 = couple2.replace(" ","")

    couple1 = list(couple1)
    couple2 = list(couple2)

    couple1.sort()
    couple2.sort()

    
    
    # Striking the Letter matches in couple1 and couple2
    for letter in couple1:
        if letter in couple2:
            couple1.remove(letter)
            couple2.remove(letter)
    
    for letter in couple2:
        if letter in couple1:
            couple1.remove(letter)
            couple2.remove(letter)

    # total no from the process side        
    total = len(couple1) + len(couple2)


    # main process for checking the desired output for given names
    parseString = ['f','l','a','m','e','s']
    while(len(parseString) != 1):
        #print(parseString)
        rem_idx = total % len(parseString) - 1
        #print(rem_idx)
        parseString.pop(rem_idx)
        if rem_idx != -1:
            parseString = parseString[rem_idx:] + parseString[:rem_idx]
            
    # output side 
    choice = parseString[0]

    if choice == 'f' :
        res = redirect(url_for('result', name= "FRIENDSHIP"))
        #print("The Relation Between {} and {} is \" FRIENDSHIP \"".format(strcouple1.capitalize(),strcouple2.capitalize()))
    elif choice == 'l' :
        res = redirect(url_for('result', name= "LOVE"))
        #print("The Relation Between {} and {} is \" LOVE \"".format(strcouple1.capitalize(),strcouple2.capitalize()))
    elif choice == 'a' :
        res = redirect(url_for('result', name= "AFFECTION"))
        #print("The Relation Between {} and {} is \" AFFECTION \"".format(strcouple1.capitalize(),strcouple2.capitalize()))
    elif choice == 'm' :
        res = redirect(url_for('result', name= "MARRIAGE"))
        #print("The Relation Between {} and {} is \" MARRIAGE \"".format(strcouple1.capitalize(),strcouple2.capitalize()))
    elif choice == 'e' :
        res = redirect(url_for('result', name= "ENEMY"))
        #print("The Relation Between {} and {} is \" ENEMY \"".format(strcouple1.capitalize(),strcouple2.capitalize()))
    elif choice == 's' :
        res = redirect(url_for('result', name= "SISTER"))
        #print("The Relation Between {} and {} is \" SISTER \"".format(strcouple1.capitalize(),strcouple2.capitalize()))
    else:
        pass

    return res


if __name__ == '__main__':
    app.run(debug = True)
    
    