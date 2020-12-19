# E2E_Generators_v0.1

# Welcome to the DevSpaces Team Speed Hackathon
There are two coding challenges for your team to work on.
They are found in the `contact-tracing` and `decryption` directories of this project.
The event host will run a test script using designed inputs on your completed project.
Scoring is shown below. Tiebreaker is earliest submission time.
| Challenge | Result | Points |
| ----------- | ----------- | ----------- |
| Decrypt | Solved | 50 |
| Contact Tracing | All traces found |  50 |
| Contact Tracing | At least half of traces found |  25 |

## Process
1. Fork this repo, make it public, give your team members access to commit
2. Give the event host the project url
3. Let the event host know when completed
4. Event host will clone your repo and run evaluation script with real input
5. NOTE: stdout is not used for judging, only the designated OUTPUT_FILE

## Contact Tracing Challenge
You are given a set of time-based person location data in `locations.csv` and 
virus exposure notifications in `exposure.csv`. Your task is to write to `output.csv`
a set of people who were exposed based on the following criteria.
- The world is a 10x10 dimension specified as x, y coordinates in the locations input
- Time is noted as an increasing integer series, i.e. `t=1`, `t=2`, etc.
- `locations.csv` format is `Time,Person,x,y`
- `exposure.csv` format is #Time,Person
- `output.csv` format is `TraceId,Time,Person`. TraceId can be any integer value. Only the first exposure (two consecutive time periods) needs to be noted in this file.
- A person is `exposed` if they are in an adjacent spot (including diagonals) for at least two consective time intervals with someone who was exposed previously
- See the example Ruby code for more details. You can run `./trace.rb`


## Message Decryption Challenge
This one is pretty simple, at least in terms of the problem. The input.txt has a decrypted message
and your job is to decrypt it. It does not use RSA encryption or anything like this.
It is a reasonable solution that can be found using character manipulation.
Run `./decrypt.rb` and see the example. Note that you will need to change the code
to point to the real input.

For convenience, the output of the test example is shown here:
```
Note this is the test input. See the real input.txt for this challenge.
The test uses ceasar cipher with -3 character offset.
 
TEST Input Message
------------------
Wklv#lv#d#whvw#phvvdjh
 
Decrypted Content
-----------------
This is a test message
```
