from flask import render_template
import connexion

# Create instance
app = connexion.App(__name__, specification_dir='./')

# Read swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route for "/"
@app.route('/')
def home():

#    localhost:5000/

    return render_template('home.html')

# in stand-alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)