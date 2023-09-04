from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review  # Adjust the import path based on your project structure

# Create a database connection
engine = create_engine('sqlite:///restaurant_reviews.db')  # Adjust the database URI

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create sample instances
restaurant1 = Restaurant(name="Athi", price=3)
restaurant2 = Restaurant(name="Mara", price=2)
customer1 = Customer(first_name="Kimno", last_name="Nganga")
customer2 = Customer(first_name="Anton", last_name="Chupa")

# Add instances to the session
session.add_all([restaurant1, restaurant2, customer1, customer2])

# Commit the changes to the database
session.commit()

# Create sample reviews
review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer1)
review3 = Review(star_rating=3, restaurant=restaurant1, customer=customer2)
review4 = Review(star_rating=4, restaurant=restaurant2, customer=customer2)

# Add reviews to the session
session.add_all([review1, review2, review3, review4])

# Commit the changes to the database
session.commit()

# Close the session
session.close()
