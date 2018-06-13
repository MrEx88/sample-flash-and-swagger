from flask import render_template
import connexion

# create app instance
app = connexion.App(__name__, specification_dir='./')

# read the swagger.yml file to configure endpoints
app.add_api('swagger.yml')

# create URL route for "/"
@app.route('/')
def home():
    """Returns home.html
    """
    return render_template('home.html')
    
    
# run if in stand alone mode
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
