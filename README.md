# DS Unit 3 Advanced Assignment (Build Week)

Welcome to your first day working at ACME Corp! You are replacing an employee who just got an amazing job offer at Google on the condition that he resign at ACME corp immediately and give no notice (they're fierce competitors of ours).

This has left us in a tough spot here at ACME. The person you are replacing was working on a ML-fueled Recommender System Web App built using song data from Spotify. We promised the client that we would present a basic working prototype of the app to them in just 3 days time, but the project's only half finished! We need you to dive into the code base and see if you can get a basic version of this working before the looming deadline. This is why we pay you the big bucks!

## What you'll find in this repository

- `Spotify_Recommender.ipynb` - This file holds a IPython notebook where the last guy was working on training the machine learning model for the recommender system using a K-Nearest Neighbors Algorithm from Scikit-Learn.

- A Flask app called `spotify` that has a basic interface, but doesn't have any defined database models, doesn't have any song data added to the database, and doesn't have the Machine Learning Model added to it yet!

## Next Steps?

If you could do the following it would really save our bacon:

- Check the Machine Learning model to see if it's making good recommendations; If it's not, let's get the app working first so that we at least have something to show the client and we'll work on improving the ML model if we have time.

- We need to move all of the song data from the CSV dataset into the SQLite database so that we can query the database when we want to display the song recommendations.

- We need to export the ML model from the .ipynb file and include it in the flask app somehow. I've never done it before, but the last guy said something about using a Python Package called Joblib and he shared with me these links a few days back when we were talking about it over Slack:

  - <https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/>

  - <https://maze-runner.medium.com/deploying-the-ml-model-to-the-flask-with-joblib-53f313d24003>

  - <https://www.analyticsvidhya.com/blog/2020/04/how-to-deploy-machine-learning-model-flask/>

- When a person submits a Song Title, we should find that song in the database, send its data through the KNN model to find the row ids of the five most similar songs and then query the database again to get the data of the five recommended songs, and then display that data on the HTML page. There is some fake data in the app that's currently serving as a stand-in for the real data. Once we've got these pieces stitched together we'll want to replace that fake data with the real data so that the real song recommendations will show on the web page when a user submits the form.

Feel free to change any of the files in the app even the HTML files if you feel like you need to. Do whatever you've got to do. I trust your judgement. That's why I hired you.

## If you have time (stretch goals)

If you can get everything I've listed above working then you're just amazing, but let's use all of the time available to make this as impressive as possible for the client. Here's some ideas of other improvements that could be made. I'll leave it up to you to prioritize these.

- Improve the machine learning model so that it's making better recommendations.
  - Maybe we could improve the categorical encoding of the categorical variables in the dataset.
  - Could standardizing the data with StandardScaler help?
  - I bet that the year in which the song was written is a really important piece of information when it comes to making quality recommendations. Can we engineer any features to emphasize the most important columns of data?
  - Should we use a sklearn pipeline somewhere to improve our code's organization?
  - Are there any hyperparameters that we could tune?
  - Have we even started with the right dataset? Maybe there's a better dataset out there that we could use to train the model.

- Is there anything that could be improved with the look and feel of the site like the structure of the HTML or the CSS Styling? I know you don't have very much experience with that, but hey, if we've got time, maybe we give it a shot.

- Can we get the site deployed to Heroku so that we can share a link to the app directly with the client rather than having to show them the development version on one of our computers?

- Maybe we could use the [Spotify API](https://developer.spotify.com/documentation/web-api/) to get additional data about the songs that we have. If we could get information about the song's genre, I bet that would really help us make better recommendations!
