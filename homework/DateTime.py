def launch_message(launch_datetime):
 return "We're launching in " + launch_datetime - datetime.datetime.now()) +  " days" 
 
 return "We're launching in " + str((launch_datetime - datetime.datetime.now()) .days) + " days!"
 
 launch_message(launch_date)
 launch_message(add_months(datetime.datetime.now() ,5))

