import math

shutdown = 0


def ichi(first, second):
    try:
        error = first[3]
        ichi_result = first[:4] + second + first[4:]
        # firstly we check if fourth symbol in first entry exists, then create number with everything before fourth,
        # add second entry and then add everything other from first.
        return "/\n%s" % ichi_result
    except:
        return "/\nError, first str is less than 4"


def ni(start, end, step):
    notclose = True
    # I decided to not use 'return' statement for easier output of right answer if everything is ok
    # I did it with just 'print' and without another one list where I should've created indentation after every answer
    try:
        # first 'try' for errors in input
        start = float(start)
        end = float(end)
        step = float(step)
        x = start
        solutions = []
        try:
            # second 'try' for errors in formula
            errorhappened = 0
            check = 1/x
            check = x ** 3 + 3 * math.log2(-(x + 2) / 6) - 2 ** x - math.sqrt((x ** 2) - 3 * x + 17)
            check = math.sqrt(step)
            # I found that with math.isclose function I can properly count with float type start or step
            # because without it float type comparisons were not too much correct
            while notclose == True:
                if math.isclose(x, end) == True:
                    notclose = False
                count = x ** 3 + 3 * math.log2(-(x + 2) / 6) - 2 ** x - math.sqrt((x ** 2) - 3 * x + 17)
                x = x + step
                solutions.append(count)

        except:
            # if something goes wrong to do not show half of results and then print error, we will check
            # if there is error and only if there is no errors at all, we will show result
            errorhappened = 1
        if errorhappened == 0:
            print('/')
            for i in range(len(solutions)):
                print(solutions[i])
        else:
            print("/\ncan't be counted, solution out of feasible region or doesn't exist")
    except:
        print("/\nall input should be numbers, float or int, try again")


def san(strone, strtwo):
    counter = 0
    for i in range(len(strtwo)):
        if strtwo[i:len(strone) + i] == strone:
            counter += 1
    return "/\n%s times" % counter


def yon(row_amount, row_given):
    row_mean = 0
    row_result = 0
    try:
        row_amount = int(row_amount)
        row_split = row_given.split('a')
        if len(row_split) == row_amount:
            for i in row_split:
                row_mean += int(i)
            row_mean = row_mean / row_amount
            for i in row_split:
                if int(i) < row_mean:
                    row_result += int(i)
            return "/\nsum is %s" % row_result
        else:
            return '/\nerror, something is wrong with input'
    except:
        return '/\nerror, something is wrong with input'


def go(a):
    b = a.split('.')
    week = ('Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    # month dictionary in "'given number':(number for formula, amount of days in month)" format
    # we have 29 days in february just for easier check system
    month_info = {'01': (1, 31), '02': (4, 29), '03': (4, 31), '04': (0, 30), '05': (2, 31), '06': (5, 30),
                  '07': (0, 31), '08': (3, 31), '09': (6, 30), '10': (1, 31), '11': (4, 30), '12': (6, 31)}
    # input will be in str format and I will use function int() a lot, so we will use try right away
    try:
        # check if amount of days is ok. And it the same moment we can't check it without correct month input so we check both
        # also check if century is 17 because it is only century we work with
        if int(b[0]) >= 1 and int(b[0]) <= month_info[b[1]][1] and (int(b[2][:2]) == 16 or b[2] == '1700'):
            # and special check for leap year which has 29 days in february
            # and we also check 1600 year which is for some reason is 16th century
            if int(b[1]) == 2 and int(b[0]) == 29 and int(b[2]) % 4 != 0 or b[2] == '1600':
                return ('/\nsomething is wrong with given date')
            else:
                try:
                    # and last check for having extra numbers after third point. (e.g. 29.02.1604.1337.228)
                    ch1 = a[11]
                    return ('/\nwrong given date')
                except:
                    # year indexes will be different for different amounts of hundreds years
                    if b[2][:2] == '16':
                        year_index = (6 + int(b[2][2::]) + int(b[2][2::]) // 4) % 7
                    elif b[2][:2] == '17':
                        year_index = (4 + int(b[2][2::]) + int(b[2][2::]) // 4) % 7
                    math_result = (int(b[0]) + month_info[b[1]][0] + year_index) % 7
                    if int(b[1]) <= 2 and int(b[0]) <= 29 and int(b[2]) % 4 == 0:
                        math_result -= 1
                    day_of_the_week = week[math_result]
                    return "at %s there was a %s" % (a, day_of_the_week)
        else:
            return '/\nsomething is wrong with given date'
    except:
        return '/\nwrong given date format'


while shutdown == 0:
    general_info = 'Entering following numbers will give let you use use these programs:\n' \
                   '"1" —  put one string into another\n' \
                   '"2" —  calculate given mathematical function in inputted D(f)\n' \
                   '"3" —  find how much one string enters another\n' \
                   '"4" —  function that will find sum of numbers that are smaller that arithmetic mean\n' \
                   '"5" —  day of a week of 17 cuntury date you will write\n' \
                   'Or you can write "-1" to shut the program down'
    print(general_info)
    general_input = input('>')
    while True:
        if general_input == "1":
            print('/\nProgram 1 is now working. . . \n/\n'
                  'Write two strings and programm will merge them into one by inserting second string to the first from 4th letter')
            print(ichi(input('first - '), input('second - ')))
        elif general_input == "2":
            print('/\nProgram 2 is now working. . . \n/\n'
                  'You can write where to start, where to stop and step for function '
                  'f(x)=x^3 + 3 * log2(-(x + 2) / 6) - 2^x - sqrt(x^2 - 3x + 17)')
            ni(input('start - '), input('end - '), input('step - '))
        elif general_input == "3":
            print('/\nProgram 3 is now working. . . \n/\n'
                  'write two strings and program will show hum much first string inters into second')
            print(san(input('first string - '), input('second string - ')))
        elif general_input == "4":
            print('/\nProgram 4 is now working. . . \n/\n'
                  'write number n and then n amount of numbers divided not by spacebar but by symbol "a".\n'
                  'program will give you sum of numbers that are less than mean of all numbers')
            print(yon(input('amount of numbers - '), input('row of numbers - ')))
        elif general_input == "5":
            print('/\nProgram 5 is now working. . . \n/\n'
                  'write 17th century date and it will show what day of week it was that day')
            print(go(input('date in dd.mm.yyyy format - ')))
        elif general_input == "-1":
            print("We will be happy to see you again\n"
                  "shutting down. . . ")
            shutdown = 1
            break
        else:
            print('/\nsometing went wrong throwing back to main menu. . .\n/')
            break
            # and below here is part of function for repeating sub-program without having to go through main menu again and again:
        again = input("/\nDo you want to continue working with sub-program or come back to list of all?\n"
                      "Write '1' if you want to try again and '0' if you want to come back to main menu? ")
        if again == '1':
            continue
        elif again == '0':
            print('/')
            break
        else:
            print('/\nwrong input, throwing back to main menu\n/')
            break
