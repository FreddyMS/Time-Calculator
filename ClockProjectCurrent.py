def add_time(start, duration, starting_day=''):
    # Days of the week for reference
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_of_week[0]
    starting_day = starting_day.lower()

    # Remainder division
    hours = 12
    hours_per_day = 24
    minutes = 60
    days = 7
    # account for chg in PM and AM
    bef_mid_day = ''
    aft_mid_day = ''

    if 'AM' in start:
        bef_mid_day = 'AM'

    if 'PM' in start:
        aft_mid_day = 'PM'
    #  Base Case:
    if duration == '0:00' and starting_day == '':
        return start
        #  Base Case:
    if duration == '24:00' and starting_day == '':
        start = start + ' ' + '(next day)'

        return start

    start = start.strip('PM')
    start = start.strip('AM')
    start = start.replace(':', '')
    start = start.replace(' ', '')
    duration = duration.replace(':', '')
    duration = duration.replace(' ', '')

    # hour slicing
    if len(start) <= 3:
        hour1 = start[:1]
    if len(start) >= 4:
        hour1 = start[:2]
    if len(duration) <= 3:
        hour2 = duration[:1]
    if len(duration) >= 4:
        hour2 = duration[:2]
    if len(duration) >= 5:
        hour2 = duration[:3]

    total_hours = int(hour1) + int(hour2)

    # minutes slicing
    if len(start) <= 3:
        minute1 = start[1:3]
    if len(start) > 3:
        minute1 = start[2:4]
    if len(duration) <= 3:
        minute2 = duration[1:3]
    if len(duration) > 3:
        minute2 = duration[2:4]
    if len(duration) > 4:
        minute2 = duration[3:5]
    plus_one = 0
    total_minutes = int(minute1) + int(minute2)
    if total_minutes >= 60:
        total_minutes = total_minutes % 60
        total_hours += 1
        plus_one += 1

    total_hours = str(total_hours)
    total_minutes = str(total_minutes)

    for index, letter in enumerate(starting_day):
        if index == 0:
            starting_day = starting_day[0].upper() + starting_day[1:]

    ###############################################################################
    # Less than 12 hours when len of minute is ONE
    if int(total_hours) < 12:
        if len(total_minutes) == 1:
            if bef_mid_day:
                if starting_day in days_of_week:
                    concantenate = str(
                        int(total_hours) % hours) + ':' + '0' + total_minutes + ' ' + 'AM' + ',' + ' ' + starting_day
                    return concantenate
                else:
                    concantenate = str(total_hours) + ':' + '0' + total_minutes + ' ' + 'AM'
                    return concantenate
            if aft_mid_day:
                if starting_day in days_of_week:
                    concantenate = str(
                        int(total_hours) % hours) + ':' + '0' + total_minutes + ' ' + 'PM' + ',' + ' ' + starting_day
                    return concantenate
                else:
                    concantenate = str(total_hours) + ':' + '0' + total_minutes + ' ' + 'PM'
                    return concantenate
    # NO Issue so Far
    ###############################################################################
    # exactly 12 hours, For PM -> AM or  AM ->PM

    if int(total_hours) == 12:
        if len(total_minutes) == 1:
            if bef_mid_day:
                concantenate = str(int(total_hours)) + ':' + '0' + total_minutes + ' ' + 'PM'
                return concantenate
            if aft_mid_day:
                concantenate = str(int(total_hours) % hours) + ':' + '0' + total_minutes + ' ' + 'AM'
                return concantenate

            # NO Issue so Far
    ###############################################################################
    # Greater than12 hours
    if int(total_hours) > 12:
        if len(total_minutes) == 1:
            if bef_mid_day:
                concantenate = str(int(total_hours) % hours) + ':' + '0' + total_minutes + ' ' + 'PM'
                return concantenate
            if aft_mid_day:
                military_time = 12 + int(hour1)

                addition = military_time + int(hour2) + 1

                quotient = addition // 24

                if quotient == 1:
                    concantenate = str(
                        int(total_hours) % hours) + ':' + '0' + total_minutes + ' ' + 'AM' + ' ' + '(next day)'
                    return concantenate
                # NO Issue so Far
                ###############################################################################
                # error in COrrec hour then must settle PM and AM
                if quotient > 1:

                    for index, letter in enumerate(starting_day):
                        if index == 0:
                            starting_day = starting_day[0].upper() + starting_day[1:]
                    for index, days in enumerate(days_of_week):
                        if starting_day == days:
                            value = index + 1

                    day = quotient  # +  value
                    reminder_day = day % 7
                    final_day = days_of_week[reminder_day - 1]
                    hour2 = int(hour2) % 12
                    addition = int(hour1) + int(hour2) + plus_one

                    if starting_day == '':
                        if addition <= 12:
                            concantenate = str(
                                int(addition)) + ':' + '0' + total_minutes + ' ' + 'AM' + ' ' + '(' + str(
                                quotient) + ' ' + 'days later)'
                        else:
                            concantenate = str(
                                int(addition) % hours) + ':' + '0' + total_minutes + ' ' + 'AM' + ' ' + '(' + str(
                                quotient) + ' ' + 'days later)'

                    if starting_day in days_of_week:
                        if addition <= 12:
                            concantenate = str(
                                int(addition)) + ':' + '0' + total_minutes + ' ' + 'AM' + ',' + ' ' + final_day + ' ' + '(' + str(
                                quotient) + ' ' + 'days later)'
                        else:
                            concantenate = str(
                                int(addition) % 12) + ':' + '0' + total_minutes + ' ' + 'AM' + ',' + ' ' + final_day + ' ' + '(' + str(
                                quotient) + ' ' + 'days later)'
                    return concantenate

                ###############################################################################
    # Less than 12 hours when len of minute is greater than ONE
    if int(total_hours) < 12:
        if len(total_minutes) > 1:
            if bef_mid_day:
                if starting_day in days_of_week:
                    concantenate = str(
                        int(total_hours) % hours) + ':' + total_minutes + ' ' + 'AM' + ',' + ' ' + starting_day
                    return concantenate
                else:
                    concantenate = str(total_hours) + ':' + total_minutes + ' ' + 'AM'
                    return concantenate

            if aft_mid_day:
                if starting_day in days_of_week:
                    concantenate = str(
                        int(total_hours) % hours) + ':' + total_minutes + ' ' + 'PM' + ',' + ' ' + starting_day
                    return concantenate
                else:
                    concantenate = str(total_hours) + ':' + total_minutes + ' ' + 'PM'
                    return concantenate

    if int(total_hours) == 12:
        if len(total_minutes) > 1:
            if bef_mid_day:
                concantenate = str(int(total_hours)) + ':' + total_minutes + ' ' + 'PM'

            if aft_mid_day:
                concantenate = str(int(total_hours) % hours) + ':' + total_minutes + ' ' + 'AM'
            return concantenate
    # NO Issues
    ###############################################################################
    # same day
    if int(total_hours) > 12:
        if len(total_minutes) > 1:

            if bef_mid_day:

                military_time = 12 + int(hour1)
                addition = military_time + int(hour2)
                quotient = addition // 24

                if quotient == 1:
                    concantenate = str(int(total_hours) % hours) + ':' + total_minutes + ' ' + 'AM' + ' ' + '(next day)'
                    return concantenate
                if quotient > 1:
                    for index, letter in enumerate(starting_day):
                        if index == 0:
                            starting_day = starting_day[0].upper() + starting_day[1:]
                    # value=None
                    for index, days in enumerate(days_of_week):
                        if starting_day == days:
                            index = index + 1
                            break
                    
                    day = quotient + index
                    reminder_day = day % 7
                    final_day = days_of_week[reminder_day - 1]
                    if starting_day == '':
                        concantenate = str(
                            int(total_hours) % hours) + ':' + total_minutes + ' ' + 'AM' + ' ' + '(' + str(
                            quotient) + ' ' + 'days later)'
                        return concantenate
                    if starting_day in days_of_week:
                        concantenate = str(
                            int(total_hours) % hours) + ':' + total_minutes + ' ' + 'AM' + ',' + ' ' + final_day + ' ' + '(' + str(
                            quotient) + ' ' + 'days later)'
                        return concantenate
                    else:
                        concantenate = str(int(total_hours) % hours) + ':' + total_minutes + ' ' + 'PM'
                        return concantenate
                        ############################################################
            # One day max /next day right after midnight

            if aft_mid_day:
                military_time = 12 + int(hour1)
                addition = military_time + int(hour2)
                quotient = addition // 24
                print(quotient)

                if quotient == 1:
                    concantenate = str(int(total_hours) % hours) + ':' + total_minutes + ' ' + 'AM' + ' ' + '(next day)'
                    return concantenate
                if quotient > 1:
                    for index, letter in enumerate(starting_day):
                        if index == 0:
                            starting_day = starting_day[0].upper() + starting_day[1:]
                    for index, days in enumerate(days_of_week):
                        if starting_day == days:
                            index = index + 1
                            print(index)
                            break
                    day = quotient + index
                    print(day)
                    reminder_day = day % 7
                    final_day = days_of_week[reminder_day - 1]
                    if starting_day == '':
                        concantenate = str(
                            int(total_hours) % hours) + ':' + total_minutes + ' ' + 'AM' + ' ' + '(' + str(
                            quotient) + ' ' + 'days later)'
                    # 10
                    if starting_day in days_of_week:
                        concantenate = str(
                            int(total_hours) % hours) + ':' + total_minutes + ' ' + 'AM' + ',' + ' ' + final_day + ' ' + '(' + str(
                            quotient) + ' ' + 'days later)'
                    return concantenate


