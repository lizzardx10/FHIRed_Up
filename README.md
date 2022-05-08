# FHIRed Up

## Inspiration

Our team has a common interest in human health and the nature of this project allowed us to express our passion towards the subject matter. We all know at least one family member that have a hereditary disease and it felt very easy for us to get pumped up about it! 

## What it does

Our program builds upon the previously established EHRs in a way that will lower the amount of time that a doctor/nurse would have to spend in front of the computer. We have made the process simpler and easier to learn for new people in the field, as well as those who are already well established. After connecting to the database, we expedite the process for data retrieval. Once the data is retrieved, we format it in a way that even if a patient accessed the web application only their data would be visible. We also verify that all files that are available do in fact belong to the person in question and take in any new files that are sent over from the lab.

## How we built it

We took various approaches going into this project, and we ended up deciding on using python with streamlit. The reason we settled on this approach was because python would be simpler to use, and the tools for building web apps are very intuitive. We were able to build a working software in a matter of hours, and there weren't (too) many problems that arose while we were using it. We also ran into some of the same issues, but thanks to python being a lot easier than the other languages we fixed them. 

## Challenges we ran into

We had a couple failed attempts before we settled on using streamlit in python. Those attempts will be chronicled below:

Attempt 1: Html web application. We followed the guides given in the SMART FHIR Documentation that we were given, and we were able to create a presentable application. However, we ended up tabling this idea when we started running into errors in the form entries. We tried to remedy the problems with JavaScript scripts and other supplementary materials, but we ended up scrapping the idea to go in other ways.

Attempt 2: C# Form application. We created a Forms app that would be split into different forms to meet the needs of patient and providers alike, but it did not interact with FHIR or follow the format. This would have been the simplest, but it would not have satisfied the challenge that was given as much as we would like. This approach would run on a database that we created to store the data and in turn export it out into a .csv file as we made changes to the database.

## Accomplishments that we're proud of

After all of the time we spent thinking, scrapping ideas we thought were not good enough, building software that we enjoyed making, and re-thinking ideas that we thought were going in the wrong direction; we managed to build something that we are proud of and can show off in our portfolios. We also managed to break down the question enough to help other teams, and each other understand the prompt well enough to create software/presentations. 

## What we learned

We learned that we should trust our instincts when we attempt to tackle a problem. We had a lot of moments where we were on track and began to second guess ourselves, but we learned from the experience. We also picked up a few skills in database manipulation with python and learned to use the streamlit  python library.

## What's next for FHIRed Up

We will continue to grow together and seek out more projects and hackathons to build our portfolios and hopefully gain meaningful employment in the near future. 
Python StreamLit WebApp created for the Hudson Alpha Tech Challenge 2022
Copyright 2022 The FHIR Starters:Anthony McGee, Roberto Padron, Amir Utley

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
