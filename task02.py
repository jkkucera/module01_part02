salary = float(input('Enter monthly salary: '))
loan = float(input('Enter monthly loan payments: '))
utility = float(input('Enter monthly utility payments: '))

available_funds = salary-loan-utility

print('Monthly available funds: ', available_funds)