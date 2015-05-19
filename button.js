---
---

document.getElementsByClassName("button").onclick = function () {
    location.href = "{{ site.baseurl }}/sentences/" + getRandomInt();
};

function getRandomInt() {
    return Math.floor(Math.random() * {{ site.posts | size }} + 1);
}; 