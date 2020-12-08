
commands_bold = []

for cmd in valid_sys_commands:
    commands_bold.append('\033[1m'+cmd+'\033[0m')


def command_instructions():
    """Print out statements that shows how the booking system works."""

    if len(sys.argv) >= 2 and sys.argv[1] != 'help':
        command = ""
        for arg in sys.argv[1:]:
            command += f"{arg}"

        print(f"Unrecognized command: \"wtc-cal {command.strip()}\"")
    
    elif len(sys.argv) == 1:
        print("Please provide some options\n")
        print("\tusage: wtc-cal <command> [<args>]")


    print('\nThese are wtc-cal commands that can be used in this Code Clinic:\n')
    
    print('setup and login')
    print('\t'+commands_bold[0]+'\t\tInstall required packages')
    print('\t'+commands_bold[1]+'\t\tUsed to login')
    print('\t'+commands_bold[2]+'\t\tUsed to logout')
    print('\t'+commands_bold[3]+'\t\tUsed to config\n')

    print('booking and slots')
    print('\t'+commands_bold[4]+'\tCreate a slot to be booked by a patient [RUN-TIME]')
    print('\t'+commands_bold[5]+'\t\tView slots that were created by volunteers [OPEN], [BOOKED]')
    print('\t'+commands_bold[6]+'\t\tUsed to book an empty slot as a patient')
    print('\t'+commands_bold[7]+'\tUsed to cancel a booking [PATIENTS]')
    print('\t'+commands_bold[8]+'\t\tUsed to cancel an empty slot [VOLUNTEERS]\n')

    print('calendars and viewing')
    print('\t'+commands_bold[9]+'\tView your personal calendar on the terminal')



    "conferenceData ": {
  "entryPoints": [
   {
    "entryPointType": "video",
    "uri": "https://meet.google.com/wix-pvpt-njj",
    "label": "meet.google.com/wix-pvpt-njj"
   },
   {
    "entryPointType": "more",
    "uri": "https://tel.meet/wix-pvpt-njj?pin=1701789652855",
    "pin": "1701789652855"
   },
   {
    "entryPointType": "phone",
    "uri": "tel:+44-20-3873-7654",
    "label": "+44 20 3873 7654",
    "pin": "6054226"
   }
  ],
  "conferenceSolution": {
   "key": {
    "type": "hangoutsMeet"
   },
   "name": "Hangouts Meet",
   "iconUri": "https://lh5.googleusercontent.com/proxy/bWvYBOb7O03a7HK5iKNEAPoUNPEXH1CHZjuOkiqxHx8OtyVn9sZ6Ktl8hfqBNQUUbCDg6T2unnsHx7RSkCyhrKgHcdoosAW8POQJm_ZEvZU9ZfAE7mZIBGr_tDlF8Z_rSzXcjTffVXg3M46v"
  },
  "conferenceId": "wix-pvpt-njj",
  "signature": "ADwwud9tLfjGQPpT7bdP8f3bq3DS"
 }



#####callll

gapi.client.calendar.events.patch({
  calendarId: "primary",
  eventId: "7cbh8rpc10lrc0ckih9tafss99",
  resource: eventPatch,
  sendNotifications: true,
  conferenceDataVersion: 1
}).execute(function(event) {
  console.log("Conference created for event: %s", event.htmlLink);
})

#####rESPONSE

  
"conferenceData": {
  "createRequest": {
   "requestId": "7qxalsvy0e",
   "conferenceSolutionKey": {
    "type": "hangoutsMeet"
   },
   "status": {
    "statusCode": "pending"
   }
  }
 }

###
const eventPatch = {
   conferenceData: {
   createRequest: { requestId: "yourRandomString" },
  },
};
let response = await calendar.events.patch({
  calendarId: 'primary',
  eventId: "createdEventID",
  resource: eventPatch,
  sendNotifications: true,
  conferenceDataVersion: 1,
});