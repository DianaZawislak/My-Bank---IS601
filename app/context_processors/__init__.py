from os import getenv
import datetime

import sqlalchemy

from app.auth.forms import login_form


def utility_text_processors():
    message = "hello world"
    form = login_form()


    def account_balance():
        # THIS WILL PRINT THE BALANCE FOR ALL BANK'S TRANSACTIONS
        engine = sqlalchemy.create_engine("sqlite:////home/myuser/database/db2.sqlite")
        data = sqlalchemy.MetaData(bind=engine)
        sqlalchemy.MetaData.reflect(data)
        total = data.tables['transactions']
        query = sqlalchemy.select(sqlalchemy.func.sum(total.c.amount))
        result = engine.execute(query).fetchall()
        return result


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
        account_balance = account_balance
    )
