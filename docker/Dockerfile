# Base image
FROM ros:humble

ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install necessary packages for USB device mounting
RUN apt-get update && apt-get install -y \
    usbutils \
    udev \
    python3-pip \
    python3-opencv 

###################################################################

# Create a mount point for the USB device
RUN mkdir /mnt/usb
RUN pip install pygame
RUN pip install opencv-contrib-python==4.6.0.66
RUN pip install RPi.GPIO

# Set up udev rules for USB device detection
RUN echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="054c", ATTR{idProduct}=="05c4", MODE="0666"' >> /etc/udev/rules.d/99-usb.rules


# Add ros sourcing to bashrc
RUN echo ". /opt/ros/humble/setup.bash" >> ~/.bashrc

# Create Ros workspace
ENV EXOMY_WS=/WS/orion_ws
RUN mkdir -p $EXOMY_WS/src

WORKDIR /WS/orion_ws

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
