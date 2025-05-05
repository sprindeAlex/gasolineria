from app.models.user import User
from app.config.database import db_session

class UserService:
    @staticmethod
    def create_user(user_data):
        new_user = User(**user_data)
        db_session.add(new_user)
        db_session.commit()
        return new_user

    @staticmethod
    def get_user(user_id):
        return db_session.query(User).filter(User.id == user_id).first()

    @staticmethod
    def update_user(user_id, user_data):
        user = db_session.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            db_session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = db_session.query(User).filter(User.id == user_id).first()
        if user:
            db_session.delete(user)
            db_session.commit()
            return True
        return False

    @staticmethod
    def get_all_users():
        return db_session.query(User).all()