# Lumen-Alert
A repository documenting the details, code, setup and associated story for my light based alarm system, Lumen Alert !

## The story
I've always had trouble keeping to a schedule, and I feel that traditional sound based alarms tend to be extremely annoying and stress inducing, so I thought of another sense to annoy to get me on track - The sense of sight !
<br>
Over the past few weeks I worked on making a portable, brick-sized(but not as heavy) device with the capability to track me down and relentlessly bombard me with a beam of light till I get up and go do my work. Equipped with a servo motor for precise angular control, the device (henceforth referred to as Lumen-A ) gets my position from the live feed of my phone that was processed with a Python script (currently) being run on my laptop. Lumen-A isn't satisfied till I leave its field of view, and even when I do, it's ready to hunt me down if I return when I'm not supposed to.
<br>
Another useful feature is the 'Wake-light': A yellow LED pointed at the pillows on my bed that slowly wakes me up in the morning, mimicking the sun but less intense. This is a permanent fixture as the area of coverage is less than in the first case.

## The build

### Components
-Arduino Uno
-Breadboard
-Towerpro Servo motor (9gm Torque)
-Red and Yellow LEDs
-220 Ohm resistor (for LED protection)
-Assorted wires with the required connector types

### Software
-Arduino IDE
-IDLE (for python)
-IP Webcam (Installed on phone)
