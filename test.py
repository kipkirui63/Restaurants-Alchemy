from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Create a database connection
engine = create_engine('sqlite:///restaurant_reviews.db')  # Adjust the database URI

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Test your models and methods here
# Example: Retrieve all restaurants and print their names
restaurants = session.query(Restaurant).all()
for restaurant in restaurants:
    print(f"Restaurant: {restaurant.name}")

# Don't forget to close the session when you're done
session.close()
