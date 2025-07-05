from flask import Flask, render_template, request, redirect, url_for, flash
from forms import LoginForm, SignupForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/')
def home():
    return render_template('home.html', title='Paradise Stay - Home')

@app.route('/rooms')
def rooms():
    rooms_data = [
        {
            'name': 'Deluxe Room',
            'description': 'King bed, sea view, free Wi-Fi, complimentary breakfast',
            'price': '₹3,999/night',
            'features': ['King Size Bed', 'Sea View', 'Free Wi-Fi', 'Complimentary Breakfast', 'Air Conditioning', 'Mini Bar']
        },
        {
            'name': 'Standard Room',
            'description': 'Queen bed, city view, air conditioning, free Wi-Fi',
            'price': '₹2,499/night',
            'features': ['Queen Size Bed', 'City View', 'Free Wi-Fi', 'Air Conditioning', 'Cable TV', 'Room Service']
        },
        {
            'name': 'Suite Room',
            'description': 'Spacious suite with separate living area, premium amenities',
            'price': '₹5,999/night',
            'features': ['Separate Living Area', 'Premium Amenities', 'Balcony', 'Complimentary Breakfast', 'Butler Service', 'Jacuzzi']
        }
    ]
    return render_template('rooms.html', title='Rooms & Rates', rooms=rooms_data)

@app.route('/menu')
def menu():
    menu_data = {
        'starters': [
            {'name': 'Tomato Basil Soup', 'description': 'Fresh tomatoes blended with basil and cream.', 'price': '₹120'},
            {'name': 'Paneer Tikka', 'description': 'Grilled cottage cheese with Indian spices.', 'price': '₹180'},
            {'name': 'Spicy Vegetable Pakora', 'description': 'Crispy fritters with seasonal vegetables and spices, served with tangy chutney.', 'price': '₹150'}
        ],
        'main_course': [
            {'name': 'Butter Chicken', 'description': 'Creamy tomato-based chicken curry.', 'price': '₹250'},
            {'name': 'Veg Biryani', 'description': 'Aromatic rice with mixed vegetables and spices.', 'price': '₹200'},
            {'name': 'Fish Curry', 'description': 'Fresh fish simmered in spicy coconut gravy, served with steamed rice.', 'price': '₹230'}
        ],
        'desserts': [
            {'name': 'Gulab Jamun', 'description': 'Soft milk-solid balls soaked in sugar syrup.', 'price': '₹90'},
            {'name': 'Ice Cream', 'description': 'Vanilla, chocolate, and strawberry flavors.', 'price': '₹80'},
            {'name': 'Rasgulla', 'description': 'Spongy cheese balls soaked in light sugar syrup, a classic Odia sweet treat.', 'price': '₹120'}
        ]
    }
    return render_template('menu.html', title='Dining Menu', menu=menu_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

if __name__ == '__main__':
    app.run(debug=True)