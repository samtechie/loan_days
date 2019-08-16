
def get_days_of_power(R1,D1,R2,D2,R3,D3,K):

    days_of_power = 0

    #Use dictionary to track the days
    days = {
        'D1' : D1,
        'D2' : D2,
        'D3' : D3,

    }

    #sort the start day of the loans from the earliest to the latest
    #sort days will be a list of tuples with the key and value arranged in ascending order
    sort_days = sorted(days.items(), key = lambda days: days[1])
    #check if there are any other loans starting on the same day
    #we find dictionary keys with duplicate values
    rev_days = {}

    for key, value in days.items():
        rev_days.setdefault(value, set()).add(key)

    result = filter(lambda x: len(x)>1, rev_days.values())

    #we get a set with the keys of duplicate days i.e loans starting on the same day.
    #it will return a set of the keys
    equal_days = list(result)

    day_rates = {
        'D1' : R1,
        'D2' : R2,
        'D3' : R3,
    }
    earliest_day_set = {sort_days[0][0]}
    earliest_day = sort_days[0][0]
    second_day = sort_days[1][0]
    third_day = sort_days[2][0]
    earliest_day_val = sort_days[0][1]
    second_day_val = sort_days[1][1]
    third_day_val = sort_days[2][1]

    #we will use this list to track the loans

    loan_days_rates = []

    #if there are no duplicate days i.e loans starting on the same days
    if not equal_days:
        # we iterate through the days calculating the respective loan rates
        # for the days
        for i in range(earliest_day_val, second_day_val):
            loan_days_rates.append(day_rates[earliest_day])

        for i in range(second_day_val,third_day_val):
            loan_days_rates.append(day_rates[earliest_day]+ day_rates[second_day])

        loan_days_rates.append(day_rates[earliest_day]+ day_rates[second_day]+ day_rates[third_day])

        for i in loan_days_rates:
            if K >= i and i != loan_days_rates[-1]:
                K-=i
                days_of_power += 1

        #We must keep truck of the last element in the out loan_rate list in case we still have some balance available
        if(loan_days_rates[days_of_power]== loan_days_rates[-1]):
            extra_days = K //loan_days_rates[-1]
            days_of_power+=extra_days

        print ("total days of power are {}".format(days_of_power))

    else:
        #Deals with loans starting on the same day
        if earliest_day_set.issubset(equal_days[0]):
            duplicate_start_dates_set = equal_days[0].difference(earliest_day_set)
            if len(duplicate_start_dates_set) == 1:
                duplicate_start_date = duplicate_start_dates_set.pop()

                for i in range(earliest_day_val,third_day_val):
                    loan_days_rates.append(day_rates[earliest_day]+ day_rates[duplicate_start_date])

                loan_days_rates.append(day_rates[earliest_day]+ day_rates[duplicate_start_date]+ day_rates[third_day])
                for i in loan_days_rates:
                    if K >= i and i != loan_days_rates[-1]:
                        K-=i
                        days_of_power += 1


                if(loan_days_rates[days_of_power]== loan_days_rates[-1]):
                    extra_days = K //loan_days_rates[-1]
                    days_of_power+=extra_days

                print ("total days of power are {}".format(days_of_power))


            elif len(duplicate_start_dates_set) == 2:
                duplicate_start_date_list = list(duplicate_start_dates_set)

                duplicate_loan_days_rates = day_rates[earliest_day] + day_rates[duplicate_start_date_list[0]] + day_rates[duplicate_start_date_list[1]]
                days_of_power = K //duplicate_loan_days_rates
                print ("total days of power are {}".format(days_of_power))


        else:
            for i in range(earliest_day_val,third_day_val):
                loan_days_rates.append(day_rates[earliest_day])

            loan_days_rates.append(day_rates[earliest_day]+ day_rates[second_day]+ day_rates[third_day])

            for i in loan_days_rates:
                if K >= i and i != loan_days_rates[-1]:
                    K-=i
                    days_of_power += 1


            if(loan_days_rates[days_of_power]== loan_days_rates[-1]):
                extra_days = K //loan_days_rates[-1]
                days_of_power+=extra_days

            print ("total days of power are {}".format(days_of_power))





get_days_of_power(R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=21000)

get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000)
get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000)
get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000)
get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)


