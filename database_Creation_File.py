from new import db, create_app
import os
app = create_app()

with app.app_context():
    if not os.path.exists("/tmp/database.db"):
        db.create_all()
    # user_1 = User(username = 'Yashas', email = 'X@demo.com', password = 'password')
    # db.session.add(user_1)
    # db.session.commit()   #Makes changes in the database properly
    
    # user = User.query.first()
    # print(user)
    # post_1 = Post(title = 'Blog 1', content = 'First Post Content', user_id = user.id)
    # db.session.add(post_1)
    # db.session.commit()
    
    # who = post_1.author #This only works because of that backref thingy done
    
    # db.drop_all()
########A FEW COMMON QUERIES########
# User.query.all() #Gives all the users in the database
# User.query.first() #Gives the first user
# User.query.filter_by(username = 'Yashas').all() #Applies this filter and then returns shit

# User.query.get() #So here you gotta pass the ID of the user to get the data 