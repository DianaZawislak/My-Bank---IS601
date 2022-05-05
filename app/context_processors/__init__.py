from locale import currency
from os import getenv
import datetime
from flask_login import current_user
import sqlalchemy
from sqlalchemy import String, Float
from sqlalchemy.sql.functions import current_user, user
from app.db.models import User
from app import transactions
from app.auth.forms import login_form


def utility_text_processors():
    message = "hello world"
    form = login_form()

    def account_balance():

        try:
            engine = sqlalchemy.create_engine("sqlite:////home/myuser/database/db2.sqlite")
            data = sqlalchemy.MetaData(bind=engine)
            sqlalchemy.MetaData.reflect(data)
            total = data.tables['transactions']
            query = sqlalchemy.select(sqlalchemy.func.sum(total.c.amount))
            result = engine.execute(query).fetchall()
            currency = str(result[0])
            balance = currency[1:-2]
            return "${:,.2f}".format(float(balance))
        except:
                return ("$0.00")

    #def user_balance():
      #  userid = current_user.id
       # user_trans = transactions.query.filter_by(user_id=userid).all()
        #total = 0
        #for trans in user_trans:
         #   total += trans.amount
        #return "${:,.2f}".format(float(total))#

    def deployment_environment():
        return getenv('FLASK_ENV', None)

    def current_year():
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        return year

    def format_price(amount, currency="$"):
        return f"{currency}{amount:.2f}"

    return dict(
        form=form,
        mymessage=message,
        deployment_environment=deployment_environment(),
        year=current_year(),
        format_price=format_price,
        account_balance=account_balance,
        #user_balance=user_balance()
    )
