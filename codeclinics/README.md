# Code Clinics Group Project

Code Clinics is a booking CLI system that uses Google API. A student needs to book a specific time slot to attend a Coding Clinic session, and typically these sessions are one-on-one sessions with a more experienced person who can advise on the coding problem at hand.

### Bonus Functionality

There is an ics file - which is a Calendar Document. You can open it and see the bookings in an Application of your choice.

Path: 
```bash
~/code-clinic-booking-system/codeclinics/files/ics
```

## Cloning the repo

Please add the git repo to your home directory. Run all the steps in order as they appear in this document:

```bash
cd ~/
git clone https://github.com/DamianOdendaal/code-clinic-booking-system.git
```

## Setup the System

Make sure you are in ```codeclinics``` directory, then run:

```bash
cd code-clinic-booking-system/codeclinics
chmod +x cal-setup
chmod +x wtc-cal
```

## Bash Configuration

Run the script below in your bash terminal:

```bash
code ~/.bashrc
```

Then inside that ```.bashrc``` file, add the script below at the end of the ```.bashrc``` file.

```bash
export PATH="$HOME/code-clinic-booking-system/codeclinics:$PATH"
```

## Installing Dependencies

Run the following command from any directory to download required packages:

```bash
cal-setup
```

## Running the System

Run the following to see what type of CLI commands work with our system.

### Code Clinic Commands

```bash
wtc-cal
````

### Volunteering for a slot

```bash
wtc-cal volunteer
````

### Viewing Slots

```bash
wtc-cal slots
````

### Booking a Slot

```bash
wtc-cal book <ui_code>
```

### Cancelling a Slot or Cancelling a Booking

```bash
wtc-cal cancel <ui_code>
```

### Running the  Tests
```
python3 -m unittest tests/test_main.py

NOTE: running the tests will raise a ResourceWarning
because we are opening a connection to the
Google Calendar API that later closes automatically.
```

# Authors and Acknowledgement

## Team Members who made this System Possible

Thabang Soulo,
Nkosingiphile Nkosi,
Nicholas Brummer,
Princess Lamola,
Kamogelo Mohlabu, and
Tebogo Tema

Also, all thanks to WeThinkCode for making us think outside the box. We really learned a lot just from working on this simple system.