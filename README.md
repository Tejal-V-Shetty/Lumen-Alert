# Lumen-Alert
A repository documenting the details, code, setup and associated story for my light based alarm system, Lumen Alert !

## The story
I've always had trouble keeping to a schedule, and I feel that traditional sound based alarms tend to be extremely annoying and stress inducing, so I thought of another sense to annoy to get me on track - The sense of sight !
<br>
<img src="https://github.com/Tejal-V-Shetty/Lumen-Alert/blob/main/Files/Full_view.jpg" alt="Lumen Alert" width=1080>

Over the past few weeks I worked on making a portable, brick-sized(but not as heavy) device with the capability to track me down and relentlessly bombard me with a beam of light till I get up and go do my work. Equipped with a servo motor for precise angular control, the device (henceforth referred to as Lumen-A ) gets my position from the live feed of my phone that was processed with a Python script (currently) being run on my laptop. Lumen-A isn't satisfied till I leave its field of view, and even when I do, it's ready to hunt me down if I return when I'm not supposed to.
<br>

Another useful feature is the 'Wake-light': A yellow LED pointed at the pillows on my bed that slowly wakes me up in the morning, mimicking the sun but less intense. This is a permanent fixture as the area of coverage is less than in the first case.

## The build
I tried to make Lumen-A with components that I already had on hand. The following components can and probably will be upgraded in a future build.
<br>

### Components
- Arduino Uno
- Breadboard
- Towerpro Servo motor (9gm Torque)
- Red and Yellow LEDs
- 220 Ohm resistor (for LED protection)
- Assorted wires with the required connector types

### Software
- Arduino IDE
- IDLE (for python)
- IP Webcam (Installed on phone)

### Miscellaneous
- Cardboard
- Thermocol
- Paper sheets
- Lens(To focus the LED's illumination to a spot)
- Plastic cone with reflective backing
- Metal wire(for mountings wherever necessary)
- Rubber bands

## Assembly
### Circuit
Assemble the circuit on the breadboard as shown in the images below.

### Case
The housing case has a footprint of 20cm X 11cm and is made with cardboard, styrofoam, and paper. 
<br>

The base of thermocol has cutouts for the breadboard, along with holders for the phone and servo. The underside is stuck to a piece of cardboard to provide more structural stability.
<br>

The top cover is made of thick chart paper and has cut-outs for the phone and servo to pop out.

### Peripherals
The peripheral assembly includes mounting the red LED on the servo motor, and mounting the yellow LED on a metal mount directed towards the head of the bed.
<br>

I made a hole in the plastic cone and pushed the LED through, then used a hot-melt glue gun to attach the lens to the plastic cone.
This was attached to the servo using the glue gun and secured with a rubber band.
<br>

The yellow LED was mounted using a rubber band.
<br>

I used rubber bands as they are really cheap and allow for easy dismounting whenever necessary.

## Setup
### Arduino
Open the attached Arduino code in the Arduino IDE. Upload it to the board(ensure that the correct COM porthas been selected) and press the reset button if necessary. If successful, the servo should turn to an angle of 30 degrees(the default set by the code).

### Phone
Firstly, install the IP Webcam application. Turn the mobile hotspot on, start a server and note down the IP address. IP Webcam has an option to run in the background, which ensures it doesn't use up excessive amounts of battery charge. Take a reference photo in the area you plan to keep the device.

### Python
Connect the laptop/computer to the hotspot and enter the IP address in the Python program in the respective URL string variable. Also include the path to the reference photo. Enter the time for the alarm in the ledtype and ltype dictionaries along with the associated LED type(refer to the guide in the code for number correlation).

## Runtime !
Ensure that the Arduino serial COM port isn't being used by any other program. Just run the Python code and it'll keep checking for the presence of a person when the time for the alarm has arrived, and light the LED correspondingly.

## Final notes
This project was really fun and I was happy to be able to make a functional device from an Arduino that had been laying about for 2 years. If possible, I hope to make improvements in the future, mainly making it completely autonomous by using a Power bank for a portable power source, and a Raspberry Pi for image processing. Stronger lights and improved image processing would also improve the effectiveness of Lumen-A. 
<br>

I've learnt a lot from this project, related to both the software(Python code, Arduino code) and also the electronic and mechanical setup of the components. It's been a pleasure working on the project and I hope it continues to be useful in the future.