# NO Issues
###############################################################################


# Examples
# print(add_time('2:59 AM', '0:00'))  # Returns 2:59 AM #Done
# print(add_time('3:30 PM', '2:12'))  # Returns: 5:42 PM #Done
# print(add_time('3:00 PM', '3:01'))  # Returns: 6:01 PM #Done
# print(add_time('11:43 PM', '7:00'))  # Returns: 6:43 AM#Done
# print(add_time('11:43 AM', '7:00'))  # Returns: 6:43 PM #FIx PM
# print(add_time('11:43 AM', '0:17'))  # Returns: 12:00 PM #Done
# print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM#error when PM
# print(add_time('10:10 PM', '3:30','Monday')) # Returns: 1:40 AM (next day)#when AM, does not chg to pM
# print(add_time('6:30 PM', '205:12','Monday'))  # Returns: 7:42 AM Wednesday (9 days later)#Done
# print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns:2:02 PM Monday #MIssing Monday(DAY)
# print(add_time('8:16 PM', '466:02', 'tuesday'))  # Returns: 6:18 AM, Monday (20 days later)#Done
# print(add_time('3:30 PM', '2:12', 'Monday')) #'5:42 PM, Monday #less than 12 hours #Done
# print(add_time('2:59 AM', '24:00')) # Return '2:59 AM (next day) #Done so far#Done
# print(add_time('11:59 PM', '24:05','Monday'))   # MUSt Review for error!!!!return '12:04 AM Tuesday (2 days later)'
# print(add_time('2:59 AM', '24:00', 'saturDay')) #should return '2:59 AM, Sunday (next day)'.#Issue but solved/will Review
# # print(add_time('11:59 PM', '24:05', 'Wednesday'))#should return '12:04 AM, Friday (2 days later)'
# print(add_time('8:16 PM', '466:02')) # Return '6:18 AM (20 days later)' #Issue with 3rd input#AM
# print(add_time('8:16 PM', '466:02', 'tuesday')) #return '6:18 AM, Monday (20 days later)'
# print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)#AM
print(add_time('11:59 PM', '24:05', 'Wednesday'))  # return '12:04 AM, Friday (2 days later)'

