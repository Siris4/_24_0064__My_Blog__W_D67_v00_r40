import os
from main import app, db, User

with app.app_context():
    user = User.query.get(1)  # Use the correct user_id here in ()
    if user:
        user.is_admin = True
        db.session.commit()
        print("User has been set as admin.")
    else:
        print("User not found.")
