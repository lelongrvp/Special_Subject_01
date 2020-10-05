MONTHS = ['January', 'February', 'March', 
        'April', 'May', 'June', 
        'July', 'August', 'September', 
        'October', 'November', 'December']

user_date = input('Enter the date as form mm/dd/yyyy: ')
month_str, day_str, year_str = user_date.split('/')
month = int(month_str)

print ('\nThe date is', MONTHS[month - 1], day_str + ',', year_str + ',')