# This segment of code solves print(add_time('2:59 AM', '24:00', 'saturDay')) #should return '2:59 AM, Sunday (next day)' However, it creates problems for the rest of the code below it
#     military_time= 12 + int(hour1)
#     addition=military_time + int(hour2)
#     quotient= addition//24

#     if int(total_hours) > 12:
#         if len(total_minutes) > 1:
#             if bef_mid_day: #############
#             # Capitalize the first letter of the starting day
#                 starting_day = starting_day[0].upper() + starting_day[1:]
#             # Initialize value with a default (e.g., 0 or None)
#
#             # Find the day index
#                 for index, days in enumerate(days_of_week):

#                   if starting_day == days:
#                     index = index + 1
#                     print(value)
#                     break  # Exit the loop once the day is found

#             # Ensure value has been assigned before using it
#                 if value is not None:
#                     day = quotient + value
#                 else:
#                     print("Error: starting_day not found in days_of_week")

#
#                 reminder_day= day%7
#                 final_day=days_of_week[reminder_day-1]

#                 if quotient==1:
#                 #First if: Day + Next day
#                   if starting_day in days_of_week:
#                     if  starting_day in days_of_week:
#                         concantenate=str(int(total_hours) % hours)  + ':'  + total_minutes + ' '  + 'AM'+','  + ' ' + final_day+ ' ' + '(next day)'
#                         return concantenate

#                     else:
#                         concantenate=str(int(total_hours) % hours) + ':'  + total_minutes + ' '  + 'AM' + ' ' + '(next day)'
#                         return concantenate