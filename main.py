from datetime import datetime
import application.db.people
from application.salary import calculate_salary

if __name__ == '__main__':
    application.db.people.get_employees()
    calculate_salary()
    now_date = datetime.now()
    print(f"Текущая дата : {now_date.day}.{now_date.month}.{now_date.year}")
