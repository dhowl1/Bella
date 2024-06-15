# COMS W3132 Individual Project

## Author
Jangho Park. jp4509@columbia.edu

## Project Title
Search engine with ChatGPT API

## Project Description
In "Bella", I aim to create a web-based application that integrates the power of Google's search engine with the ChatGPT conversational ability. This combination will allow users to search for information across the web, as well as interact with the search results in the ChatGPT such as asking clarifications, summaries, or further explanations. The motivation behind this project is that I would like to improve the traditional search experience by making it more interactive and more informative, essentially allowing users to get more information within a single webpage; Arc and Microsoft Bing have developed this feature in their web browsers. This project may be useful for students, researchers, and others who need to use Search engines most of the time and require an understanding of the topic well.

Important to read: There was not many things to do with data structures on my webpage, so I just did a basic one which is stacking history into my stack, which is working well!!

## Overview
![image](https://github.com/coms-w3132/final-project-dhowl1/assets/139436754/fc7c7cac-f1e5-4b42-9af8-d87dbd1b5bad)
![image](https://github.com/coms-w3132/final-project-dhowl1/assets/139436754/f871ba5a-02e3-49a5-aff7-89b6e076339b)

## Timeline
*To track progress on the project, we will use the following intermediate milestones for your overall project. Each milestone will be marked with a tag in the git repository, and we will check progress and provide feedback at key milestones.*
I do not remember the exact dates that I created tags for them, but I did tag everything that were required.

| Date               | Milestone                                                                                              | Deliverables                | Git tag    |
|--------------------|--------------------------------------------------------------------------------------------------------|-----------------------------|------------|
| **March&nbsp;29**  | Submit project description                                                                             | README.md                   | proposal   |
| **April&nbsp;5**   | Update project scope/direction based on instructor/TA feedback                                         | README.md                   | approved   |
| **April&nbsp;12**  | Basic project structure with empty functions/classes (incomplete implementation), architecture diagram | Source code, comments, docs | milestone1 |
| **April&nbsp;19**  | Finishing implementation of UI and basic implementation for API call from Google and ChatGPT           | Source code, unit tests     | milestone2 |
| **April&nbsp;26**  | Completely (or partially) finished implementation                                                      | Source code, documentation  | milestone3 |
| **May&nbsp;10**    | Final touches (conclusion, documentation, testing, etc.)                                               | Conclusion (README.md)      | conclusion |

*The column Deliverables lists deliverable suggestions, but you can choose your own, depending on the type of your project.*

## Requirements, Features and User Stories
I designed this project as following, if users query something on the main search bar, then it trigger Google API and ChatGPT API at the same time so that it can give both results on the results page. There is no need to type the same questions twice. With that, if users want to ask the following questions, they can simply ask ChatGPT in the query box. Moreover, there is a search history button on the bottom right side, once users hit it, it will display the query history that users have looked for on ChatGPT's answer box. 

## Technical Specification
I used HTML, CSS, and JavaScript to make an interactive webpage and used python with flask for handling OpenAI's API and Goolge's API, as well as stacking search history with stack and queue implementation. Also, I used .env for the sake of security hiding actual API keys. I also made the pytest file so that it can test that the main functions are working appropriately.

## System or Software Architecture Diagram
![image](https://github.com/coms-w3132/final-project-dhowl1/assets/139436754/a0777d89-0afb-43b2-a1e0-297bac30cbb2)

## Development Methodology
I kept developing to integrate API call and getting search prompt which will result in creating output in google search and ChatGPT API after users enter on search bar, JavaScript was a big help to allow the webpage to be dynamic. 
I created traditional pytest code so that I can test Python functionalities. The result of the test cases is passed, so it implies my API handling and history function works well as expected.

## Potential Challenges and Roadblocks
I have no experience with using API, so it may cause some challenges and require me to learn about it. It will be challenging to design a webpage with frontend technology, so it may have low-quality UI. There should be pricing for Google API and ChatGPT API, so I may need to handle them. 

The most challenging part of this project was using ChatGPT API. I had trouble with making prompts and implementing JavaScript functions so that they can interact well the most frequent error I have got was "404 error".

## Additional Resources
https://platform.openai.com/docs/api-reference
https://developers.google.com/custom-search/v1/overview
## Conclusion and Future Work
The main goal is to enhance the traditional search engine experience with ChatGPT interaction by making it a more interactive and insightful search tool that retrieves information effectively. The expectation is to build a platform that stands out for its ability to merge the data retrieval of Google search with ChatGPT, thereby offering a comprehensive tool for information discovery and learning. 
At this point, I want to improve some potential error handling on web browsers and definitely would like to improve the general user interface. I want to show the image section as Google does, so I will try to figure out how to make an image section on my web browser.
