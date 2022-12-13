# Email forwarder #

## Purpose ##

This app simply forwards messages to email addresses it gets via curl using a google service account. 
The point of the app was to play with python.
My previous python experience was simple scripts. 
I tried to play with as many python concepts as possible given the simple premise of the app, so some of the style is inconsistent. 

At the time of writing my day job is C#, but I found python to be quite fun to write as it has incredibly little boiler plate code.


## Techs Used ##

pip3-venv (apparently not included in python3 now)
flask
python3
flask-rest
flask-sqlalchemy
flask-marshmallow
docker
aws lightsail

I have also included the requirements.txt

## Envrionment ##

I used Ubuntu and visual studio code to do the work. 
The new window's terminal is very good.
AWS cli and AWS lightsail were used to deploy.
Docker build for images.

## Hosting ##

AWS lightsail to host. Very easy to to set up!

## How to Use ##

Example payload and curl. The app is hosted on AWS currently, but I did not list here.

curl --location --request PUT 'http://<hostedurl>:5001/email' \
--header 'Content-Type: application/json' \
--data-raw '{
    "address":"russel.hampton@gmail.com"
}'

It will rate limit if you try to send too many emails to the same address.