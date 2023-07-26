from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "Hello IT School, this is my project :)";  
  
if __name__ =='__main__':  
    app.run(debug = True)  