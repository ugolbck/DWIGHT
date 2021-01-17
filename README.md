DWIGHT 
<img align="right" width="200" height="200" src="assets/images/dwight-clipart.jpg">
============================== 

Automated generation of new `The Office` scripts using deep neural networks

How to
------------
1. download the project locally with `git clone https://github.com/ugolbck/DWIGHT.git`
2. `cd DWIGHT` to move in the project directory
3. if `pipenv` is not installed, run `pip install pipenv`
4. run `pipenv install` to install dependencies in the virtual environment
5. `cd src`to move in the source code directory
6. run `uvicorn main:app --port 8080` to run the web server on port 8080
7. try out the model prediction from another terminal by running `curl -X GET "http://localhost:8000/predict/?seed_text=Hello%20Dwight&len_resp=10" -H  "accept: application/json"`, OR visit the URL `http://localhost:8000/predict/?seed_text=Hello%20Dwight&len_resp=10` in your browser. The input sentence here is "Hello Dwight" and we expect a 10 word answer from the bot.


TODO
------------
- Collect data DONE
- Sequence each character's lines DONE
- Try text generation on one character (keras/transformers) DONE
- Get sequence of character conversation, stage direction, etc... DONE
- Create conversationnal model for a given character DONE
- Create a simple API to query model predictions DONE
- Improve architecture performance and query speed
- Handle absolute paths for all OS, handle exceptions, docstrings, improve security
- Create and optimize Docker container for the whole solution
- Create front end that works well with FastAPI
- Find cool domain name and deploy on OVH/other provider
- Advertise + Medium story



Example
------------
'What are you doing?' -> "Just clearing my desk. I can't concentrate."

------------
**Disclaimer**

This project is only for fun purposes, not commercial. I own none of the used data and do not intend on distributing it.
