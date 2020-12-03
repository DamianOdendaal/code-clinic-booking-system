from cal_setup import get_calendar_service

def main():

    service = get_calendar_service()
    try:
        service.events().delete(
            calendarId='primary',
            eventId='kv5eh1bpg10e571bmshlp1512k'
        ).execute()
    except googleapiclient.errors.HttpError:
        print("Failed to delete event")

    print("Event deleted")

if __name__ == "__main__":
    main()