# JSON and YAML
I was cruising around the internet looking for some decent python automation scripts for ideas. I ended up at https://www.activestate.com/blog/top-10-tasks-to-automate-with-python/ - This blog seems to be the #1 response and even has a featured snippet on google. 

![](https://i.imgur.com/NUrpQt1.png)

The first 4 scripts are checking and converting json and yaml. I decided I wanted to smash these all together and make a sort of cmd line interface for doing all of these tasks. 

So the concept is to 

Run the program
 - Do you want to 
	 - check if a file is json?
	 - check if a file is yaml?
	 - convert a file from json to yaml?
	 - coverta a file from yaml to json?

![](https://i.imgur.com/detqRpr.png)



Notes: 
- In the conversion functions, if the file doesnt exist or we create the file, we just exit the program with no information.
