def get_days_power(R1,D1,R2,D2,R3,D3,K):
    print("Hello {R1} {D1} {R2} {D2} {R3} {D3} {K}".format(R1=R1,D1=D1,R2=R2,D2=D2,R3=R3,D3=D3,K=K))

    #Use dictionary to track the days
    days = { 
        'D1' : D1,
        'D2' : D2,
        'D3' : D3,

    }
    print( "highest loan start date {max}".format(max=max(days, key=days.get)
))

    print( "lowest loan start date {min}".format(min=min(days, key=days.get)
))


get_days_power(R1=1000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=21000)
