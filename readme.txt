Install instructions:
	- rabbitmq: stable 3.6.4
	- OpenCV: 3.1.0_3
	- pika: 0.10.0

	RabbitMQ and OpenCV were installed using homebrew.
	Pika was installed using Pip.

Testing:
	python test.py

Runtime:
	In separate terminals:
		rabbitmq-server
		python consumer.py
		python producer.py img1_file img2_file output_file

To start off, this took me around 5 hours. Probably a little more than 5 hours. A lot of that was grappling with the differences between OpenCV 1, 2, and 3. Also, installing OpenCV 3 caused me a lot of problems. I ended having to reinstall some of the dependencies so everything would work together.
The method I went with is good at the translation to line up the pictures, but it doesn’t look into filling in the background image; instead, it just leaves black space. If I had more time, the next thing would be to move to migrating the backgrounds of both pictures into one frame. 
If this system was to be set up on multiple machines, one machine would just have to be the designated rabbitmq server and have the connection broker look for that instead of localhost.
Also, depending on the type of translation between registered images, different settings might be better suited. warp_mode is set to translation because of the photo I selected, but there is also rotational. The method that accounts for both rotational and translational took several minutes for me to run each time, which is why I did not use that.
