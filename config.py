from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEYS']="azertyqwerty"
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:@localhost/order-dba"

db = SQLAlchemy(app)