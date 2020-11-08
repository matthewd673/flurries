function update() {
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("log-container").insertAdjacentHTML("afterbegin", this.responseText);
        }
        //document.write(this.responseText);
            //document.getElementById("log-container").innerHTML += this.responseText;
    };

    xhttp.open("GET", "poll", true);
    xhttp.send();
}