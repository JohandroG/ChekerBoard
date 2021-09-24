from flask import Flask
from flask import render_template

app = Flask( __name__ )


@app.route ('/' ,methods=['GET'])
def board1():

    xnumMax = 8
    ynumMax = 8

    return render_template ('index.html', xmax = xnumMax, ymax = ynumMax)

@app.route ('/4' ,methods=['GET'])
def board2():

    xnumMax = 8
    ynumMax = 4

    return render_template ('index.html', xmax = xnumMax, ymax = ynumMax)


@app.route ('/<x>/<y>' ,methods=['GET'])
def board(x,y):

    xnumMax = int(x)
    ynumMax = int(y)


    return render_template ('index.html', xmax = xnumMax, ymax = ynumMax)



if __name__ == "__main__":
    app.run( debug = True )

