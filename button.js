---
---

function goToNewSentence() {
    location.href = "{{ site.baseurl }}/sentences/".concat(getRandomInt());
};

function getRandomInt() {
    return Math.floor(Math.random() * {{ site.collections.sentences.docs | size }} + 1);
}; 