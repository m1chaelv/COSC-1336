from datetime import datetime, timedelta

def current_year_week_with_sunday_as_reference():
    # Get the current date
    current_date = datetime.now()

    # Calculate the end of this week (Sunday)
    end_of_week = current_date + timedelta(days=(6 - current_date.weekday()))

    # Format the year and week number based on the end of the week
    year_week = end_of_week.strftime("%Y-%U")

    return year_week

def main():
    current_week_based_on_sunday = current_year_week_with_sunday_as_reference()
    print(current_week_based_on_sunday)

# main()

list1 = [{'a': 1}, {'b': 2}]
list2 = [{'c': 3}, {'d': 4}]
print(list1)
print(list2)

list1.update(list2)
print(list1)
print(list2)

