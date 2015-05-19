---
---

var button = document.getElementById("button");
button.onclick = goToNewSentence();

function goToNewSentence() {
    location.href = "{{ site.baseurl }}/sentences/" + getRandomInt();
};

function getRandomInt() {
    return Math.floor(Math.random() * {{ site.collections.sentences.docs | size }} + 1);
}; 