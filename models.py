from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a database engine
engine = create_engine('sqlite:///restaurant_reviews.db')  

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define the base class for declarative models
Base = declarative_base()

# Define table models with autoload=True to reflect existing schema
class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
    # Define a relationship to any related tables (e.g., reviews)
    reviews = relationship('Review', back_populates='customer')
    
class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    
    # Define a relationship to customers and reviews
    customers = relationship('Customer', secondary='reviews')
    reviews = relationship('Review', back_populates='restaurant')
    
class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)  # Add the star_rating column definition
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    

    def __init__(self, star_rating, restaurant, customer):
        self.star_rating = star_rating
        self.restaurant = restaurant
        self.customer = customer
    
    # Define foreign keys to customer and restaurant
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    
    # Define relationships to customer and restaurant
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

# Create all tables in the database
Base.metadata.create_all(engine)

# Insert data into the 'customers' table
new_customer = Customer(first_name='Kimno', last_name='Nganga')
session.add(new_customer)
session.commit()

# Close the session
session.close()
