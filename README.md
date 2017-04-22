This program in implemented using Python 2.7
To run this program make sure Python 2.7 is installed
https://www.python.org/downloads/

MAC/LINUX Installing via pip:
	1. If pip is not installed:
		Download get-pip.py 		https://pip.pypa.io/en/stable/installing/
		Install pip 	python get-pip.py

	2. If pip is already installed, upgrade it:
		python -m pip install --upgrade pip	to the latest version
	
	3. pip install --user numpy scipy

	4. For user installs, make sure your user install executable directory is on your PATH. Here are 	   example commands for setting the user PATH:

	   Linux:

			# Consider adding this at the end of your ~/.bashrc file
			export PATH="$PATH:/home/your_user/.local/bin"
	   OSX:

			# Consider adding this at the end of your ~/.bash_profile file
			export PATH="$PATH:/Users/your_user/Library/Python/2.7/bin"

	   Replace 'your_user' with your username

	5. pip install -U scikit-learn

Windows:
	Install Anaconda for python 2.7 version:   https://www.continuum.io/downloads



To run the project:

	1. Unzip the finalProject folder
	2. Navigate to finalProject folder in terminal
	3. Execute the project by typing following command
	   python main.py
	4. Program asks for input in the following order
   		input filename, no of folds, lower or upper approximation and output filename
	5. After execution, program prints error rate on the terminal
	6. Final ruleset for the given input is written to output file
