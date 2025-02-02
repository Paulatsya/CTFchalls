FROM ubuntu:latest

# Install dependencies in a single RUN command
RUN apt-get update && apt-get -y install python3 python3-pip

# Create ctf-user and group
RUN groupadd -r ctf && useradd -r -g ctf ctf

# Copy necessary files into the container
COPY flag.txt /home/ctf/flag.txt
COPY requirements.txt /home/ctf/requirements.txt
COPY server.py /home/ctf/server.py
COPY vulnerable.db /home/ctf/vulnerable.db

# Set proper permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/server.py
RUN chown ctf:ctf /home/ctf/vulnerable.db
RUN chmod 666 /home/ctf/vulnerable.db
RUN chmod 440 /home/ctf/flag.txt
RUN chmod 440 /home/ctf/requirements.txt

# Install Python requirements
RUN python3 -m pip install --break-system-packages -r /home/ctf/requirements.txt

# Switch to the ctf user
USER ctf

# Command to run the server
CMD ["python3", "/home/ctf/server.py"]
