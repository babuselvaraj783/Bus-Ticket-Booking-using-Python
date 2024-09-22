# Blue Bus Booking System

This repository contains a Python script for a simple bus booking system called "Blue Bus". The script allows users to book bus tickets by selecting various options through a command-line interface.

## Features

The Blue Bus Booking System offers the following features:

1. Route Selection: Choose from 10 different routes starting from Chennai.
2. Timing Selection: Pick a suitable time slot for your journey.
3. Seat Preference: Choose between AC/Non-AC and Seater/Sleeper options.
4. Bus Selection: Pick from 5 different bus operators.
5. Seat Number Selection: Choose a seat number between 1 and 30.
6. Boarding Point Selection: Choose between two boarding points in Chennai.
7. Dropping Point Selection: Select a dropping point based on your destination.
8. Passenger Details: Enter personal information for booking.
9. OTP Verification: Verify your booking with a randomly generated OTP.

## Usage

To use the Blue Bus Booking System:

1. Run the script in a Python environment.
2. Follow the prompts to make your selections for each step of the booking process.
3. Enter your personal details when asked.
4. Verify your booking with the OTP provided.

## Sample Interaction

```
WELCOME TO BLUE BUS!!!
OUR BUS ROUTE DETAILS:
1) Chennai to Coimbatore
2) Chennai to Salem
...

Select the bus route for your journey: 1
you select Chennai to Coimbatore
Your bus route selected successfully!!!

Select the timing
1) 6.00 to 9.00
2) 9.00 to 12.00
...

Enter the timing: 1
you selected 6.00 to 9.00
Time selected successfully!!!

...

Enter your Details
Name: John Doe
Age: 30
Phone Number: 1234567890
Email.id: john@example.com

otp is: 5678
enter otp: 5678
otp is correct

Your details upload successfully!!!
HAPPY JOURNEY!!!
```

## Limitations and Potential Improvements

- The script currently runs in a linear fashion and doesn't allow for easy corrections if a user makes a mistake.
- There's no data persistence - bookings are not saved after the script ends.
- Error handling could be improved to make the system more robust.
- A graphical user interface (GUI) could make the system more user-friendly.

## Contributing

Feel free to fork this repository and submit pull requests with improvements or additional features for the Blue Bus Booking System.

## License

This project is open source and available under the [MIT License](LICENSE).
