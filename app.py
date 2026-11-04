def main():
	print("Employee Management Portal")

if __name__ == "__main__":
      	main()

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Employee Management Portal"

@app.route('/employees')
def employees():
   return "Employee Management System"

if __name__ == '__main__':
   app.run(debug=True)
