from locale import currency
from os import getenv
import datetime

import sqlalchemy
from sqlalchemy import String, Float
from sqlalchemy.sql.functions import current_user, user

from app.auth.forms import login_form


def utility_text_processors():
    message = "hello world"
    form = login_form()

    def account_balance():
        engine = sqlalchemy.create_engine("sqlite:////home/myuser/database/db2.sqlite")
        data = sqlalchemy.MetaData(bind=engine)
        sqlalchemy.MetaData.reflect(data)

        total = data.tables['transactions']
        query = sqlalchemy.select([sqlalchemy.func.round(sqlalchemy.func.sum(total.c.amount), 2)])
        result = engine.execute(query).fetchall()
        currency = "$"
        # sum = []
        # for record in result:
        # print("\n", record[0], record[1])
       # {{account_balance(result)}}
        return currency, result


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

    )
