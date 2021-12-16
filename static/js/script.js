// Copyright 2017 Jacques Berger
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
function installation_query() {
    let formData = new FormData(document.getElementById("form-district"));
    let arrondissement = formData.get("arrondissement");
    fetch('/api/installations?arrondissement=' + arrondissement)
        .then(function (response) {
            return response.text();
        }).then(function (text) {

        const json = JSON.parse(text);
        if (json[0].length === 0) {
            document.getElementById("result_search").innerHTML = "<br><br>" + "<h5>No results.</h5>";
        } else {

            let output = "<br><br><h5>" + "Search Result" + "</h5><table class='table table-bordered'> ";
            output += "<thead>";
            output += "<tr class='table-active'><th>" + "ID" + "</th>" + "<th>"
                + "Name" + "</th>" + "<th>" + "District" + "</th></tr></thead>";

            for (let k = 0; k < json.length; k++) {
                for (let j = 0; j < json[k].length; j++) {
                    let obj = json[k][j];

                    output += "<tbody><tr><td>" + obj["id"] + "</td>"  +
                        "<td>" + obj["nom"] + "</td>" + "<td>" + obj["arrondissement"] + "</td></tr></tbody>";
                }
            }
            output += "</table>";
            document.getElementById("result_search").innerHTML = output;
        }
    });
}


function installation_selection(name) {
    fetch('/api/installations-name?nom=' + name)
        .then(function (response) {
            return response.text();
        }).then(function (text) {
        const json = JSON.parse(text);

        let output = "<br><br><h5>" + "Search Result" + "</h5><table class='table table-bordered'> ";
        output += "<thead>";
        output += "<tr class='table-active'><th>" + "ID" + "</th>" + "<th>"
            + "Name" + "</th>" + "<th>" + "District" + "</th></tr></thead>";

        for (let k = 0; k < json.length; k++) {
            for (let j = 0; j < json[k].length; j++) {
                const obj = json[0][j];

                output += "<tbody><tr><td>" + obj["id"] + "</td>"
                    + "<td>" + obj["nom"] + "</td>" + "<td>"
                    + obj["arrondissement"] + "</td></tr></tbody>";
            }
        }
        output += "</table>";
        document.getElementById("result_search").innerHTML = output;
    });
}
