def get_last_three ( items ) :
    start = len( items ) - 3
    end = len ( items )
    return items [ start : end ]

print ( get_last_three ([10 , 20 , 30 , 40 , 50]) )