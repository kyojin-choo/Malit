
chrome.browserAction.onClicked.addListener(function(tab) {
  console.log('Injecting content script(s)');
  
  chrome.tabs.executeScript(tab.id,{
      code: 'document.body.innerHTML;'
  },receiveText);
  
});

function receiveText(resultsArray){
  var x = document.createElement("div")
  x.innerHTML = resultsArray[0];
  
  console.log("TESTTTTTTTTTTTTTTTTTTT");

  var usernames = x.innerHTML.match(/(?<=data-author=").{3,20}(?=".*?data-replies)/g);
  console.log(usernames);
}

/*
chrome.browserAction.onClicked.addListener(function(tab) {
      //console.log(document.getElementsByTagName('a'));
      chrome.tabs.executeScript(tab.id,{
        code: 'document.getElementsByTagName("a");'
    },receiveText);
});

function receiveText(resultsArray){
  console.log(resultsArray[0]);
  //console.log("TESTTTTTTTTTTTTTTTTTTT");
  //console.log(resultsArray[0].search('a'));
}

//<a href="https://old.reddit.com/user/Klaus0225" class="author may-blank id-t2_yi6xb">Klaus0225</a>

//<a href="https://old.reddit.com/user/Vaskre" class="author may-blank id-t2_5p3p5">Vaskre</a>

chrome.browserAction.onClicked.addListener(function(tab) {
  var all_a = document.getElementsByTagName("a");
  console.log(all_a);
  var authors = []; 
  for (var i = 0; i < all_a.length; i++) { 
    var a = all_a[i]; 
    if (a.className.match(/^author_\d+$/)) { 
      authors.push(a.innerHTML); }
  }
  console.log(authors.length);
  for (var i = 0; i < authors.length; i++) {
    console.log(authors[i]);
  }
});
*/
