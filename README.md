# Multi-Camera-Tracking-for-Missing-Individuals

#Use Case:
Here we specify the use cases this project will tackle.
Firstly, as mentioned before, an immense amount of time and man power is wasted on manually checking and going through hours of footage to track a kidnapper.
Our system will tackle this head on. Simply procure the footage through our application, tag the victim or perpetrator and submit the image. Once that’s done, our application will sift through video footages for you, which would automatically be much faster than manually doing it.  It will come up with a potential route (or routes) that the culprit has taken, thus tracking them down. 
Secondly an extension of our application can also apply to identifying missing people as well. When tagging a person through our application, it tracks them down through the network of city cameras that are available. It also uses their gait, (since facial recognition can fail due to image quality and distance from camera), to track and identify them. Thus giving a potential route (or routes) the missing person has taken as well. 

#How we do it:

First the user (cop/other legal authority) can gather camera footage and submit it to our application, along with the camera’s specific location (since all cameras are geotagged, helps in reducing search to cameras near the one who’s footage is submitted)

We then perform rudimentary object detection to detect all the people and objects in the frame. After which the user can tag the right object(s)/ person(s) to track.

After this we submit the footage to our main system which then runs in other local camera server clusters using kubernetes. Kubernetes deploys the pods, which contain the necessary information and the processing unit necessary to track the object(s)/ person(s) in the footage. This helps in ensuring our system is scalable, failure tolerate and ease of use. Using kubernetes also reduces set up time, and doesn’t require extra hardware to run. It can directly be setup on the existing servers that are used for the cameras. 

After this the route(s) is calculated and shown as output to the user. 

#Algorithm for tracking:

It follows a tree-like level based processing procedure. 
First if tagged object is found in camera 1, using its location (geotag) and the surrounding cameras we go level by level to process the images to check for the tagged object. 
This continues further on, based on the routes taken by object and cameras that are closest in the level.
Now suppose the next level cameras don’t detect the objects? 
This is where the fall back triggers. Based on certain timeout values(based on traffic and distance), if the camera doesn’t detect it within the timeout, it searches based off radius, rather than level. 
Thus from camera 1 it checks in a radius rather than going down a level, until it finds the objects tagged. This of course increases processing and time taken, however it still is a faster and better compared to wasting man power on sifting through hours of camera footage. 

#Tech stack:

We’ll be implementing this in two parts. First using hardware to represent security cameras, and software for building our application. 

Hardware stack:

Raspberry Pi
Pi/ webcams
Together they’ll act as security cameras in our proof of concept implementation. 
The pi collects the video using the picam/ webcam and sends it to the central server, much like how the security feeds are recorded in a city.
And the locations of said pis are known, as our the locations of the security cameras in a city.

Software Stack:

Kubernetes: deployment and scalability
RabbitMQ: network transmissions
Flask: Server side programming
OpenCV: image/video processing
YOLO: image classification
Python

#Drawbacks:

So far the current drawback we face is that we need government support. 
Without it, we have no access to any footage or infrastructure, since we’re using pre-existing structure to reduce cost.
Another issue is blindspots. We won’t be able to do much about blind spots, but we aim to use our fallback to track better and further. While it may not always work, it’s better than nothing.

#Future scope:
We aim to improve our systems in the following ways:

Pre event processing: When tracking tagged objects, we can also add  an extension to track those objects before the event has occurred as well. To see if the kidnapping was planned and to track more culprits if possible.

Anomaly Detection: Certain ML algorithms and models have begun coming up slowly regarding detecting the act/ crime itself. While the datasets aren’t public, their initial research and findings seem promising. Thus we can integrate that as well with our system, making it even faster and better at tracking criminals/ missing people.

 

