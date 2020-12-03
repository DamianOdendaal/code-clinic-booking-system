def confirm_bookings(id):
    """Validation function that prevents the volunteer from booking their own
    slot."""

    user_email = user.get_user_details().get('email')
    volunteer_email = get_attribute(id, 'email')
    patient_email = get_attribute(id, 'patient')
    status = get_attribute(id, 'status')

    if user_email == volunteer_email:
        print("A volunteer cannot book an their OWN slot!")
    elif status == '[BOOKED]':
        print(f"Sorry, the event is already booked by {patient_email}.")
        print(f"Please check an open slot. {colored('[AVAILABLE]', 'green')}")
    else:
        create_bookings(id)


def booking_summary(id):
    """This will print out the booking details in a summarised format."""

    volunteer_email = get_attribute(id, 'email')
    help_topic = get_attribute(id, 'summary')
    time = get_attribute(id, 'time')
    date = get_attribute(id, 'date')

    print("Booking Summary:")
    print(f"You're getting help with: {help_topic}")
    print(f"The volunteer: {volunteer_email}")
    print(f"Time: {time}")
    print(f"Date: {date}")

ef get_attribute(id, prompt):
    """
    This function access the volunteer and patient items
    """
    calendar = cal.show_code_clinics_calendar()

    slot = None
    for item in calendar:
        if item[6] == id:
            slot = item
    if slot != None:
        if prompt == "email":
            return slot[4]
        elif prompt == "date":
            return slot[0]
        elif prompt == "time":
            return slot[1]
        elif prompt == "summary":
            return slot[2]
        elif prompt == "patient":
            #use regex later stage things
            return slot[3]
        elif prompt == "volunteer":
            return slot[4]
        elif prompt == "status":
            string = slot[5]
            return string[5:13] 
    
    return slot


    def cancel_a_slot(id):
    """This function blocks the user from deleting an event if it's already
    booked, or if the patient tries to delte the slot."""

    user_email = user.get_user_details().get('email')
    volunteer_email = attribute.get_attribute(id, 'email')
    patient_email = attribute.get_attribute(id, 'patient')
    status = attribute.get_attribute(id, 'status')

    if status == '[BOOKED]' and volunteer_email == user_email:
        print(f"Sorry, you cannot cancel a {colored('[BOOKED]', 'red')} a booked slot.")
    elif user_email == patient_email:
        print(f"Please run 'wtc-cal cancel_booking <argv (id)>' to cancel your own booking.")
    else:
        cancel_open_slot(id)