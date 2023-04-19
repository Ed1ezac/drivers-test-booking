## Drivers-test-booking system
This is a django system that helps people book tests for a driver's license assessment. People will be presented a list of venues with dates. They can then select register to book a spot for that date or cancel their booking.

## Project Status
<p align="center">
<img src="https://img.shields.io/badge/development-Maintenance & Updates-blue" alt="development status"/>
</p>

## Technology Used
This system was made using the Django framework, a python framework for web system development and these technologies:

|Technology       |Description   |
|:---------------:|:------------:|
| <a href="https://tailwindcss.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" alt="tailwind" width="40" height="40"/> </a> | Tailwind CSS v2.2.15 |


## Requirements
If you intend to make additions to this project you need to meet the following (Minimum requirements):
- Python V3.7.9 
- pip 23.0.1

## Architecture & Directories
This project's architecture follows the Django framework architecture and directory structure. The root folder contains 5 folders:
- `administrator` - an abstraction for the administrator's functionality
- `bookinng_project` - the core project folder
- `templates` - holds the html pages
- `test_dates` - an abstraction for the TestDate functionality
- `theme` - an abstraction for the CSS styling of the system
- `users` - an abstraction for the CustomUser and its roles and permissions 

Each abstraction is a mini-app with its own `view.py`, `urls.py` and `models.py`, `tests.py`, `forms` and `migrations` to drive the functionality.

## Local Configuration
- Download and unzip the project
- If you have Visual Studio Code IDE you can use its built-in command processor by clicking `Terminal`->`New Terminal` on the top ribbon menu
- Otherwise fire up your console app *(e.g command prompt on windows)* and navigate to the project folder 
- Run the commands: `pipenv shell`
- Install css dependencies: `python manage.py tailwind install`
- `python manage.py migrate`
- Serve the application by using the command: `python manage.py runserver`
- Navigate to http://localhost:8000 to view it

## Testing
In order to test the app you can use Django built in testing:
- Each mini-app (`administrator`, `officer`, `test_dates` folders) has a test.py file
- We can add tests to each to test functionality on that paritcular area 
- To run the tests we use the `python manage.py test` command
- If all is good we won't get any error

## Possible Improvements
- Display dates in calendar widget
- TestResult model functionality
- email verification to mailgun
