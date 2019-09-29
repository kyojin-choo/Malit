<img src="https://raw.githubusercontent.com/kyoogoo/Malit/master/icon.png">
# Malit
**Developers**: Daniel Choo, Tristan Gantz, Kenny McDonnell, Adrianne Santinor
**Artist**: Arizza Santos

## Inspiration
<p>Due to increasing trolls and propagandist accounts emerging on Reddit, it is difficult to discern who is "being serious" and who is stirring up controversy to garner attention. Thus, some Reddit threads have been polarizing to the point where Redditors will avoid certain subreddits as there is an influx of trolls, extremists, and/or propagandists. This extension will attempt to expose Reddit trolls and malicious accounts so that Redditors can avoid being deceived.</p>

## What it does
<p>Once you click on the extension, it will list the all of the users in the thread in the window frame and display their "suspicious score." </p>

## How we built it
- HTML/CSS (frontend)
- Javascript/Python
- Custom algorithm to calculate scores and assign them to users in a thread.

## Challenges we ran into
- Establishing a pipeline from the Chrome to Python (still in progress)

## Accomplishments that we're proud of 
- Learning how to use Chrome Extension API
- Fetching usernames from a block of HTML by identifying patterns and implementing regular expressions

## What we learned
- How to create a Chrome extension
- More about regular expressions

## What's next for Malit
- Block malicious comments from appearing on the page
- Assign the score on the page
- More additions to the popup window on the front end
