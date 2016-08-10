import os
import uuid
from flask import Flask


app = Flask(__name__)
my_uuid = str(uuid.uuid1())
ORANGE = "#fa5a00"
GREEN = "#33CC33"

COLOR = ORANGE
counter = 0 


@app.route('/')
def hello():
    global counter
    counter += 1
    if counter %2 == 0:
        COLOR = GREEN
    else:
        COLOR = ORANGE
    
    return """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="black">Hi, I'm GUID:<br/>
    {}</br>
    
    <br>
    
    Page Hit Count {}

    </center>
    <br>

    </body>
    </html>
    """.format(COLOR,my_uuid,counter)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
