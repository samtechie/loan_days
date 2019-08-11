
def get_days_power(R1,D1,R2,D2,R3,D3,K):
    print("Hello {R1} {D1} {R2} {D2} {R3} {D3} {K}".format(R1=R1,D1=D1,R2=R2,D2=D2,R3=R3,D3=D3,K=K))

    days_of_power = 0

    #Use dictionary to track the days
    days = {
        'D1' : D1,
        'D2' : D2,
        'D3' : D3,

    }
    print( "highest loan start date {max}".format(max=max(days, key=days.get)
))


    #sort the start day of the loans from the earliest to the latest
    sortDays = sorted(days.items(), key = lambda days: days[1])
    print(sortDays)
    #get the earliest loan start date
    #print(sortDays[0][0])
    #check if there are any other loans starting on the same day

    rev_days = {}

    for key, value in days.items():
        rev_days.setdefault(value, set()).add(key)

    result = filter(lambda x: len(x)>1, rev_days.values())

    equal_days = list(result)

    day_rates = {
        'D1' : R1,
        'D2' : R2,
        'D3' : R3,
    }
    earliest_day_set = {sortDays[0][0]}
    earliest_day = sortDays[0][0]
    third_day = sortDays[2][0]

    if not equal_days:
      if earliest_day == 0:
          account_daily_rate = day_rates[earliest_day]
          if K == account_daily_rate:
              days_of_power+=1
          elif K > account_daily_rate:
              balance = K - account_daily_rate
              days_of_power+=1
              for days in range(1,):
              #consider using generators and a for loop




    else:
        #Deals with loans starting on the same day
        if earliest_day_set.issubset(equal_days[0]):
            duplicate_start_dates_set = equal_days[0].difference(earliest_day_set)
            if len(duplicate_start_dates_set) == 1:
                duplicate_start_date = duplicate_start_dates_set.pop()
                account_daily_rate = day_rates[earliest_day] + day_rates[duplicate_start_date]
            elif len(duplicate_start_dates_set) == 2:
                duplicate_start_date_list = list(duplicate_start_dates_set)
                account_daily_rate = day_rates[earliest_day] + day_rates[duplicate_start_date_list[0]] + day_rates[duplicate_start_date_list[1]]
        else:
            account_daily_rate = day_rates[sortDays[0][0]]




    print(equal_days)
    #print(equal_days[0][1])
    #print(type(sortDays[0][0]))


    #print(day_rates[sortDays[0][0]])
    print(account_daily_rate)




get_days_power(R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=21000)
